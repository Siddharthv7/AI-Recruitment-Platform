from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi import File, UploadFile
import shutil
import os
import pdfplumber


from app.schemas import UserLogin
from app.hashing import verify_password
from app.auth import create_access_token, verify_token
from app.database import engine, SessionLocal
from app.models import Base, User
from app import models
from app.schemas import UserCreate
from app.hashing import hash_password, verify_password
from app.models import User
from fastapi import HTTPException
from app.database import SessionLocal
from app.models import Resume
from app.resume import calculate_resume_score
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

db = SessionLocal()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SKILLS_DB = [
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "React",
    "Node.js",
    "FastAPI",
    "Django",
    "SQL",
    "MongoDB",
    "AWS",
    "Docker",
    "Machine Learning",
    "AI",
    "Deep Learning",
    "TensorFlow",
    "PyTorch",
    "Git",
    "HTML",
    "CSS",
    "Kubernetes",
    "Terraform",
    "Linux",
    "DevOps",
    "Machine Learning",
    "Deep Learning",
    "CI/CD",
    "Redis",
    "GraphQL",
    "TypeScript"
]

# Database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "AI Recruitment Platform Backend Running"}


@app.post("/register")
async def register(data: dict):

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    existing_user = db.query(User).filter(
        User.email == email
    ).first()

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    hashed_password = hash_password(password)

    new_user = User(
        username=username,
        email=email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User Registered Successfully"
    }
    
@app.post("/login")
async def login(data: dict):

    email = data.get("email")
    password = data.get("password")

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        raise HTTPException(
            status_code=400,
            detail="Invalid Email"
        )

    if not verify_password(password, user.password):
        raise HTTPException(
            status_code=400,
            detail="Invalid Password"
        )

    return {
        "message": "Login Successful",
        "user": {
            "username": user.username,
            "email": user.email
        }
    }
    
@app.get("/profile")
def profile(current_user: str = Depends(verify_token)):

    return {
        "message": "Protected Route Accessed",
        "user": current_user
    }

@app.post("/upload-resume")
def upload_resume(file: UploadFile = File(...)):

    upload_folder = "resumes"

    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    file_path = f"{upload_folder}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "Resume Uploaded Successfully",
        "filename": file.filename
    }
    
@app.post("/extract-resume")
def extract_resume(file: UploadFile = File(...)):

    text = ""

    with pdfplumber.open(file.file) as pdf:

        for page in pdf.pages:
            text += page.extract_text()

    return {
        "resume_text": text
    }

@app.post("/save-resume")
async def save_resume(data: dict):

    new_resume = Resume(
        filename=data.get("filename"),
        skills=", ".join(data.get("skills")),
        resume_score=data.get("resume_score")
    )

    db.add(new_resume)

    db.commit()

    db.refresh(new_resume)

    return {
        "message": "Resume Saved Successfully"
    }
        
@app.post("/extract-skills")
def extract_skills(file: UploadFile = File(...)):

    text = ""

    with pdfplumber.open(file.file) as pdf:

        for page in pdf.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted

    found_skills = []

    for skill in SKILLS_DB:

        if skill.lower() in text.lower():
            found_skills.append(skill)
            
    resume_score = len(found_skills) * 5

    if resume_score > 100:
        resume_score = 100
        
    ai_feedback = []

    if resume_score < 90:
        ai_feedback.append("Add more measurable achievements")

    if "github" not in text.lower():
        ai_feedback.append("Add GitHub profile link")

    if "linkedin" not in text.lower():
        ai_feedback.append("Add LinkedIn profile")

    if "certification" not in text.lower():
        ai_feedback.append("Add certifications")

    return {
        "skills": found_skills,
        "resume_score": resume_score,
        "ai_feedback": ai_feedback
    }
    
@app.post("/resume-score")
def resume_score(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    text = ""

    with pdfplumber.open(file.file) as pdf:

        for page in pdf.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted

    job_description = "Python FastAPI React PostgreSQL AI ML"

    score = calculate_resume_score(
        text,
        job_description
    )

    feedback = ["AI Resume Matching Completed"]

    ai_feedback = []

    if "github.com" not in text.lower():
        ai_feedback.append("Add GitHub project links")

    if "linkedin.com" not in text.lower():
        ai_feedback.append("Add LinkedIn profile")

    if "certification" not in text.lower():
        ai_feedback.append("Add certifications")

    if "%" not in text:
        ai_feedback.append("Add measurable achievements with percentages")

    if "project" not in text.lower():
        ai_feedback.append("Add strong projects section")

    if len(text.split()) < 300:
        ai_feedback.append("Resume content is too short")

    new_resume = models.Resume(
        filename=file.filename,
        skills=", ".join(feedback),
        resume_score=score,
        user_email="workinguser@gmail.com"
    )

    db.add(new_resume)
    db.commit()

    return {
        "resume_score": score,
        "feedback": feedback,
        "ai_feedback": ai_feedback
    }
    
@app.get("/all-resumes")
def all_resumes(db: Session = Depends(get_db)):

    resumes = db.query(models.Resume).all()

    return resumes


@app.get("/top-resumes")
def top_resumes(db: Session = Depends(get_db)):

    resumes = db.query(models.Resume).order_by(
        models.Resume.resume_score.desc()
    ).all()

    return resumes


@app.get("/search-skill/{skill}")
def search_skill(skill: str, db: Session = Depends(get_db)):

    resumes = db.query(models.Resume).filter(
        models.Resume.skills.ilike(f"%{skill}%")
    ).all()

    return resumes


@app.get("/resume/{resume_id}")
def get_resume(resume_id: int, db: Session = Depends(get_db)):

    resume = db.query(models.Resume).filter(
        models.Resume.id == resume_id
    ).first()

    if not resume:
        return {"error": "Resume not found"}

    return resume


@app.delete("/delete-resume/{resume_id}")
def delete_resume(resume_id: int, db: Session = Depends(get_db)):

    resume = db.query(models.Resume).filter(
        models.Resume.id == resume_id
    ).first()

    if not resume:
        return {"error": "Resume not found"}

    db.delete(resume)
    db.commit()

    return {
        "message": "Resume Deleted Successfully"
    }
    
@app.post("/match-job")
def match_job(data: dict):

    resume_skills = data.get("resume_skills")
    job_description = data.get("job_description")

    jd_words = job_description.lower().split()

    matched_skills = []
    missing_skills = []

    for skill in resume_skills:

        if skill.lower() in jd_words:
            matched_skills.append(skill)

    for word in jd_words:

        for skill in SKILLS_DB:

            if skill.lower() == word and skill not in matched_skills:
                missing_skills.append(skill)

    match_score = round(
        (len(matched_skills) / len(resume_skills)) * 100
    )

    return {
        "match_score": match_score,
        "matched_skills": matched_skills,
        "missing_skills": list(set(missing_skills))
    }