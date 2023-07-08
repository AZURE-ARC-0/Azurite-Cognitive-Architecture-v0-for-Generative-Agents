from flask import Flask, render_template
import requests
from server.handler import Handler

app = Flask(__name__)

handler = Handler()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    message = requests.get("message")
    return handler.handle_chat(message, "user")

@app.route("/imageBlobLink")
def get_image_blob_link():
    return handler.handle_image()

@app.route("/getRecentMessages")
def get_recent_messages():
    return handler.handle_recent_messages()

@app.route("/scrapeSite", methods=["POST"])
def scrape_site():
    links = requests.get("links")
    return handler.handle_scrape_site(links)

@app.route("/vectordbAddDocument", methods=["POST"])
def vectordb_add_document():
    data = requests.get("data")
    return handler.vectordb_add_document(data)

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
