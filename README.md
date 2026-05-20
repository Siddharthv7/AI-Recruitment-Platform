# 🚀 AI Recruitment Platform

An AI-powered full-stack recruitment platform that analyzes resumes, extracts technical skills, calculates ATS/job match scores, identifies missing skills, and provides intelligent resume feedback.

This project helps recruiters and candidates quickly evaluate resume quality and job compatibility using Natural Language Processing (NLP) techniques.

---

# ✨ Features

## 🔐 Authentication System

* User Registration
* User Login
* Password Hashing
* Secure Authentication Flow

## 📄 Resume Analyzer

* Upload PDF resumes
* Extract resume text automatically
* Detect technical skills using NLP
* Generate ATS-style resume score

## 🤖 AI Resume Feedback

Provides intelligent suggestions like:

* Add measurable achievements
* Add GitHub profile link
* Add LinkedIn profile
* Add certifications
* Improve resume quality

## 🎯 Job Matching System

* Compare resume skills with job descriptions
* Calculate job match percentage
* Show matched skills
* Detect missing skills

## 🗄️ Database Integration

* Store resume details in PostgreSQL
* Save extracted skills and scores
* SQLAlchemy ORM integration

---

# 🛠️ Tech Stack

## Frontend

* React.js
* Vite
* CSS
* Axios

## Backend

* FastAPI
* Python
* SQLAlchemy
* PostgreSQL

## AI / NLP

* Scikit-learn
* NLP-based Skill Extraction
* Cosine Similarity
* CountVectorizer

---


## Dashboard

* Resume Upload
* ATS Score
* AI Resume Feedback
* Job Match Analysis

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Siddharthv7/AI-Recruitment-Platform.git
```

---

## 2️⃣ Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend runs on:

```bash
http://127.0.0.1:8000
```

---

## 3️⃣ Frontend Setup

```bash
cd frontend/ai-recruitment-frontend
npm install
npm run dev
```

Frontend runs on:

```bash
http://localhost:5173
```

---

# 🧠 AI Features Explained

## Resume Score

Calculates ATS-style score based on:

* Resume structure
* Skills detected
* Content quality
* Keyword matching

## Job Match Score

Uses NLP similarity matching between:

* Resume Skills
* Job Description

## Missing Skills Detection

Identifies skills present in the job description but missing in the resume.

---

# 📂 Project Structure

```bash
AI-Recruitment-Platform/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── auth.py
│   │   ├── hashing.py
│   │   ├── database.py
│   │   └── resume.py
│
├── frontend/
│   └── ai-recruitment-frontend/
│       ├── src/
│       ├── components/
│       ├── App.jsx
│       └── App.css
│
└── README.md
```

---

# 🔥 Future Improvements

* JWT Authentication
* Drag & Drop Resume Upload
* Resume PDF Preview
* OpenAI/Gemini Integration
* Download AI Feedback as PDF
* Admin Dashboard
* Multi-role Authentication
* Real ATS Scoring Engine
* Cloud Deployment

---

# 👨‍💻 Author

### Siddharth Vaishnav

Passionate Full Stack & AI Developer focused on building practical AI-powered applications.

GitHub:
[https://github.com/Siddharthv7](https://github.com/Siddharthv7)

---

# ⭐ Support

If you liked this project:

* Give this repository a ⭐
* Share with others
* Fork the repository

---

# 📜 License

This project is open-source and available for learning and educational purposes.
