from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

import fastapi_blog


app = FastAPI(title='Blog with Optional API')
app.add_middleware(SessionMiddleware, secret_key='example-only-session-secret-value-0123456789abcdef0123456789', same_site='lax')
fastapi_blog.add_blog_to_fastapi(app, prefix='blog', include_api=True, api_prefix='/api/posts', api_require_auth=True, strict_frontmatter=False, sanitize_html=False)
fastapi_blog.add_admin_to_app(app, title='Blog Admin', admin_username='admin', admin_password='Admin123!', secret_key='example-only-session-secret-value-0123456789abcdef0123456789', insecure_dev=True, add_session_middleware=False)
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get('/')
async def index() -> dict:
    return {'message': 'Blog with optional REST API example', 'blog': 'http://localhost:8000/blog', 'admin': 'http://localhost:8000/dashboard', 'api_docs': 'http://localhost:8000/docs', 'note': 'REST API at /api/posts requires authentication'}
