import re

EMAIL_PATTERN = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

JOB_ROLES = [
    "Java Developer",
    "Python Developer",
    "Frontend Developer",
    "Backend Developer",
    "Full Stack Developer",
    "React Developer",
    "Node.js Developer",
    "Data Scientist",
    "Machine Learning Engineer",
    "DevOps Engineer",
    "QA Engineer",
    "Software Engineer"
]

JOB_TYPES = [
    "Contract",
    "Full-Time",
    "Full Time",
    "C2C",
    "Corp-to-Corp",
    "W2",
    "1099",
    "Internship",
    "Remote",
    "Hybrid",
    "Onsite"
]
SKILLS = [
    "Python",
    "Java",
    "JavaScript",
    "TypeScript",
    "React",
    "Angular",
    "Vue",
    "Node.js",
    "Express",
    "Spring Boot",
    "Django",
    "Flask",
    "FastAPI",
    "AWS",
    "Azure",
    "GCP",
    "Docker",
    "Kubernetes",
    "Kafka",
    "Redis",
    "MongoDB",
    "MySQL",
    "PostgreSQL",
    "SQL",
    "Git",
    "Linux",
    "HTML",
    "CSS",
    ]


LOCATION_PATTERN = r"Location\s*:\s*([A-Za-z\s]+,\s*[A-Z]{2})"


def extract_email(text: str):
    return re.findall(EMAIL_PATTERN, text)


def extract_role(text: str):
    text_lower = text.lower()

    for role in JOB_ROLES:
        if role.lower() in text_lower:
            return role

    return "Unknown"


def extract_job_type(text: str):
    text_lower = text.lower()

    for job_type in JOB_TYPES:
        if job_type.lower() in text_lower:
            return job_type

    return "Unknown"


def extract_location(text: str):
    match = re.search(LOCATION_PATTERN, text, re.IGNORECASE)

    if match:
        return match.group(1).strip()

    return "Unknown"

def extract_skills(text: str):
    """
    Extract technical skills from the text.
    """
    text_lower = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return sorted(set(found_skills))