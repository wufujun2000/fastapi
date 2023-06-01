from fastapi import FastAPI, Query
from pydantic import BaseModel

import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.get("/test")
async def test(params_1: str=Query(...), params_2: str=Query(...)):
    return{"result": {params_1, params_2}}

@app.get("/login")
async def login():
    return{'toke':'xxxxxxxx'}


if __name__ == '__main__':
    uvicorn.run(app = app)