from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import fastapi_blog


app = FastAPI(title='Multilingual Blog Admin')
fastapi_blog.add_blog_to_fastapi(app, prefix='blog', strict_frontmatter=False, sanitize_html=False, locales=['en', 'ru'], default_locale='en')
admin = fastapi_blog.add_admin_to_app(app, title='Админ-панель блога', base_url='/admin', admin_username='admin', admin_password='Admin123!', secret_key='change-me-in-production', insecure_dev=True, i18n_enabled=True, i18n_default_locale='en', i18n_locales=['en', 'ru'])
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get('/')
async def index() -> dict:
    return {'message': 'Multilingual admin panel example', 'blog': 'http://localhost:8000/blog', 'admin_en': 'http://localhost:8000/admin (switch to English in UI)', 'admin_ru': 'http://localhost:8000/admin (по умолчанию русский)', 'credentials': {'username': 'admin', 'password': 'Admin123!'}, 'note': 'Language can be switched in the admin interface'}
