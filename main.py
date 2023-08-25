from fastapi import FastAPI
from chroma import results
from lang import agent

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test")
async def test():
    return {"message": ""}

@app.get("/chroma")
async def chroma():
    return results

@app.get("/lang")
async def lang():
    return agent.run("whats the opposite of a cat?")