from pathlib import Path

from services.parser import analyze_posts
from services.exporter import save_jobs_to_csv

POST_FILE = Path("data/posts.txt")


def read_post(file_path: Path) -> str:
    """Read the input text file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def main():
    text = read_post(POST_FILE)

    jobs = analyze_posts(text)

    print("=" * 60)
    print("RECRUITER POST ANALYZER")
    print("=" * 60)

    for i, job in enumerate(jobs, start=1):
        print(f"\nJob #{i}")
        print("-" * 30)
        print(f"Role      : {job.role}")
        print(f"Job Type  : {job.job_type}")
        print(f"Location  : {job.location}")
        print(f"Country   : {job.country}")
        print(f"Spam      : {'Yes' if job.spam else 'No'}")
        print(f"Emails    : {', '.join(job.emails) if job.emails else 'None'}")

    save_jobs_to_csv(jobs)

    print("\n✅ CSV exported successfully!")


if __name__ == "__main__":
    main()