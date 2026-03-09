from schemas import ResumeClass

def skill_matcher_node(state:ResumeClass):
    jd_skills = state['Job_JD_details_extracted'].required_skills + state['Job_JD_details_extracted'].tools_and_technologies
    candidate_skills = state['Old_Resume_details_extracted'].technical_skills

    jd_skills = [skill.lower().strip() for skill in jd_skills]
    candidate_skills = [skill.lower().strip() for skill in candidate_skills]

    matched_skills = list(set(jd_skills) & set(candidate_skills))
    missing_skills = list(set(jd_skills) - set(candidate_skills))
    return {
        'matched_skills': matched_skills,
        'missing_skills': missing_skills
    }