from flask import Flask,request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/")
def home():
    return "Smart Resume Analyzer Backend Running!"


@app.route("/api/test")
def test():
    return {
        "message": "API Working Successfully",
        "project": "Smart Resume Analyzer"
    }

@app.route("/upload", methods=["POST"])
def upload_resume():

    file = request.files["resume"]

    file.save(f"uploads/{file.filename}")

    return {
        "message": "Resume Uploaded Successfully"
    }

if __name__ == "__main__":
    app.run(debug=True)