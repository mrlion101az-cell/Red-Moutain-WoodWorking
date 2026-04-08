from flask import request, jsonify
import os

UPLOAD_FOLDER = "uploads"

def register_routes(app):

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    @app.route("/")
    def home():
        return "Construction AI is running."

    @app.route("/upload", methods=["POST"])
    def upload_file():
        file = request.files.get("file")

        if not file:
            return jsonify({"error": "No file uploaded"}), 400

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        return jsonify({
            "message": "File uploaded",
            "path": filepath
        })
