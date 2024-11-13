from fastapi import FastAPI
from routes import entidad1_route, entidad2_route

app = FastAPI()

app.include_router(entidad1_route.router, prefix='/entidad1s')
app.include_router(entidad2_route.router,prefix='/entidad2s')