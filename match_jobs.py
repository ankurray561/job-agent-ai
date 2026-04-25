import json


def filter_jobs(df):
    with open("cv_profile.json") as f:
        profile = json.load(f)
    
    # Normalize profile keywords to lowercase for consistent matching
    profile["target_roles"] = [role.lower() for role in profile["target_roles"]]
    profile["exclude_keywords"] = [word.lower() for word in profile["exclude_keywords"]]
    profile["must_have_keywords"] = [word.lower() for word in profile["must_have_keywords"]]
    profile["nice_to_have"] = [word.lower() for word in profile["nice_to_have"]]

    filtered_jobs = []

    for _, job in df.iterrows():
        title = str(job["title"]).lower()
        description = str(job["description"]).lower()
        text = title + " " + description

        # 🎯 STRICT ROLE FILTER
        if not any(role in title for role in profile["target_roles"]):
            continue

        # ❌ Reject unwanted roles
        if any(word in text for word in profile["exclude_keywords"]):
            continue

        score = 0

        # ✅ Must-have keywords
        for word in profile["must_have_keywords"]:
            if word in text:
                score += 2

        # ⭐ Nice-to-have
        for word in profile["nice_to_have"]:
            if word in text:
                score += 1

        # 🚀 Boost strong role match
        if "product manager" in text:
            score += 5

        if score >= 6:
            job["score"] = score
            filtered_jobs.append(job)

    return filtered_jobs