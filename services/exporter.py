import csv
from pathlib import Path

from config import OUTPUT_FILE

OUTPUT_FILE = Path(OUTPUT_FILE)


def save_jobs_to_csv(jobs):

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Role",
            "Job Type",
            "Location",
            "Country",
            "Spam",
            "Emails",
        ])

        for job in jobs:

            writer.writerow([
                job.role,
                job.job_type,
                job.location,
                job.country,
                "Yes" if job.spam else "No",
                ", ".join(job.emails),
            ])