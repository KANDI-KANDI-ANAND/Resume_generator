from dotenv import load_dotenv
load_dotenv()

from graph import workflow

Job_description = """About the job
Role Description: The GenAI Developer is responsible for designing, developing, and implementing generative AI models and systems. This role combines the expertise of an AI developer with the specialized skills of a prompt engineer to create advanced AI solutions that generate content, automate processes, and enhance user experiences.



Main Responsibilities:

Design and develop generative AI models.
Implement prompt engineering techniques to optimize AI outputs.
Collaborate with cross-functional teams to integrate AI solutions.
Conduct research to improve generative AI capabilities.
Develop and maintain documentation for AI models and systems.
Ensure the quality and accuracy of generated content.
Monitor and optimize the performance of AI systems.
Stay updated on the latest advancements in generative AI.
Provide training and support on generative AI technologies.
Drive innovation in AI development and deployment.


Required Competences:

Proficiency in AI development tools and languages (e.g., Python, TensorFlow).
Strong understanding of generative AI algorithms.
Expertise in prompt engineering techniques.
Excellent problem-solving and analytical skills.
Ability to work with large and complex datasets.
Strong communication and collaboration abilities.
Knowledge of cloud platforms and AI deployment.
Experience with AI research and development.
Understanding of software development principles.
Ability to translate business requirements into technical solutions.




Required Certifications:

Certification in AI development (e.g., AI Specialist, Machine Learning Certification).
Certification in generative AI technologies.
Certification in prompt engineering.
Certification in cloud platforms (e.g., AWS Certified Solutions Architect).
Certification in software development (e.g., Certified Software Development Professional).
Continuous education in AI and prompt engineering.
Professional development courses in generative AI.
Certification in communication and collaboration tools.
Certification in data science and analytics.
Certification in innovation and technology management.


Required Experience:

Proven experience in AI development roles.
Extensive experience in generative AI model development.
Experience in implementing prompt engineering techniques.
Experience in collaborating with cross-functional teams.
Experience in conducting AI research.
Experience in ensuring the quality and accuracy of AI outputs.
Experience in monitoring and optimizing AI systems.
Experience in staying updated on industry trends.
Experience in providing training and support.
Experience in driving innovation in AI development.

Requirements added by the job poster

• 3+ years of work experience with Generative AI Tools

• 4+ years of work experience with Generative AI

• 3+ years of work experience with Prompt Engineering"""


initial_state = {
    'Old_Resume': "Anand_Agentic_AI_Resume_1.pdf",
    'Job_JD': Job_description,
    'iteration': 0,
    'max_iteration': 4
}
result = workflow.invoke(initial_state)

print("✅ Resume Optimization Complete!")
print(f"Old ATS Score     : {result['old_resume_ats_score']}%")
print(f"Optimized ATS Score: {result['optimized_resume_ats_score']}%")

if result.get('reason'):
    print(f"Reason : {result['reason']}")