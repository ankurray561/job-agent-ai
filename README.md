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

## 🏗️ Detailed Data Flow Diagram (DFD)

```mermaid
flowchart TD
    %% External Entities
    EE1[External Entity<br/>Job APIs<br/>(Remotive, Arbeitnow)]
    EE2[External Entity<br/>User Email<br/>(Gmail SMTP)]
    EE3[External Entity<br/>User CV<br/>(PDF File)]

    %% Processes
    P1[Process 1<br/>Fetch Jobs<br/>fetch_jobs.py]
    P2[Process 2<br/>Filter Jobs<br/>match_jobs.py]
    P3[Process 3<br/>Send Email<br/>send_email.py]
    P4[Process 4<br/>Parse CV<br/>parse_cv.py<br/>(Optional)]

    %% Data Stores
    DS1[Data Store<br/>CV Profile<br/>cv_profile.json]
    DS2[Data Store<br/>Job Data<br/>Pandas DataFrame<br/>(In Memory)]
    DS3[Data Store<br/>Filtered Jobs<br/>List of Dicts<br/>(In Memory)]
    DS4[Data Store<br/>Parsed CV Text<br/>String<br/>(In Memory)]

    %% Data Flows
    EE1 -->|HTTP GET Requests| P1
    P1 -->|Job Listings JSON| DS2
    DS2 -->|Job Data| P2
    DS1 -->|Profile Keywords| P2
    P2 -->|Filtered Jobs| DS3
    DS3 -->|Job Matches| P3
    P3 -->|SMTP Email| EE2
    EE3 -->|PDF File| P4
    P4 -->|Extracted Text| DS4
    DS4 -->|CV Text| DS1

    %% Main Orchestrator
    M[Main Process<br/>main.py<br/>Orchestrates P1-P3]
    M -.->|Calls| P1
    M -.->|Calls| P2
    M -.->|Calls| P3
```

### DFD Level 0 Explanation
- **External Entities**: Represent sources/sinks outside the system
  - Job APIs: Provide job data via REST APIs
  - User Email: Receives notifications via SMTP
  - User CV: Source for profile keywords (currently manual JSON, PDF parsing available)
- **Processes**: Core business logic functions
- **Data Stores**: Persistent or temporary data storage
- **Data Flows**: Movement of data between components

## 🏛️ Architectural Components Breakdown

### 1. Main Orchestrator (`main.py`)
**Purpose**: Entry point that coordinates the entire job matching workflow.

**Key Responsibilities**:
- Initialize the automation sequence
- Handle high-level error catching and logging
- Ensure sequential execution: Fetch → Filter → Send
- Provide user feedback via console output

**Technical Details**:
- Simple procedural script with try-except block
- No dependencies on external libraries beyond standard Python
- Execution time: ~10-30 seconds depending on API response times
- Memory usage: Minimal, as data is processed in streams

**Inputs**: None (reads configuration files)
**Outputs**: Console logs, triggers email if matches found

### 2. Job Fetching Module (`fetch_jobs.py`)
**Purpose**: Aggregate job listings from multiple remote job platforms.

**Key Responsibilities**:
- Make HTTP requests to job APIs with timeout handling
- Parse JSON responses into structured data
- Normalize job data across different API schemas
- Handle API failures gracefully (continues with other sources)

**Technical Details**:
- Uses `requests` library for HTTP calls (timeout: 10s)
- Data transformation with `pandas` DataFrame
- APIs integrated:
  - Remotive: `https://remotive.com/api/remote-jobs`
  - Arbeitnow: `https://www.arbeitnow.com/api/job-board-api`
- Error handling: Try-catch per API, prints errors but continues
- Data structure: Dict with keys: title, company, location, description, url

**Inputs**: None (API endpoints hardcoded)
**Outputs**: Pandas DataFrame with job listings

### 3. Job Matching Engine (`match_jobs.py`)
**Purpose**: Intelligently filter and score jobs based on user profile.

