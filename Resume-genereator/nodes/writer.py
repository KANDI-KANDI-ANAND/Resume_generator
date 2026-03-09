from schemas import ResumeClass
from langchain_core.messages import SystemMessage, HumanMessage
from llm import rewriter_llm

def rewriter_node(state:ResumeClass):
    original_resume = state['Old_full_resume']
    improvement_plan = state['planner'] 
    jd = state['Job_JD_details_extracted']
    matched_skills = state['matched_skills']
    missing_skills = state['missing_skills']

    messages = [
        SystemMessage(content="You are an expert resume writer specialized in ATS-optimized resumes.Your task is to rewrite resumes so they align with job descriptions while keeping all information truthful."),
        HumanMessage(content=f"""
Rewrite the candidate resume following STRICT structural rules.

Return ONLY structured JSON matching the schema.

STRUCTURE RULES:

1. Preserve ALL sections that exist in the original resume.
2. DO NOT add new sections.
3. DO NOT remove sections.
4. If a section does not exist (internships/experience), return null.
                     
CONTACT DETAILS:
- Return the Linkedin and Github ids with the https:

SUMMARY RULES:
- Keep summary length 4-5 lines
- Only improve wording
- Do not change meaning

TECHNICAL SKILLS RULES:
- Preserve skill categories exactly
- Format must be:
  Category -> [skills]

Example:
"Programming & Scripting": ["Python","JavaScript"]

- Expand abbreviations only if present in JD.
                     
EXPERIENCE RULES:
Return each experience as:

{{
 "company": "...",
 "role": "...",
 "date": "...",
 "points": ["bullet1","bullet2"]
}}

INTERNSHIP RULES:
Return each internship as:

{{
 "company": "...",
 "role": "...",
 "date": "...",
 "points": ["bullet1","bullet2"]
}}

PROJECT RULES:
Return each project as:

{{
 "title": "...",
 "date": "...",
 "link": "...",
 "points": ["bullet1","bullet2"]
}}

ACHIEVEMENTS RULES:
Return each achievement as a separate bullet.

EDUCATION RULES:
Return each line exactly as in original resume.

CONTACT RULES:
Keep name, phone, email, linkedin, github unchanged.
                     
Original Resume:
{original_resume}
Improvement Plan:
{improvement_plan}
Job Description Details:
    Role Title: {jd.role_title}
    Required Skills: {', '.join(jd.required_skills)}
    Responsibilities: {', '.join(jd.responsibilities)}
    Experience Required: {jd.experience_required}

matched skills: {', '.join(matched_skills)}
""")
    ]

    response = rewriter_llm.invoke(messages)
    skills_text = ""

    for category, skills in response.technical_skills.items():
        skills_text += f"{category}: {', '.join(skills)}\n"

    summary_text = " ".join(response.professional_summary)

    education_text = "\n".join(response.education)

    achievement_text = "\n".join([f"• {a}" for a in response.achievements])
    
    resume_text = f"""{response.name}
    {response.phone} | {response.email} | {response.linkedin} | {response.github}

    PROFESSIONAL SUMMARY:
    {summary_text}

    TECHNICAL SKILLS:
    {skills_text}"""

    if response.experience:
        resume_text += "\nWORK EXPERIENCE:\n"
        for exp in response.experience:
            resume_text += f"{exp.role} - {exp.company} {exp.date}\n"
            for p in exp.points:
                resume_text += f"• {p}\n"


    if response.internships:
        resume_text += "\nINTERNSHIPS:\n"
        for intern in response.internships:
            resume_text += f"{intern.role} - {intern.company} {intern.date}\n"
            for p in intern.points:
                resume_text += f"• {p}\n"


    if response.projects:
        resume_text += "\nPROJECTS:\n"
        for proj in response.projects:
            resume_text += f"{proj.title} {proj.date}\n"
            if proj.link:
                resume_text += f"{proj.link}\n"
            for p in proj.points:
                resume_text += f"• {p}\n"

    resume_text += f"""

    ACHIEVEMENTS & CERTIFICATIONS
    {achievement_text}

    EDUCATION
    {education_text}
    """
    return {
        'optimized_resume': resume_text
    }