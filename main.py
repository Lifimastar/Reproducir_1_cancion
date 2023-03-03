from fastapi import FastAPI, File, UploadFile
import pygame.mixer

app = FastAPI()

@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):
    with open("temp.mp3", "wb") as buffer:
        buffer.write(await file.read())
    return {"filename": file.filename}

@app.get("/play/")
async def play_file():
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    return {"estado": "reproduciendo"}

@app.get("/stop/")
async def stop_player():
    pygame.mixer.music.stop()
    return {"estado": "detenido"}

