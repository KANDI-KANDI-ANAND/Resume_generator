from pydantic import BaseModel, Field
from typing import List, Literal, TypedDict, Optional
from dotenv import load_dotenv
load_dotenv()



class personalDetails(BaseModel):
    name: str = Field(description="Full name of the candidate")
    email: str = Field(description="Email address of the candidate")
    phone: str = Field(description="Phone number of the candidate")
    linkedin: str = Field(description="LinkedIn profile URL of the candidate")
    github: str = Field(description="GitHub profile URL of the candidate")
    professional_summary: str = Field(description="Professional summary of the candidate")
    technical_skills: List[str] = Field(description="List of technical skills")
    projects: List[str] = Field(description="List of projects")
    internships: List[str] = Field(description="List of internships")
    work_experience: List[str] = Field(description="List of work experience entries")
    education: List[str] = Field(description="List of education entries")
    achievements: List[str] = Field(description="List of achievements")
    fresher: bool = Field(description="Indicates if the candidate is a fresher (True) or has work experience (False)")



class Experience(BaseModel):
    company: str
    role: str
    date: str
    points: List[str]

class Internship(BaseModel):
    company: str
    role: str
    date: str
    points: List[str]

class Project(BaseModel):
    title: str
    date: str
    link: Optional[str] = None
    points: List[str]


class ATSDecision(BaseModel):
    optimized_ats_score: float
    status: str
    reason: Optional[str]



class optimizedResume(BaseModel):
    name: str = Field(description="Full name of the candidate")
    phone: str = Field(description="Phone number of the candidate")
    email: str = Field(description="Email address of the candidate")
    linkedin: str = Field(description="LinkedIn profile URL of the candidate")
    github: str = Field(description="GitHub profile URL of the candidate")
    professional_summary: List[str] = Field(description="Professional summary of the candidate")
    technical_skills: dict[str, List[str]] = Field(description="List of technical skills with emphasis level")
    internships: Optional[List[Internship]] = None
    experience: Optional[List[Experience]] = None
    projects : Optional[List[Project]] = Field(description="List of projects")
    achievements: List[str] = Field(description="List of achievements")
    education: List[str] = Field(description="Educational qualification")


class JD_Schema(BaseModel):
    role_title: str = Field(description="Title of the job position")
    required_skills: List[str] = Field(description="List of required skills for the job")
    tools_and_technologies: List[str] = Field(description="List of tools and technologies mentioned in the job description")
    responsibilities: List[str] = Field(description="List of key responsibilities mentioned in the job description")
    experience_required: str = Field(description="Experience required for the job in years")


class ResumeClass(TypedDict):
    Old_Resume: str
    Old_full_resume : str
    
    Old_Resume_details_extracted: personalDetails
    
    Job_JD: str
    Job_JD_details_extracted: JD_Schema

    matched_skills: List[str]
    missing_skills: List[str]
    
    gap_Analysis: str
    planner: str
    optimized_resume: str
    iteration : int
    old_resume_ats_score: float
    optimized_resume_ats_score: float
    max_iteration: int
    reason: Optional[str]
    pdf_path: str
    Validation : Literal["approved", "needs_improvement"]
    
