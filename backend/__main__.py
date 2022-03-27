# main.py
from fastapi import FastAPI
app = FastAPI()
from backend.routes import demo_route

@app.get("/")
def hello():
    return {"message":"Hello, switching to pipenv."}

app.include_router(demo_route.router, prefix='/demo')
