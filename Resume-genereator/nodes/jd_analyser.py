from schemas import ResumeClass
from langchain_core.messages import SystemMessage, HumanMessage
from llm import JD_Analyser_llm

def JD_Analyser_node(state:ResumeClass):

    Job_description = state['Job_JD']
    messages = [
         SystemMessage(content="You are an expert job description parser that extracts structured information from job descriptions."),
        HumanMessage(content=f"""
You are an expert system that analyzes job descriptions and extracts structured hiring requirements.

Your task is to carefully read the job description and extract the details
If the Job title is not mentioned in the description, infer it based on the responsibilities and required skills mentioned in the description.
If the required skills are not explicitly mentioned, infer them based on the responsibilities and tools/technologies mentioned in the description.

Important Rules:
- Only extract information that appears in the job description.
- Do NOT invent skills or responsibilities.
- Remove duplicates and dont return the shortform skills (eg: ML, NLP, RAG, MCP, etc)
- Keep skills and tools concise.
- If the skills in the JD are in the shortform (eg: ML, NLP, RAG, MCP, etc), expand them to their full form (eg: Machine Learning, Natural Language Processing, Retrieval Augmented Generation, Model-context-protocol, etc) using your own knowledge and return them.
- Use short phrases instead of long sentences.
                   
                     
Job Description:
{Job_description}""")
    ]
    response = JD_Analyser_llm.invoke(messages)
    return {
        'Job_JD_details_extracted': response
        }
    