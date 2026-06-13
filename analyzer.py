import PyPDF2
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# ─── Skill Database ───────────────────────────────────────────────────────────
SKILLS_DB = {
    "Programming Languages": [
        "python", "java", "javascript", "c++", "c#", "ruby", "swift", "kotlin",
        "typescript", "php", "r", "scala", "go", "rust", "matlab"
    ],
    "Web Technologies": [
        "html", "css", "react", "angular", "vue", "node.js", "django", "flask",
        "express", "bootstrap", "tailwind", "jquery", "rest api", "graphql"
    ],
    "Data Science & ML": [
        "machine learning", "deep learning", "nlp", "computer vision",
        "tensorflow", "pytorch", "keras", "scikit-learn", "pandas", "numpy",
        "matplotlib", "seaborn", "opencv", "transformers", "bert", "gpt"
    ],
    "Databases": [
        "mysql", "postgresql", "mongodb", "sqlite", "redis", "firebase",
        "oracle", "sql", "nosql", "elasticsearch"
    ],
    "Cloud & DevOps": [
        "aws", "azure", "google cloud", "docker", "kubernetes", "git",
        "github", "ci/cd", "jenkins", "linux", "bash"
    ],
    "Soft Skills": [
        "leadership", "communication", "teamwork", "problem solving",
        "critical thinking", "time management", "project management", "agile", "scrum"
    ]
}

# ─── ATS Keywords ─────────────────────────────────────────────────────────────
ATS_KEYWORDS = [
    "experience", "education", "skills", "projects", "achievements",
    "certifications", "summary", "objective", "responsibilities", "accomplishments"
]


def extract_text_from_pdf(filepath):
    """Extract raw text from PDF file."""
    text = ""
    with open(filepath, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text.lower()


def extract_contact_info(text):
    """Extract email and phone from resume text."""
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    phone_pattern = r'(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'

    emails = re.findall(email_pattern, text, re.IGNORECASE)
    phones = re.findall(phone_pattern, text)

    return {
        "email": emails[0] if emails else "Not found",
        "phone": phones[0] if phones else "Not found"
    }


def extract_skills(text):
    """Match resume text against skill database."""
    found_skills = {}
    for category, skills in SKILLS_DB.items():
        matched = [skill for skill in skills if skill in text]
        if matched:
            found_skills[category] = matched
    return found_skills


def calculate_ats_score(text, skills_found):
    """Calculate ATS compatibility score out of 100."""
    score = 0

    # 1. Section keywords present (30 points)
    sections_found = sum(1 for kw in ATS_KEYWORDS if kw in text)
    score += min(30, sections_found * 5)

    # 2. Total skills found (40 points)
    total_skills = sum(len(v) for v in skills_found.values())
    score += min(40, total_skills * 2)

    # 3. Resume length — enough content? (15 points)
    word_count = len(text.split())
    if word_count > 300:
        score += 15
    elif word_count > 150:
        score += 8

    # 4. Contact info present (15 points)
    if "@" in text:
        score += 8
    if any(char.isdigit() for char in text):
        score += 7

    return min(100, score)


def calculate_job_match(resume_text, job_description):
    """Use TF-IDF + Cosine Similarity for job matching."""
    if not job_description.strip():
        return 0, []

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([resume_text, job_description])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    match_percent = round(similarity * 100, 2)

    # Find matching keywords
    job_words = set(job_description.lower().split())
    resume_words = set(resume_text.lower().split())
    common = job_words.intersection(resume_words)
    important_matches = [w for w in common if len(w) > 4][:10]

    return match_percent, important_matches


def generate_suggestions(skills_found, ats_score, job_match):
    """Generate improvement suggestions based on analysis."""
    suggestions = []

    if ats_score < 50:
        suggestions.append("⚠️ Add clear section headings: Summary, Skills, Experience, Education, Projects.")
    if ats_score < 70:
        suggestions.append("📌 Include more measurable achievements (e.g., 'Improved performance by 30%').")

    if "Data Science & ML" not in skills_found:
        suggestions.append("🤖 Consider adding ML/AI skills like TensorFlow, scikit-learn, or PyTorch.")
    if "Cloud & DevOps" not in skills_found:
        suggestions.append("☁️ Add cloud skills (AWS, Docker, Git) — highly demanded in industry.")
    if "Databases" not in skills_found:
        suggestions.append("🗄️ Mention database experience: MySQL, MongoDB, or PostgreSQL.")

    if job_match < 40 and job_match > 0:
        suggestions.append("🎯 Your resume doesn't closely match the job description. Tailor keywords.")
    elif job_match >= 40:
        suggestions.append("✅ Good job match! Make sure your experience section reflects the JD closely.")

    if not suggestions:
        suggestions.append("🌟 Your resume looks strong! Keep it updated with new projects and skills.")

    return suggestions


def get_skill_gaps(skills_found):
    """Identify missing skill categories."""
    all_categories = list(SKILLS_DB.keys())
    found_categories = list(skills_found.keys())
    gaps = [cat for cat in all_categories if cat not in found_categories]
    return gaps


def analyze_resume(filepath, job_description=""):
    """Main function — orchestrates the full analysis."""
    # Step 1: Extract text
    text = extract_text_from_pdf(filepath)

    # Step 2: Run all analyses
    contact_info = extract_contact_info(text)
    skills_found = extract_skills(text)
    ats_score = calculate_ats_score(text, skills_found)
    job_match, matched_keywords = calculate_job_match(text, job_description)
    suggestions = generate_suggestions(skills_found, ats_score, job_match)
    skill_gaps = get_skill_gaps(skills_found)

    # Step 3: Determine ATS level
    if ats_score >= 80:
        ats_level = "Excellent"
    elif ats_score >= 60:
        ats_level = "Good"
    elif ats_score >= 40:
        ats_level = "Average"
    else:
        ats_level = "Needs Improvement"

    return {
        "contact_info": contact_info,
        "skills_found": skills_found,
        "ats_score": ats_score,
        "ats_level": ats_level,
        "job_match_percent": job_match,
        "matched_keywords": matched_keywords,
        "suggestions": suggestions,
        "skill_gaps": skill_gaps,
        "total_skills_count": sum(len(v) for v in skills_found.values())
    }
