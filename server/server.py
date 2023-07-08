from flask import Flask, render_template, send_from_directory, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    message = requests.get("message")
    print("Received chat:", message)
    return "Message received"

@app.route("/imageBlobLink")
def get_image_blob_link():
    file_path = "static/images/Azurite001.png"
    return send_from_directory("static", file_path)

@app.route("/getRecentMessages")
def get_recent_messages():
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
