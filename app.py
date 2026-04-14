import gradio as gr
from crew import run_crew

def run_pipeline(skills, projects, experience, job_description):

    inputs = {
        "skills": skills,
        "projects": projects,
        "experience": experience,
        "job_description": job_description
    }

    result = run_crew(inputs)
    return result


iface = gr.Interface(
    fn=run_pipeline,
    inputs=[
        gr.Textbox(label="Skills"),
        gr.Textbox(label="Projects"),
        gr.Textbox(label="Experience"),
        gr.Textbox(label="Job Description")
    ],
    outputs=gr.Textbox(label="Final Output"),
    title="CrewAI Resume Agent"
)

iface.launch()
