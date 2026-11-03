from fastapi import FastAPI

import fastapi_blog


app = FastAPI()

@app.get('/api')
async def index() -> dict:
    return {'message': 'Check out the blog at the URL', 'url': 'http://localhost:8000'}
app = fastapi_blog.add_blog_to_fastapi(app, prefix=None)
