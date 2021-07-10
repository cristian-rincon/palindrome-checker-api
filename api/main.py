from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get('/')
async def home():
    return RedirectResponse('/docs')


@app.get('/ping')
async def ping():
    return {'message': 'pong'}
