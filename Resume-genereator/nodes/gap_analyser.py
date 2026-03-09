from schemas import ResumeClass
from langchain_core.messages import SystemMessage, HumanMessage
from llm import llm

def gap_analyser_node(state:ResumeClass):
    matched_skills = state['matched_skills']
    missing_skills = state['missing_skills']
    
    jd = state["Job_JD_details_extracted"]
    resume = state["Old_Resume_details_extracted"]

    jd_details = (
        jd.required_skills +
        jd.tools_and_technologies +
        [jd.experience_required] +
        jd.responsibilities
    )

    candidate_details = (
        resume.technical_skills +
        [resume.professional_summary] +
        resume.work_experience
    )
    
    messages = [
        SystemMessage(content="You are a career coach that helps job applicants analyze the gap between their skills and the job requirements, and provides personalized advice on how to bridge that gap."),
        HumanMessage(content=f"""You just analyze the gap between the candidate's skills and the job requirements based on the matched and missing skills
        Based on the below information , Return your analysis in a text format not in question and answering format.
        1. Which required skills are missing?
        2. Which important skills are already present?
        3. Which responsibilities from the job description are not reflected in the resume?
        4. Where the resume needs improvement to match the role.
                     
        Rules to follow:
        1.Return the analysis as a single paragraph.
        2.Do not invent skills that do not appear in the job description.                          

Matched Skills: {', '.join(matched_skills)}
Missing Skills: {', '.join(missing_skills)}
Job Requirements: {', '.join(jd_details)}
Candidate Details: {', '.join(candidate_details)}
""")]
    
    response = llm.invoke(messages)
    return {
        'gap_Analysis': response.content
    }