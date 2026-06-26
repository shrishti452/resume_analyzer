console.log("JS Loaded");
const button = document.getElementById("btn");
const output = document.getElementById("output");

button.addEventListener("click", async () => {

    const response = await fetch("http://127.0.0.1:5000/api/test");

    const data = await response.json();

    output.innerText = data.message;

});

const fileInput = document.getElementById("resumeFile");
const uploadBtn = document.getElementById("uploadBtn");
const uploadStatus = document.getElementById("uploadStatus");

uploadBtn.addEventListener("click", async () => {

    const file = fileInput.files[0];

    const jobDescription =
    document.getElementById("jobDescription").value;

    console.log(jobDescription);
    
    if (!file) {
        uploadStatus.innerText = "Please select a file";
        return;
    }

    const formData = new FormData();

    formData.append("resume", file);

    formData.append("job_description", jobDescription);
    
    const response = await fetch(
        "http://127.0.0.1:5000/upload",
        {
            method: "POST",
            body: formData
        }
    );

    const data = await response.json();

    uploadStatus.innerText =
        `
ATS Score: ${data.score}%

Matched Skills:
${data.matched_skills.join(", ")}

Missing Skills:
${data.missing_skills.join(", ")}
`;

});