from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import fastapi_blog


Path('posts').mkdir(exist_ok=True)
Path('pages').mkdir(exist_ok=True)
Path('static').mkdir(exist_ok=True)
app = FastAPI(title='My Blog')
fastapi_blog.add_blog_to_fastapi(app, prefix='blog', strict_frontmatter=False, sanitize_html=False, locales=['en', 'ru'], default_locale='en')
admins = fastapi_blog.add_admin_to_app(app, title='Blog Admin', admin_username='admin', admin_password='Admin123!', secret_key='change-me-in-production', insecure_dev=True, locales=['en', 'ru'], default_locale='en', enable_role_management=True)
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get('/')
async def root():
    return {'message': 'Welcome to FastAPI Blog!', 'links': {'blog': 'http://localhost:8000/blog', 'admin': 'http://localhost:8000/admin', 'api_docs': 'http://localhost:8000/docs'}, 'admin_login': {'username': 'admin', 'password': 'Admin123!', 'note': '⚠️ Change these credentials in production!'}, 'first_steps': ['1. Go to /admin and login', '2. Create your first blog post', '3. View it at /blog']}
