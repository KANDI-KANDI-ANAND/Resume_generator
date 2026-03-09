from schemas import ResumeClass
from langchain_core.messages import SystemMessage, HumanMessage
from llm import structured_parser_llm

def Skill_Extractor_node(state:ResumeClass):
    full_text = state['Old_full_resume']

    messages = [
        SystemMessage(content="You are an expert resume parser that extracts structured information from resumes."),
        HumanMessage(content=f"""
    Extract the following details from the resume text and return them in string format.
    
    Rules to follow:
    1. Extract the candidate's full name, email address, phone number, LinkedIn profile URL, GitHub profile URL, professional summary, technical skills, projects, internships, work experience entries, education entries, and achievements.
    2. If the resume does not contain work_experience and internships, return Fresher:True, else Fresher:False.

Resume Text:
{full_text}
""")
    ]

    response = structured_parser_llm.invoke(messages)
    return {
        'Old_Resume_details_extracted': response
        }