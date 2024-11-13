from fastapi import Body, FastAPI
from schemas import Post
# from fastapi.params import Body

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/posts")
def create_post(post: Post):
    return {"message": post}