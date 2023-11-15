from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/index/chart')
async def index_chart() :
    return {'hello' : 'worlds'}