from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>GenAI Curriculum Designer</title>
        <style>
            body { font-family: Arial; background:#f4f6f9; padding:20px; }
            .box { background:white; padding:20px; width:600px; margin:auto; border-radius:10px; }
            button { padding:10px; background:#3498db; color:white; border:none; }
        </style>
    </head>
    <body>
        <div class="box">
            <h2>Generative AI Curriculum Designer</h2>
            <form action="/generate" method="post">
                <input name="course" placeholder="Course Name" required><br><br>
                <input name="level" placeholder="Education Level" required><br><br>
                <input name="industry" placeholder="Industry Focus"><br><br>
                <button type="submit">Generate</button>
            </form>
        </div>
    </body>
    </html>
    """

@app.post("/generate", response_class=HTMLResponse)
def generate(course: str = Form(...), level: str = Form(...), industry: str = Form(...)):
    return f"""
    <html>
    <body style="font-family:Arial; background:#ecf0f1; padding:20px;">
        <h2>Generated Curriculum</h2>
        <p><b>Course:</b> {course}</p>
        <p><b>Level:</b> {level}</p>
        <p><b>Industry:</b> {industry}</p>

        <h3>Course Structure</h3>
        <ul>
            <li>Introduction</li>
            <li>Core Concepts</li>
            <li>Practical Applications</li>
            <li>Industry Case Studies</li>
            <li>Project</li>
        </ul>

        <h3>Learning Outcomes</h3>
        <ul>
            <li>Understand fundamentals</li>
            <li>Apply concepts</li>
            <li>Develop industry skills</li>
        </ul>

        <a href="/">Go Back</a>
    </body>
    </html>
    """