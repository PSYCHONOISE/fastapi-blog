import sys
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import fastapi_blog
from fastapi_blog.admin import RoleModelView, UserWithRolesModelView


for mod in list(sys.modules.keys()):
    if mod.startswith('fastapi_blog'):
        del sys.modules[mod]
Path('posts').mkdir(exist_ok=True)
Path('pages').mkdir(exist_ok=True)
Path('static').mkdir(exist_ok=True)
app = FastAPI(title='Blog with Roles')
fastapi_blog.add_blog_to_fastapi(app, prefix='blog', strict_frontmatter=False, sanitize_html=False)
admins = fastapi_blog.add_admin_to_app(app, title='Blog Admin with Roles', admin_username='admin', admin_password='Admin123!', secret_key='change-me-in-production', insecure_dev=True, locales=['en', 'ru'], default_locale='en')
for locale, admin in admins.items():
    from fastapi_blog.admin.models import Role, UserWithRoles
    role_view = RoleModelView(Role, icon='fa fa-shield')
    admin.add_view(role_view)
    user_roles_view = UserWithRolesModelView(UserWithRoles, icon='fa fa-users-cog')
    admin.add_view(user_roles_view)
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get('/')
async def root():
    return {'message': 'Welcome to FastAPI Blog with Role Management!', 'links': {'blog': 'http://localhost:8000/blog', 'admin': 'http://localhost:8000/admin'}, 'features': ['Role-based access control', 'User management with roles', 'Granular permissions'], 'admin_login': {'username': 'admin', 'password': 'Admin123!'}}
