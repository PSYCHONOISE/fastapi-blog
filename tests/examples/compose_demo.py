from fastapi import FastAPI

import fastapi_blog


app = FastAPI(title='fastapi-blog demo')
app = fastapi_blog.add_blog_to_fastapi(app, locales=['en', 'ru'], default_locale='en', strict_frontmatter=False, health_routes=True)
