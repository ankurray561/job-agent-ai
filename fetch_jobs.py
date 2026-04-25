import requests
import pandas as pd


def fetch_jobs():
    jobs = []

    # 🔹 Source 1: Remotive
    try:
        url = "https://remotive.com/api/remote-jobs"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        for job in data.get("jobs", []):
            jobs.append({
                "title": job.get("title", ""),
                "company": job.get("company_name", ""),
                "location": job.get("candidate_required_location", ""),
                "description": job.get("description", ""),
                "url": job.get("url", "")
            })
    except Exception as e:
        print("Error fetching Remotive:", e)

    # 🔹 Source 2: Arbeitnow
    try:
        url = "https://www.arbeitnow.com/api/job-board-api"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        for job in data.get("data", []):
            jobs.append({
                "title": job.get("title", ""),
                "company": job.get("company_name", ""),
                "location": job.get("location", ""),
                "description": job.get("description", ""),
                "url": job.get("url", "")
            })
    except Exception as e:
        print("Error fetching Arbeitnow:", e)

    df = pd.DataFrame(jobs)
    print(f"Total jobs fetched: {len(df)}")

    return df