import os
import sys
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import fastapi_blog


for mod in list(sys.modules.keys()):
    if mod.startswith('fastapi_blog'):
        del sys.modules[mod]
Path('posts').mkdir(exist_ok=True)
Path('pages').mkdir(exist_ok=True)
Path('static').mkdir(exist_ok=True)
app = FastAPI(title='My Blog with Env Vars')
fastapi_blog.add_blog_to_fastapi(app, prefix='blog', strict_frontmatter=False, sanitize_html=False)
admins = fastapi_blog.add_admin_to_app(app, title='Blog Admin', secret_key=os.environ.get('SECRET_KEY'), locales=['en', 'ru'], default_locale='en')
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get('/')
async def root():
    import os
    include_api = os.getenv('FASTAPI_BLOG_INCLUDE_API', 'false')
    admin_login = os.getenv('FASTAPI_BLOG_ADMIN_LOGIN', 'admin')
    return {'message': 'Welcome to FastAPI Blog with Environment Variables!', 'environment_variables': {'FASTAPI_BLOG_INCLUDE_API': include_api, 'FASTAPI_BLOG_ADMIN_LOGIN': admin_login, 'FASTAPI_BLOG_ADMIN_PASSWORD': '***' if os.getenv('FASTAPI_BLOG_ADMIN_PASSWORD') else 'unset'}, 'links': {'blog': 'http://localhost:8000/blog', 'admin': 'http://localhost:8000/admin', 'api_docs': 'http://localhost:8000/docs'}, 'info': {'rest_api': 'Enabled' if include_api.lower() in ('true', '1', 'yes') else 'Disabled', 'admin_username': admin_login}}
