from schemas import ResumeClass
from typing import List
from langchain_core.messages import SystemMessage, HumanMessage
from llm import ats_llm


def calculate_ats_score(resume_text:str, jd_skills:List[str]):
    resume_text = resume_text.lower()
    matched = 0
    for skill in jd_skills:
        if skill.lower() in resume_text:
            matched += 1

    score = (matched / len(jd_skills)) * 100 if jd_skills else 0
    return round(score, 1)



def ats_validator_node(state:ResumeClass):
    jd = state['Job_JD_details_extracted']
    jd_skills = jd.required_skills + jd.tools_and_technologies

    old_resume = state['Old_full_resume']
    optimized_resume = state['optimized_resume']

    old_score = calculate_ats_score(old_resume, jd_skills)
    new_score = calculate_ats_score(optimized_resume, jd_skills)

    iteration = state['iteration'] + 1
    max_iteration = state['max_iteration']

    reason = ""

    if new_score >= 95:
        status = "approved"
    elif iteration == max_iteration:
        messages = [
            SystemMessage(content="You are a senior ATS score validator. Your task is to evaluate whether the optimized resume meets the ATS score threshold for the given job description."),
            HumanMessage(content=f"""
The optimized resume has reached the maximum number of iterations ({max_iteration}) but still does not meet the ATS score threshold of 95%.
Please evaluate the {optimized_resume} ats score against the job description.
Job Description Details:
    Role Title: {jd.role_title}
    Required Skills: {', '.join(jd.required_skills)}
    Responsibilities: {', '.join(jd.responsibilities)}
    Experience Required: {jd.experience_required}

    Return :
        1. The ats score in the format "optimized_ats_score: X%" 
        2. If optimized_ats_score meets the 95% score or does not meet the 95% score, return output as status = "approved" and provide output as a detailed analysis of why it is not meeting the requirements whether the reason is lack of skills, or lack of expeience in a "reason" variable.
""")
        ]
        
        response = ats_llm.invoke(messages)
        status = response.status
        reason = response.reason
        new_score = response.optimized_ats_score
    else:
        status = "needs_improvement"

    return {
        'old_resume_ats_score': old_score,
        'optimized_resume_ats_score': new_score,
        'iteration': iteration,
        'Validation': status,
        'reason' : reason
    }