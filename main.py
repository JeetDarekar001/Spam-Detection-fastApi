from tkinter.messagebox import RETRY
from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def get_root():
    return {"Hello User":" Welcome to Spam Detection App"}