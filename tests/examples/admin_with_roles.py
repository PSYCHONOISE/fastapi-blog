from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request
from starlette.responses import Response
from starlette_admin.auth import AdminUser, AuthProvider
from starlette_admin.contrib.sqla import Admin, ModelView
from starlette_admin.exceptions import FormValidationError, LoginFailed

import fastapi_blog
from fastapi_blog.admin.database import create_engine_and_session
from fastapi_blog.admin.models import Post, User


Path('posts').mkdir(exist_ok=True)
Path('pages').mkdir(exist_ok=True)
Path('static').mkdir(exist_ok=True)
USERS = {'admin': {'name': 'Admin User', 'password': 'password', 'roles': ['admin'], 'avatar': 'https://ui-avatars.com/api/?name=Admin+User&background=0D8ABC&color=fff'}, 'editor': {'name': 'Editor User', 'password': 'password', 'roles': ['editor'], 'avatar': 'https://ui-avatars.com/api/?name=Editor+User&background=FF6B6B&color=fff'}, 'viewer': {'name': 'Viewer User', 'password': 'password', 'roles': ['viewer'], 'avatar': 'https://ui-avatars.com/api/?name=Viewer+User&background=4ECDC4&color=fff'}}

class RoleBasedAuthProvider(AuthProvider):

    async def login(self, username: str, password: str, remember_me: bool, request: Request, response: Response) -> Response:
        if len(username) < 3:
            raise FormValidationError({'username': 'Username must be at least 3 characters'})
        user = USERS.get(username)
        if user and user['password'] == password:
            request.session.update({'username': username})
            return response
        raise LoginFailed('Invalid username or password')

    async def is_authenticated(self, request: Request) -> bool:
        username = request.session.get('username')
        if username in USERS:
            request.state.user = USERS[username]
            return True
        return False

    def get_admin_user(self, request: Request) -> AdminUser | None:
        user = request.state.user
        return AdminUser(username=user['name'], photo_url=user['avatar'])

    async def logout(self, request: Request, response: Response) -> Response:
        request.session.clear()
        return response

class UserView(ModelView):

    def is_accessible(self, request: Request) -> bool:
        return 'admin' in request.state.user.get('roles', [])

    def can_delete(self, request: Request) -> bool:
        return 'admin' in request.state.user.get('roles', [])

class PostView(ModelView):

    def is_accessible(self, request: Request) -> bool:
        roles = request.state.user.get('roles', [])
        return 'admin' in roles or 'editor' in roles

    def can_delete(self, request: Request) -> bool:
        return 'admin' in request.state.user.get('roles', [])

    def can_edit(self, request: Request) -> bool:
        roles = request.state.user.get('roles', [])
        return 'admin' in roles or 'editor' in roles

    def can_create(self, request: Request) -> bool:
        roles = request.state.user.get('roles', [])
        return 'admin' in roles or 'editor' in roles
app = FastAPI(title='Blog with RBAC')
fastapi_blog.add_blog_to_fastapi(app, prefix='blog', strict_frontmatter=False, sanitize_html=False)
app.add_middleware(SessionMiddleware, same_site='lax', secret_key='example-only-session-secret-value-0123456789abcdef0123456789')
engine, _ = create_engine_and_session()
admin = Admin(engine, title='Blog Admin (RBAC)', base_url='/admin', auth_provider=RoleBasedAuthProvider())
admin.add_view(UserView(User, icon='fa fa-users'))
admin.add_view(PostView(Post, icon='fa fa-blog', label='Blog Posts'))
admin.mount_to(app)
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get('/')
async def root():
    return {'message': 'Blog with Role-Based Access Control', 'admin_panel': 'http://localhost:8000/admin', 'test_users': [{'username': 'admin', 'password': 'password', 'roles': ['admin'], 'permissions': 'Full access - can create, edit, delete everything'}, {'username': 'editor', 'password': 'password', 'roles': ['editor'], 'permissions': 'Can create and edit posts, but cannot delete'}, {'username': 'viewer', 'password': 'password', 'roles': ['viewer'], 'permissions': 'Read-only access, cannot access admin panel'}], 'note': 'Try logging in with different users to see role-based permissions'}
