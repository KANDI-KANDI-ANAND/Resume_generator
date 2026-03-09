from schemas import ResumeClass
from langchain_core.messages import SystemMessage, HumanMessage
from llm import llm

def planner_node(state:ResumeClass):
    gap_analysis = state['gap_Analysis']
    original_resume = state['Old_full_resume']
    matched_skills = state['matched_skills']
    missing_skills = state['missing_skills']
    jd_details = state['Job_JD_details_extracted']

    messages = [
        SystemMessage(content="You are an expert resume optimization strategist"),
        HumanMessage(content=f"""Based on the gap analysis and job description, create a clear improvement plan for the candidate's resume.
        Your task is to design a strategy that improves the resume while keeping all information truthful.
                     
        The plan must answer:
                     
        1. Which resume sections should be modified
        2. Which skills should be emphasized
        3. Where should missing keywords appear
        4. Which projects or experiences should be highlighted            
        5. Additional improvements to better align the resume with the role
                     
        Make that plan considering all the given inputs (gap analysis, original resume, matched skills, missing skills, job description details) below.
                     
        Rules to follow:
        - Do NOT rewrite the resume.
        - Only create an improvement strategy.
        - Do NOT invent skills or experiences that do not exist in the resume.
        - Return the plan as numbered steps.
        
Gap Analysis: {gap_analysis}
Original Resume: {original_resume}
Matched Skills: {', '.join(matched_skills)}
Missing Skills: {', '.join(missing_skills)}
Role Title:
{jd_details.role_title}

Required Skills:
{', '.join(jd_details.required_skills)}

Responsibilities:
{', '.join(jd_details.responsibilities)}

Experience Required:
{jd_details.experience_required}

    """)
    ]

    response = llm.invoke(messages)
    return {
        'planner': response.content
    }
