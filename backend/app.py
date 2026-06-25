from flask import Flask,request
from flask_cors import CORS
from resume_parser import extract_text_from_pdf
from ats_calculator import calculate_ats_score

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

    ats_result = calculate_ats_score(resume_text)

    print(ats_result)

    return ats_result

if __name__ == "__main__":
    app.run(debug=True)