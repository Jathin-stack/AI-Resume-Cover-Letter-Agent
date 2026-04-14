from crewai import Agent

def create_agents():

    resume_agent = Agent(
        role="Resume Generator",
        goal="Create ATS-friendly resumes",
        backstory="Expert resume writer with HR experience"
    )

    jd_agent = Agent(
        role="Job Description Analyzer",
        goal="Extract key skills and requirements",
        backstory="AI recruiter متخصص in job analysis"
    )

    tailor_agent = Agent(
        role="Resume Tailor",
        goal="Optimize resumes for ATS systems",
        backstory="ATS optimization expert"
    )

    cover_agent = Agent(
        role="Cover Letter Writer",
        goal="Write personalized cover letters",
        backstory="Professional career coach"
    )

    return resume_agent, jd_agent, tailor_agent, cover_agent
