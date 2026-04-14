from crewai import Task

def create_tasks(resume_agent, jd_agent, tailor_agent, cover_agent, inputs):

    skills = inputs["skills"]
    projects = inputs["projects"]
    experience = inputs["experience"]
    job_description = inputs["job_description"]

    resume_task = Task(
        description=f"""
        Create an ATS-friendly resume using:
        Skills: {skills}
        Projects: {projects}
        Experience: {experience}
        """,
        agent=resume_agent,
        expected_output="Professional resume"
    )

    jd_task = Task(
        description=f"""
        Analyze this job description and extract:
        skills, keywords, responsibilities:
        {job_description}
        """,
        agent=jd_agent,
        expected_output="Structured job insights"
    )

    tailor_task = Task(
        description="""
        Optimize the resume based on job analysis.
        """,
        agent=tailor_agent,
        expected_output="Tailored resume"
    )

    cover_task = Task(
        description="""
        Write a personalized cover letter.
        """,
        agent=cover_agent,
        expected_output="Cover letter"
    )

    return [resume_task, jd_task, tailor_task, cover_task]