**Key Responsibilities**:
- Load user preferences from JSON configuration
- Apply strict role-based filtering
- Implement keyword matching with weighted scoring
- Exclude irrelevant positions

**Technical Details**:
- Scoring algorithm:
  - Must-have keywords: +2 points each
  - Nice-to-have keywords: +1 point each
  - Product Manager role boost: +5 points
  - Minimum threshold: 6 points
- Filtering logic:
  - Role filter: Must contain target roles in title
  - Exclusion filter: Skip if contains exclude keywords
- Configuration loaded from `cv_profile.json`
- Processes DataFrame row-by-row for memory efficiency

**Inputs**: Job DataFrame, CV Profile JSON
**Outputs**: List of matching job dictionaries with scores

### 4. Email Notification Service (`send_email.py`)
**Purpose**: Deliver curated job matches via professional HTML email.

**Key Responsibilities**:
- Generate responsive HTML email template
- Authenticate with Gmail SMTP server
- Send formatted job listings with apply links
- Include match scores for prioritization

**Technical Details**:
- Uses `smtplib` for SMTP communication
- HTML template with inline CSS for cross-client compatibility
- Authentication: Gmail App Password required
- Email structure: Subject, HTML body with job cards
- Security: TLS encryption enabled

**Inputs**: List of matched jobs
**Outputs**: Email sent to configured recipient

### 5. CV Parsing Utility (`parse_cv.py`)
**Purpose**: Extract text content from PDF CV files for automated profile generation.

**Key Responsibilities**:
- Read PDF files using PyPDF2
- Extract raw text from all pages
- Normalize text to lowercase for processing

**Technical Details**:
- Uses `PyPDF2.PdfReader` for PDF parsing
- Concatenates text from all pages
- Currently not integrated into main workflow
- File hardcoded: "ANKUR_RAY_CV_2026.pdf"

**Inputs**: PDF file path
**Outputs**: Lowercase text string

### 6. Configuration Store (`cv_profile.json`)
**Purpose**: User-defined preferences for job matching criteria.

**Structure**:
- `target_roles`: List of desired job titles (strict match required)
- `must_have_keywords`: Essential skills/terms (+2 score)
- `nice_to_have`: Bonus skills/terms (+1 score)
- `exclude_keywords`: Positions to avoid entirely

**Technical Details**:
- JSON format for easy editing
- Loaded once per execution
- No validation currently implemented
- Human-readable and modifiable without code changes

## 🔄 System Workflow Sequence

1. **Initialization** (`main.py`)
   - Print startup message
   - Call `fetch_jobs()`

2. **Data Acquisition** (`fetch_jobs.py`)
   - Request jobs from Remotive API
   - Request jobs from Arbeitnow API
   - Combine into DataFrame
   - Return to main

3. **Intelligent Filtering** (`match_jobs.py`)
   - Load profile from JSON
   - Iterate through jobs:
     - Check role match
     - Check exclusions
     - Calculate score
     - Filter if score ≥ 6
   - Return matched jobs

4. **Notification Delivery** (`send_email.py`)
   - Build HTML email with job cards
   - Connect to Gmail SMTP
   - Send email
   - Close connection

5. **Completion** (`main.py`)
   - Print success message
   - Exit

## 🛡️ Error Handling & Resilience

- **API Failures**: Individual API errors don't stop execution
- **Network Timeouts**: 10-second timeouts prevent hanging
- **Authentication Errors**: Clear error messages for email setup
- **Data Parsing**: Try-catch blocks around JSON parsing
- **Empty Results**: Graceful handling when no jobs match

## 📈 Performance Characteristics

- **Execution Time**: 10-30 seconds (API dependent)
- **Memory Usage**: ~50-200MB (depends on job volume)
- **Network Requests**: 2-3 HTTP calls per run
- **CPU Usage**: Minimal (string matching, no heavy computation)
- **Scalability**: Linear with job volume, suitable for daily runs

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
