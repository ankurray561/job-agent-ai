**Built as a personal solution to eliminate noise in job discovery and improve application efficiency.**

✨ 1. Header
# 🚀 AI-Powered Job Matching Agent

An intelligent job discovery system that fetches global remote jobs and filters them based on a personalized CV-driven scoring engine.

Built to solve the problem of **irrelevant job recommendations** by aligning opportunities with candidate intent, skills, and role preferences.
🎯 2. Problem Statement
## ❌ Problem

Most job platforms:

* Show generic listings
* Lack personalization
* Require manual filtering

This leads to:

* Time waste
* Low-quality applications
* Poor job-candidate fit

---

## ✅ Solution

This system:

* Fetches **global remote jobs**
* Parses user CV profile
* Applies **rule-based + scoring engine**
* Sends **highly relevant job matches via email**

⚙️ 3. System Architecture
<img width="611" height="521" alt="image" src="https://github.com/user-attachments/assets/56ca845d-5cfb-4db5-80bf-dcb20d916b1c" /><img width="859" height="321" alt="image" src="https://github.com/user-attachments/assets/0c4880eb-68fb-4400-bfe8-dda3e7797f9a" />
<img width="759" height="456" alt="image" src="https://github.com/user-attachments/assets/bffdc3f1-76b4-48c7-be6c-96b03a551792" />
<img width="2320" height="1507" alt="image" src="https://github.com/user-attachments/assets/f54b22bd-fa34-422a-95e1-b8cdfec46811" />
<img width="801" height="401" alt="image" src="https://github.com/user-attachments/assets/e7bb70b4-6727-469c-a39a-2b0ac7339ee6" />
<img width="810" height="331" alt="image" src="https://github.com/user-attachments/assets/fc28cc09-8f35-4271-8774-8910bd33a98f" />
### 🧩 Components

1. **Data Ingestion Layer**

   * Fetch jobs from APIs (Remotive)

2. **Processing Layer**

   * CV-based keyword matching
   * Scoring engine

3. **Filtering Engine**

   * Hard filters (role-based)
   * Soft scoring (keywords, AI, growth)

4. **Output Layer**

   * HTML email generator
   * Personalized job recommendations

---

### 🔄 Data Flow

CV → Profile JSON → Job Fetch → Text Matching → Scoring → Filter → Email Output

🧱 4. Tech Stack
## 🛠 Tech Stack

* **Language:** Python

* **Libraries:**

  * `requests` → API calls
  * `pandas` → data processing
  * `smtplib` → email automation
  * `PyPDF2` → CV parsing

* **APIs:**

  * Remotive Jobs API

* **Output:**

  * HTML Email UI

* **Version Control:**

  * Git + GitHub

🧪 5. How It Works (Step-by-Step)
## 🔍 Workflow

### Step 1: Fetch Jobs

* Calls Remotive API
* Converts response → DataFrame

### Step 2: Load Profile

* Reads `cv_profile.json`
* Defines:

  * target roles
  * must-have skills
  * exclusions

### Step 3: Filtering Logic

* Rejects irrelevant roles
* Applies scoring:

  * +2 → must-have keywords
  * +1 → nice-to-have
  * +5 → role match

### Step 4: Ranking

* Filters jobs with score ≥ threshold

### Step 5: Email Generation

* Builds HTML UI
* Sends curated jobs via Gmail SMTP


🧠 6. Scoring Engine (this impresses PMs)
## 🧮 Matching Algorithm

Score =

* (Must-have keywords × 2)
* (Nice-to-have × 1)
* (Role match bonus)

---

### Example:

Job: "AI Product Manager"

Matches:

* product ✅
* roadmap ✅
* ai ✅

Score = 2 + 2 + 1 + 5 = **10**

→ Selected


📬 7. Output Example
## 📧 Output

Users receive:

* Clean HTML email
* Top job matches
* Direct apply links
* Match score visibility

---

Example:

* Product Manager → Score: 9
* AI PM → Score: 11


🚀 8. Future Improvements (THIS IS GOLD)
## 🔮 Future Enhancements

* 🤖 GPT-based semantic matching
* 🌍 Multi-source job aggregation (LinkedIn, Indeed)
* 📊 Dashboard UI
* 📈 Learning-based ranking (feedback loop)
* 🧠 Vector embeddings for CV-job similarity


9. How to Run
## ▶️ Run Locally

```bash
pip install -r requirements.txt
python main.py
```

---

## ⚠️ Setup

* Add Gmail App Password
* Update `cv_profile.json`
* Add your CV PDF


