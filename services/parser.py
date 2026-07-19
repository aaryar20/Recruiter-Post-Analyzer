from services.extractor import (
    extract_email,
    extract_role,
    extract_job_type,
    extract_location,
    extract_skills,
)

from services.filters import (
    detect_country,
    is_spam,
)

from models.job_post import JobPost
from config import POST_SEPARATOR


def analyze_posts(text: str):
    """Split the input into multiple posts and extract data."""

    jobs = []

    posts = text.split(POST_SEPARATOR)

    for post in posts:

        post = post.strip()

        if not post:
            continue

        location = extract_location(post)

        job = JobPost(
            role=extract_role(post),
            job_type=extract_job_type(post),
            location=location,
            emails=extract_email(post),
            country=detect_country(location),
            spam=is_spam(post),
            skills=extract_skills(post),
        )

        jobs.append(job)

    return jobs