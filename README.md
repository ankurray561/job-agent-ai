# Job Automation 🚀

A Python-based automation system that fetches remote job postings, intelligently filters them based on your CV profile, and sends curated job matches to your email.

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    Main Orchestrator                        │
│                    (main.py)                               │
└────────┬─────────────────┬──────────────────┬──────────────┘
         │                 │                  │
    ┌────▼───┐      ┌──────▼──────┐    ┌─────▼────┐
    │ Fetch  │      │   Filter    │    │  Send    │
    │  Jobs  │      │    Jobs     │    │  Email   │
    │        │      │             │    │          │
    └────┬───┘      └──────┬──────┘    └─────┬────┘
         │                 │                  │
    ┌────▼──────────┐  ┌────▼────────┐      │
    │  Job APIs     │  │ CV Profile  │      │
    │               │  │  (JSON)     │      │
    │ • Remotive    │  └─────────────┘      │
    │ • Arbeitnow   │                       │
    └────────────────┘               ┌──────▼─────┐
                                     │ SMTP Gmail │
                                     └────────────┘
```

## 📁 Project Structure

```
job-automation/
├── main.py                          # 🎯 Entry point - Orchestrates the entire workflow
├── fetch_jobs.py                    # 📥 Fetches jobs from multiple remote job APIs
├── match_jobs.py                    # 🔍 Filters jobs based on CV profile and scoring
├── send_email.py                    # 📤 Sends matched jobs via email
├── parse_cv.py                      # 📄 Extracts text from CV PDF (optional)
├── cv_profile.json                  # ⚙️ User preferences & keywords configuration
├── ANKUR_RAY_CV_2026.pdf           # 📋 CV file
└── README.md                        # 📖 This file
```

## 🔄 Workflow

1. **Fetch Jobs** (`fetch_jobs.py`)
   - Calls multiple job board APIs:
     - **Remotive**: `https://remotive.com/api/remote-jobs`
     - **Arbeitnow**: `https://www.arbeitnow.com/api/job-board-api`
   - Returns a pandas DataFrame with job listings
   - Handles errors gracefully with try-catch blocks

2. **Filter Jobs** (`match_jobs.py`)
   - Reads user preferences from `cv_profile.json`
   - Applies strict role filtering
   - Excludes unwanted keywords
   - Scores jobs based on:
     - Must-have keywords (weight: 2 points each)
     - Nice-to-have keywords (weight: 1 point each)
     - Role boost (Product Manager: +5 points)
   - Returns only jobs with score ≥ 6

3. **Send Email** (`send_email.py`)
   - Generates formatted HTML email
   - Sends via Gmail SMTP
   - Includes job title, company, match score, and apply link
   - Requires Gmail App Password for authentication

## ⚙️ Configuration

### `cv_profile.json`
Define your job preferences:
```json
{
  "target_roles": ["product manager", "pm", "product lead"],
  "must_have_keywords": ["python", "data", "analytics"],
  "nice_to_have": ["machine learning", "ai", "sql"],
  "exclude_keywords": ["junior", "unpaid", "internship"]
}
```

### Email Configuration (`send_email.py`)
Update these values:
- `msg["From"]`: Your Gmail address (sender)
- `msg["To"]`: Recipient email address
- `server.login("email_A", "YOUR_APP_PASSWORD")`: Use Gmail App Password

## 🚀 Getting Started

### Prerequisites
```bash
pip install requests pandas PyPDF2
```

### Run the Script
```bash
python main.py
```

### Output
```
🚀 Script started...
📥 Fetching jobs...
🔍 Filtering jobs...
✅ Jobs matched: 5
📤 Sending email...
🎉 Done!
```

## 🔒 Security Notes

- **Never commit credentials** to git
- Use Gmail App Password (not your main password)
- Add sensitive files to `.gitignore`

## 📊 Data Flow

1. **API Calls** → Job listings fetched as JSON
2. **Transformation** → Converted to pandas DataFrame
3. **Filtering** → Keyword matching & scoring algorithm
4. **Delivery** → HTML formatted email via SMTP

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.x |
| HTTP Requests | `requests` |
| Data Processing | `pandas` |
| PDF Processing | `PyPDF2` |
| Email | `smtplib` + `email.mime` |
| Configuration | JSON |

## ✨ Features

- ✅ Multi-source job aggregation
- ✅ Smart keyword matching & scoring
- ✅ Beautiful HTML email formatting
- ✅ Error handling & logging
- ✅ Configurable preferences
- ✅ PDF CV parsing capability

## 🚧 Future Enhancements

- [ ] Schedule jobs with cron/APScheduler
- [ ] Database integration for job tracking
- [ ] Duplicate detection across APIs
- [ ] Machine learning-based job matching
- [ ] Telegram/Slack notifications
- [ ] Web UI for configuration

## 📝 License

Personal Project

---

**Created by**: Automation System  
**Last Updated**: 2026
