# 🧠 ResumeIQ — AI-Powered Resume Analyzer & Job Match System

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-black?style=for-the-badge&logo=flask)
![AI](https://img.shields.io/badge/AI-NLP%20Powered-purple?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> **Final Year Project — Master of Computer Science (MCS)**
> An intelligent web application that analyzes your resume using Artificial Intelligence and tells you exactly what's missing, how strong it is, and how well it matches a job.

---

## 🤔 What is ResumeIQ? (In Simple Words)

Imagine you apply for a job. Before your resume reaches a human, a **computer software called ATS (Applicant Tracking System)** scans it. If your resume doesn't have the right keywords and format — it gets **rejected automatically**. You never even get a chance!

**ResumeIQ solves this problem.**

You upload your resume → Our AI reads it → It tells you:

- ✅ What skills you have
- ❌ What skills are missing
- 📊 How strong your resume is (ATS Score)
- 🎯 How well your resume matches a specific job

**Think of it like a smart friend who is an HR expert and reviews your resume in seconds — for free!**

---

## ✨ Features

| Feature               | Description                                        |
| --------------------- | -------------------------------------------------- |
| 📄 PDF Resume Upload  | Upload your resume in PDF format                   |
| 🤖 AI Skill Detection | Automatically finds 80+ skills across 6 categories |
| 📊 ATS Score          | Gives your resume a score out of 100               |
| 🎯 Job Match %        | Compares your resume with any job description      |
| 💡 Smart Suggestions  | Tells you exactly how to improve your resume       |
| 📇 Contact Detection  | Finds your email and phone from the resume         |
| 🌙 Beautiful UI       | Modern dark-themed interface, works on mobile too  |

---

## 🖥️ How It Looks

```
┌─────────────────────────────────────┐
│         ResumeIQ Interface          │
│                                     │
│  [ Upload PDF Resume ]              │
│  [ Paste Job Description ]          │
│  [ 🔍 Analyze Resume Button ]       │
│                                     │
│  Results:                           │
│  ATS Score: 78/100 (Good)           │
│  Job Match: 65%                     │
│  Skills Found: 12                   │
│                                     │
│  Skills: Python, Flask, MongoDB...  │
│  Suggestions: Add cloud skills...   │
└─────────────────────────────────────┘
```

---

## 🚀 How to Run This Project (Complete Beginner Guide)

> **Don't know coding? No problem! Follow each step carefully.**

---

### 📥 Step 1 — Download & Install Python

Python is the programming language this project is built with. Think of it like installing an app to run the project.

1. Go to 👉 [https://www.python.org/downloads](https://www.python.org/downloads)
2. Click the big yellow **"Download Python"** button
3. Open the downloaded file
4. ⚠️ **IMPORTANT:** Check the box that says **"Add Python to PATH"** before clicking Install
5. Click **Install Now**
6. Wait for it to finish

**Verify it worked — open Command Prompt and type:**

```
python --version
```

You should see something like: `Python 3.12.0` ✅

---

### 📥 Step 2 — Download This Project

**Option A — Download ZIP (easiest):**

1. Click the green **"Code"** button on this GitHub page
2. Click **"Download ZIP"**
3. Extract the ZIP file to your Desktop

**Option B — Using Git:**

```bash
git clone https://github.com/kunal-sonawane/Resume-analyser.git
```

---

### 📂 Step 3 — Open the Project Folder

1. Open the extracted folder `Resume-analyser`
2. You should see these files inside:

```
Resume-analyser/
├── app.py
├── analyzer.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── main.js
```

---

### 💻 Step 4 — Open Command Prompt in This Folder

1. Open the `Resume-analyser` folder
2. Click on the address bar at the top of the folder
3. Type `cmd` and press Enter
4. A black Command Prompt window will open **inside your project folder**

---

### 📦 Step 5 — Install Required Packages

These are extra tools our project needs. Think of it like installing plugins.

Copy and paste this command and press Enter:

```
pip install flask==3.0.0 PyPDF2==3.0.1 scikit-learn numpy
```

Wait for it to finish. You'll see lots of text — that's normal! ✅

---

### ▶️ Step 6 — Run the Project

```
python app.py
```

You will see:

```
* Running on http://127.0.0.1:5000
```

---

### 🌐 Step 7 — Open in Browser

Open any browser (Chrome, Firefox, Edge) and go to:

```
http://127.0.0.1:5000
```

**🎉 ResumeIQ is now running on your computer!**

---

### 📄 Step 8 — Use the App

1. Click **"Browse File"** and select your resume (must be PDF)
2. Optionally paste a job description in the text box
3. Click **"🔍 Analyze Resume"**
4. Wait 2-3 seconds
5. See your results! 🎊

---

## 🛠️ Tech Stack (What Technologies We Used)

| Technology       | What is it?                | Why we used it?                           |
| ---------------- | -------------------------- | ----------------------------------------- |
| **Python**       | A programming language     | Main language of the project              |
| **Flask**        | A web framework for Python | To create the website and handle requests |
| **PyPDF2**       | A Python library           | To read and extract text from PDF files   |
| **scikit-learn** | A Machine Learning library | For TF-IDF and Cosine Similarity          |
| **NumPy**        | A math library for Python  | For numerical calculations                |
| **HTML/CSS/JS**  | Web technologies           | To build the user interface               |

---

## 🧠 AI/ML Concepts Used (Explained Simply)

### 1. 📄 PDF Text Extraction

> **Simple explanation:** When you upload a PDF, the computer needs to "read" it first. PyPDF2 opens your PDF like a book and converts all the text into a string (plain text) that Python can work with.

---

### 2. 🔍 Skill Extraction (Keyword Matching)

> **Simple explanation:** We have a list of 80+ skills (like Python, MySQL, Docker etc.). We check if any of these words appear in your resume text. If "python" is in your resume → we add it to your skill list. It's like a word search game!

**Categories we check:**

- Programming Languages (Python, Java, JavaScript...)
- Web Technologies (HTML, CSS, React, Flask...)
- Data Science & ML (TensorFlow, scikit-learn, NLP...)
- Databases (MySQL, MongoDB, PostgreSQL...)
- Cloud & DevOps (AWS, Docker, Git...)
- Soft Skills (Leadership, Communication, Teamwork...)

---

### 3. 📊 ATS Score (Resume Strength Score)

> **Simple explanation:** ATS stands for **Applicant Tracking System** — software companies use to filter resumes automatically. Our system calculates a score out of 100 based on:

| What we check                                               | Points |
| ----------------------------------------------------------- | ------ |
| Section keywords present (Skills, Experience, Education...) | 30 pts |
| Number of skills found                                      | 40 pts |
| Resume length (enough content?)                             | 15 pts |
| Contact info present (email, phone)                         | 15 pts |

**Score meaning:**

- 80-100 → Excellent 🌟
- 60-79 → Good ✅
- 40-59 → Average ⚠️
- 0-39 → Needs Improvement ❌

---

### 4. 🎯 Job Match — TF-IDF + Cosine Similarity

> **Simple explanation:** This is the most interesting AI part! Let us explain with an example:

**TF-IDF (Term Frequency — Inverse Document Frequency):**

- Imagine your resume has the word "Python" 5 times
- And the word "the" 20 times
- TF-IDF understands that "Python" is MORE important than "the" even though "the" appears more
- It converts both your resume and the job description into numbers (vectors)

**Cosine Similarity:**

- Once both resume and job description are converted to numbers
- We measure how "similar" they are — like measuring the angle between two arrows
- If they point in the same direction → high similarity = good match!
- Result: a percentage like 72% match

**Real world use:** This is exactly how Netflix recommends movies, how Google matches search results, and how LinkedIn matches jobs!

---

### 5. 💡 Smart Suggestions

> **Simple explanation:** Based on your ATS score, missing skills, and job match — our system generates personalized advice. Like: "Add cloud skills like AWS or Docker" or "Your resume doesn't match this job well, add more relevant keywords."

---

## 📁 Project Structure Explained

```
Resume-analyser/
│
├── app.py              → Main server file. Handles URL routes and file uploads
├── analyzer.py         → The AI brain. All the smart logic lives here
├── requirements.txt    → List of packages needed to run the project
│
├── templates/
│   └── index.html      → The webpage that users see (frontend)
│
└── static/
    ├── css/
    │   └── style.css   → Makes the webpage look beautiful
    └── js/
        └── main.js     → Handles button clicks, shows results on screen
```

---

## 🔄 How It Works — Step by Step Flow

```
User uploads PDF
      ↓
Flask receives the file (app.py)
      ↓
PyPDF2 extracts text from PDF (analyzer.py)
      ↓
Text is converted to lowercase
      ↓
┌─────────────────────────────────┐
│         Analysis Pipeline       │
│                                 │
│  1. Extract Skills              │
│  2. Calculate ATS Score         │
│  3. Calculate Job Match %       │
│  4. Generate Suggestions        │
│  5. Detect Contact Info         │
└─────────────────────────────────┘
      ↓
Results sent back as JSON
      ↓
JavaScript displays results on screen
      ↓
User sees their analysis! 🎉
```

---

## ⚠️ Common Issues & Fixes

| Problem                    | Solution                                                                    |
| -------------------------- | --------------------------------------------------------------------------- |
| `python is not recognized` | Python not added to PATH. Reinstall Python and check "Add to PATH"          |
| `pip is not recognized`    | Same as above — reinstall Python with PATH option                           |
| `No module named flask`    | Run `pip install flask` again                                               |
| `Only PDF files supported` | Make sure your resume is saved as .pdf not .doc                             |
| App opens but shows error  | Make sure your folder structure is correct (templates/ and static/ folders) |

---

## 👨‍💻 Project By

**Sakshi** — MCS Final Year Student

---

## 📄 License

This project is for educational purposes — Final Year MCS Project.

---

## 🌟 If this project helped you, give it a ⭐ on GitHub!
