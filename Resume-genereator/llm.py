from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from schemas import personalDetails, JD_Schema, optimizedResume, ATSDecision


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite"
)


structured_parser_llm = llm.with_structured_output(personalDetails)

JD_Analyser_llm = llm.with_structured_output(JD_Schema)

rewriter_llm = llm.with_structured_output(optimizedResume, method="json_schema")

ats_llm = llm.with_structured_output(ATSDecision)

