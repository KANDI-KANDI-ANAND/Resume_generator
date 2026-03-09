
# 🚀 AI Resume Optimizer (Agentic AI Resume Generator)

An **Agentic** AI-powered resume optimization system that analyzes a candidate's resume against a job description and automatically generates an ATS-optimized resume.  
This system uses a LangGraph multi-node pipeline to parse resumes, analyze skill gaps, plan improvements, rewrite the resume, validate ATS compatibility, and generate a professional PDF resume output.  
The project also includes a Streamlit UI that allows users to upload their resume, provide a job description through a chat interface, and download an optimized resume.

---

## 🧠 Project Overview

This project implements an Agentic AI architecture using LangGraph where each step of the resume optimization pipeline is handled by a specialized node.

The system performs the following steps:

- Resume Parsing  
- Skill Extraction  
- Job Description Analysis  
- Skill Matching  
- Gap Analysis  
- Resume Improvement Planning  
- Resume Rewriting  
- ATS Score Validation  
- PDF Resume Generation  

The final result is a structured, ATS-optimized resume in PDF format.

---

## ✨ Features

- Automated ATS resume optimization  
- Agentic AI pipeline using LangGraph  
- Skill gap analysis  
- Structured resume rewriting  
- Dynamic handling of projects, internships, and experience  
- Professional PDF generation  
- Interactive Streamlit chat interface  
- Multiple resume generations from a single uploaded resume  
- Supports different job descriptions  

---

## 🏗 Architecture

The system is built as a LangGraph pipeline:

```text
Resume Parser
      ↓
Skill Extractor
      ↓
JD Analyzer
      ↓
Skill Matcher
      ↓
Gap Analyzer
      ↓
Planner
      ↓
Resume Writer
      ↓
ATS Validator
      ↓
PDF Builder
```

<img width="274" height="1051" alt="Project_Graph" src="https://github.com/user-attachments/assets/e6c38699-be89-4649-9ce9-84aeccbeb7c8" />

Each step is implemented as a separate node, making the system modular and easy to extend.

---

## 📂 Folder Structure

```text
Resume_Generator
│
├── nodes
│   ├── __init__.py
│   ├── ats_validator.py
│   ├── gap_analyser.py
│   ├── jd_analyser.py
│   ├── pdf_builder.py
│   ├── planner.py
│   ├── resume_parser.py
│   ├── skill_extractor.py
│   ├── skill_matcher.py
│   └── writer.py
│
├── .env
├── .gitignore
├── graph.py
├── llm.py
├── main.py
├── router.py
├── schemas.py
├── app.py
└── README.md
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/KANDI-KANDI-ANAND/Resume_generator.git
cd Resume_generator
```

### 📦 Install uv (Python Package Manager)

If `uv` is not installed:

```bash
pip install uv
```

Or install using `curl`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 🧪 Create Virtual Environment

```bash
uv venv
```

Activate the environment:

Mac / Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 📚 Install Dependencies

```bash
uv pip install -r requirements.txt
```

If `requirements.txt` does not exist, generate it:

```bash
uv pip freeze > requirements.txt
```

---

## 🔑 Setup Environment Variables

Create a `.env` file in the root directory.

Example:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

You can obtain a Gemini API key from:  
https://aistudio.google.com/app/apikey

---

## ▶️ Running the Application

Start the Streamlit UI:

```bash
streamlit run app.py
```

The application will start at:

```text
http://localhost:8501
```

---

## 💻 How to Use

- Enter your Google API key  
- Upload your existing resume (PDF)  
- Start chatting with the assistant  
- Paste the job description  
- The system analyzes the resume and job description  
- The system generates an ATS-optimized resume  
- Download the generated PDF resume  

---

## 🔄 Example Workflow

```text
User uploads resume
      ↓
User provides job description
      ↓
System extracts resume information
      ↓
Job description is analyzed
      ↓
Skill gap analysis performed
      ↓
Resume improvement strategy generated
      ↓
Resume rewritten with ATS keywords
      ↓
ATS validation performed
      ↓
Optimized resume PDF generated
```

---

## 📄 Example Output

The generated resume includes:

- Optimized professional summary  
- Improved technical skills section  
- ATS keyword alignment  
- Enhanced project descriptions  
- Structured formatting  
- Clickable links  
- Professional PDF layout  

---

## 🚀 Future Improvements

- Training a ML Model with the best ats scored resumes to evaluate the job description and to create the best resume 
- Multiple resume templates  and Support for DOCX resumes
- using RAG (pdf reading) concept to read the uploaded resume properly
- Converting this application to the AI startup tool (1 optimized resume for 1rs.)

---

## 📜 License

MIT License

---

## 👨‍💻 Author

**Anand**  
Agentic AI Engineer
