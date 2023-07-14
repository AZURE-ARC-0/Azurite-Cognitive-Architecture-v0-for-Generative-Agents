from flask import Flask, request
from services.handler import DataHandler
from typing import Dict, List

app = Flask(__name__)

handler = DataHandler()


@app.route("/chat", methods=["POST, GET"])
def chat(message: List[Dict[str, str]]):
    req: List[Dict[str, str]] = request.get_data(message)
    response: GeneratorExit = handler.handle_chat(req)
    print(response)
    return response


@app.route("/imageBlobLink")
def get_image_blob_link():
    return handler.handle_image()


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
