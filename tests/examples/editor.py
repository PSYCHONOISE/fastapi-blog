from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

import fastapi_blog


app = FastAPI()
app.add_middleware(SessionMiddleware, same_site='lax', secret_key='example-only-session-secret-value-0123456789abcdef0123456789')
app = fastapi_blog.add_blog_to_fastapi(app, strict_frontmatter=False, sanitize_html=False)
app = fastapi_blog.add_editor_to_app(app, strict=False, require_auth=True)
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get('/')
async def index() -> dict:
    return {'message': 'Blog at /blog, editor API at /api/posts (see /docs)', 'blog': 'http://localhost:8000/blog', 'api_docs': 'http://localhost:8000/docs'}
