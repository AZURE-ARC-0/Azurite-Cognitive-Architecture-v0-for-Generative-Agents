from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Access-Control-Allow-Origin"],
)

connected_websockets = set()


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.websocket("/chat")
async def chat(websocket: WebSocket):
    await websocket.accept()
    connected_websockets.add(websocket)
    try:
        while True:
            message = await websocket.receive_text()
            print("Received chat:", message)
            await broadcast_message(message)
    except WebSocketDisconnect:
        connected_websockets.remove(websocket)
        print("Client disconnected")

async def broadcast_message(message: str):
    for websocket in connected_websockets:
        await websocket.send_text(message)


@app.get("/imageBlobLink")
async def get_image_blob_link():
    file_path = "static/images/Azurite001.png"
    return FileResponse(file_path)


@app.get("getRecentMessages")
async def get_recent_messages():
    return [{"status": "success"}]


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000)
