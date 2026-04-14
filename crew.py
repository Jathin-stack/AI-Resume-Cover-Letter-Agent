from crewai import Crew
from agents import create_agents
from tasks import create_tasks

def run_crew(inputs):

    resume_agent, jd_agent, tailor_agent, cover_agent = create_agents()

    tasks = create_tasks(
        resume_agent,
        jd_agent,
        tailor_agent,
        cover_agent,
        inputs
    )

    crew = Crew(
        agents=[resume_agent, jd_agent, tailor_agent, cover_agent],
        tasks=tasks,
        verbose=True
    )

    result = crew.kickoff()
    return result
