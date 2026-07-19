# Recruiter Post Analyzer

A web application built with Streamlit that helps extract useful information from recruiter posts and job descriptions. The application also uses Google Gemini to summarize job requirements and compare a resume against the uploaded job description.

This project was built to simplify the process of understanding recruiter posts by automatically extracting important details such as job roles, skills, locations, recruiter emails, and hiring trends.

---

## Features

### Recruiter Post Extraction

- Upload recruiter posts in PDF or TXT format
- Extract:
  - Job role
  - Recruiter email
  - Location
  - Job type
  - Required skills
  - Country
- Basic spam detection

---

### Analytics Dashboard

View insights from the extracted data, including:

- Total recruiter posts
- Hiring locations
- Most common job roles
- Job type distribution
- Frequently requested skills
- Search and filtering
- CSV export

---

### AI Job Analysis

Uses Google Gemini to generate:

- Job summary
- Experience requirements
- Education requirements
- Responsibilities
- Soft skills
- Resume keywords

---

### Resume Matcher

Upload a resume and compare it with the job description.

The application provides:

- Match score
- Matching skills
- Missing skills
- Strengths
- Suggestions for improvement
- Overall recommendation

---

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- Pandas
- Plotly
- pdfplumber

---

## Project Structure

```text
Recruiter-Post-Analyzer/
│
├── app.py
├── components/
├── services/
├── models/
├── styles/
├── data/
├── logs/
├── config.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/aaryar20/Recruiter-Post-Analyzer.git
```

Go to the project folder

```bash
cd Recruiter-Post-Analyzer
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

macOS / Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install the required packages

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project directory.

```text
GEMINI_API_KEY=your_api_key
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## Screenshots


---

## Possible enhancements

Some ideas I plan to add in future versions:

- PDF report generation
- Better spam detection
- Company name extraction
- Dark mode
- Resume history
- Improved ATS scoring
- Support for multiple job descriptions

---

## What I Learned

Building this project helped me get hands-on experience with:

- Working with the Google Gemini API
- Parsing and processing PDF files
- Building interactive dashboards using Plotly
- Structuring larger Streamlit applications using reusable components
- Designing a clean and user-friendly interface

---

## Author

**Aarya Rashinker**

Electronics and Telecommunication Engineering Student

GitHub: https://github.com/aaryar20

## Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project!