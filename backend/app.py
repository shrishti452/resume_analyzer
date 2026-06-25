from flask import Flask,request
from flask_cors import CORS
from resume_parser import extract_text_from_pdf

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

    file_path = f"uploads/{file.filename}"

    file.save(file_path)

    resume_text = extract_text_from_pdf(file_path)

    print(resume_text)

    return {
        "message": "Resume Uploaded Successfully"
    }

if __name__ == "__main__":
    app.run(debug=True)