from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI(title=" Pixel Pirates")

# ---------------- HOME PAGE ----------------
@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>CurrHub | Pixel Pirates</title>
<style>
body{
    margin:0;
    font-family:Segoe UI, Arial, sans-serif;
    background:linear-gradient(135deg,#5f5bd8,#7c73e6);
    color:white;
}
nav{
    background:white;
    color:#5f5bd8;
    padding:15px 40px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    box-shadow:0 4px 10px rgba(0,0,0,0.1);
}
nav a{
    text-decoration:none;
    color:#5f5bd8;
    margin-left:20px;
    font-weight:600;
}
.hero{
    text-align:center;
    padding:90px 20px;
}
.hero h1{
    font-size:42px;
}
.section{
    padding:60px 40px;
}
.cards{
    display:flex;
    flex-wrap:wrap;
    justify-content:center;
    gap:25px;
}
.card{
    background:white;
    color:#333;
    width:280px;
    padding:25px;
    border-radius:18px;
    text-align:center;
    box-shadow:0 15px 30px rgba(0,0,0,0.18);
}
footer{
    background:#1f1f3d;
    padding:20px;
    text-align:center;
    font-size:14px;
}
</style>
</head>

<body>
<nav>
  <b>CurrHub 🚀</b>
  <div>
    <a href="/">Home</a>
    <a href="/generator">Generator</a>
    <a href="#">About</a>
  </div>
</nav>

<div class="hero">
  <h1>AI Curriculum Builder for Engineers</h1>
  <p>Designed by <b>Pixel Pirates</b> – Build Smarter, Faster</p>
</div>

<div class="section">
<h2 style="text-align:center">💻 CSE Engineering Courses</h2>
<div class="cards">
  <div class="card">
    <h3>Artificial Intelligence</h3>
    <p>ML, NLP, Neural Networks & real-world AI systems</p>
  </div>
  <div class="card">
    <h3>Data Science</h3>
    <p>Python, Data Analytics, Visualization & Big Data</p>
  </div>
  <div class="card">
    <h3>Cyber Security</h3>
    <p>Ethical Hacking, Network Security & Cryptography</p>
  </div>
  <div class="card">
    <h3>Cloud Computing</h3>
    <p>AWS, Azure, DevOps & Cloud Architecture</p>
  </div>
</div>
</div>

<footer>
© 2026 CurrHub | Built by <b>Pixel Pirates</b>
</footer>

</body>
</html>
"""

# ---------------- GENERATOR PAGE ----------------
@app.get("/generator", response_class=HTMLResponse)
def generator():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Curriculum Generator</title>
<style>
body{
    font-family:Segoe UI, Arial;
    background:linear-gradient(135deg,#5f5bd8,#7c73e6);
    padding:50px;
}
.box{
    background:white;
    max-width:1000px;
    margin:auto;
    padding:35px;
    border-radius:18px;
    display:flex;
    gap:30px;
    box-shadow:0 20px 40px rgba(0,0,0,0.25);
}
input{
    width:100%;
    padding:12px;
    margin-top:12px;
    border-radius:8px;
    border:1px solid #ccc;
}
button{
    margin-top:25px;
    padding:14px;
    width:100%;
    background:#5f5bd8;
    color:white;
    border:none;
    border-radius:10px;
    font-size:16px;
    cursor:pointer;
}
.right{
    background:#f4f4ff;
    padding:25px;
    border-radius:15px;
    flex:1;
}
</style>
</head>

<body>
<div class="box">
<div style="flex:1">
<h2>Create Curriculum</h2>
<form method="post" action="/generate">
<input name="student_name" placeholder="Student Name" required>
<input name="roll_no" placeholder="Roll Number" required>
<input name="course" placeholder="Course Name" required>
<input name="level" placeholder="Education Level (B.Tech / M.Tech)">
<input name="semesters" placeholder="Number of Semesters">
<input name="industry" placeholder="Industry Focus">
<input name="team" value="Pixel Pirates" readonly>
<button type="submit">Generate Curriculum</button>
</form>
</div>

<div class="right">
<h3>⚡ Why CurrHub?</h3>
<p>✔ AI-powered academic design</p>
<p>✔ Industry-aligned syllabus</p>
<p>✔ Built by <b>Pixel Pirates</b></p>
</div>
</div>
</body>
</html>
"""

# ---------------- GENERATION RESULT ----------------
@app.post("/generate", response_class=HTMLResponse)
def generate(
    student_name: str = Form(...),
    roll_no: str = Form(...),
    course: str = Form(...),
    level: str = Form(""),
    semesters: str = Form(""),
    industry: str = Form(""),
    team: str = Form("")
):
    return f"""
<!DOCTYPE html>
<html>
<body style="font-family:Segoe UI, Arial;background:#eef;padding:50px;">
<h2>📘 Generated Curriculum</h2>

<p><b>Student:</b> {student_name}</p>
<p><b>Roll No:</b> {roll_no}</p>
<p><b>Team:</b> {team}</p>

<hr>

<p><b>Course:</b> {course}</p>
<p><b>Level:</b> {level}</p>
<p><b>Industry Focus:</b> {industry}</p>

<h3>📚 Course Structure</h3>
<ul>
<li>Foundations & Basics</li>
<li>Core Engineering Concepts</li>
<li>Hands-on Labs & Mini Projects</li>
<li>Industry Case Studies</li>
<li>Capstone Project</li>
</ul>

<h3>🎯 Learning Outcomes</h3>
<ul>
<li>Strong conceptual clarity</li>
<li>Practical problem-solving skills</li>
<li>Industry readiness</li>
</ul>

<br>
<a href="/" style="text-decoration:none;font-weight:bold;">⬅ Back to Home</a>
</body>
</html>
"""