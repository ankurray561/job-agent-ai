import requests
import pandas as pd

def fetch_jobs():
    url = "https://remotive.com/api/remote-jobs"
    response = requests.get(url)
    data = response.json()

    jobs = []

    for job in data.get("jobs", []):
        jobs.append({
            "title": job.get("title"),
            "company": job.get("company_name"),
            "location": job.get("candidate_required_location"),
            "description": job.get("description"),
            "url": job.get("url")
        })

    df = pd.DataFrame(jobs)
    print(f"Total jobs fetched: {len(df)}")
    return df