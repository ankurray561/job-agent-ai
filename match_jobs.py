from parse_cv import extract_cv_text
import pandas as pd
import requests

def fetch_remotive():
    """Fetch jobs from Remotive and return a DataFrame with 'title' and 'description'."""
    url = "https://remotive.io/api/remote-jobs"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json().get("jobs", [])
        rows = [{"title": j.get("title", ""), "description": j.get("description", "")} for j in data]
        return pd.DataFrame(rows)
    except Exception:
        return pd.DataFrame(columns=["title", "description"])


def fetch_arbeitnow():
    """Fetch jobs from Arbeitnow and return a DataFrame with 'title' and 'description'."""
    url = "https://www.arbeitnow.com/api/job-board-api"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json().get("data", [])
        rows = [{"title": j.get("title", ""), "description": j.get("description", "")} for j in data]
        return pd.DataFrame(rows)
    except Exception:
        return pd.DataFrame(columns=["title", "description"])


def filter_jobs(df):
    import json

    with open("cv_profile.json") as f:
        profile = json.load(f)

    filtered_jobs = []

    for _, job in df.iterrows():
        text = (str(job["title"]) + " " + str(job["description"])).lower()

        score = 0

        # ❌ Hard reject
        if any(word in text for word in profile["exclude_keywords"]):
            continue

        # ✅ Must-have scoring
        for word in profile["must_have_keywords"]:
            if word in text:
                score += 2

        # ⭐ Bonus scoring
        for word in profile["nice_to_have"]:
            if word in text:
                score += 1

        # 🎯 Role alignment boost
        if any(role.lower() in text for role in profile["target_roles"]):
            score += 5

        if score >= 5:
            job["score"] = score
            filtered_jobs.append(job)

        # HARD FILTER → only Product roles
        if "product" not in job["title"].lower():
            continue
        score = 0
        text = (job["title"] + job["description"]).lower()

        # Strong signals
        if "product manager" in text:
            score += 10

        if "ai" in text or "machine learning" in text:
            score += 3

        if "growth" in text or "strategy" in text:
            score += 2

        # Reject junk
        if any(x in text for x in ["support", "sales", "designer", "recruiter"]):
            continue

        if score >= 8:
            job["score"] = score
            filtered_jobs.append(job)

        df1 = fetch_remotive()
        df2 = fetch_arbeitnow()

        df = pd.concat([df1, df2])

    return filtered_jobs