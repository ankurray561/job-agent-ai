print("🚀 Script started...")

from fetch_jobs import fetch_jobs
from match_jobs import filter_jobs
from send_email import send_email


def run():
    try:
        print("📥 Fetching jobs...")
        df = fetch_jobs()

        print("🔍 Filtering jobs...")
        jobs = filter_jobs(df)

        print(f"✅ Jobs matched: {len(jobs)}")

        if len(jobs) == 0:
            print("⚠️ No relevant jobs found. Skipping email.")
            return

        print("📤 Sending email...")
        send_email(jobs)

        print("🎉 Done!")

    except Exception as e:
        print("❌ Error occurred:", e)


if __name__ == "__main__":
    run()