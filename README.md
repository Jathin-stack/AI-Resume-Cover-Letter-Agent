# 🧾 AI Resume & Cover Letter Agent

## 🚀 Problem Statement
Design an AI-powered multi-agent system that automatically generates, analyzes, and optimizes resumes and cover letters based on job descriptions, ensuring ATS compatibility and personalization.

---

## 💡 Solution
We built a **CrewAI-based multi-agent system** where specialized AI agents collaborate to:
- Generate resumes
- Analyze job descriptions
- Tailor resumes for ATS
- Write personalized cover letters

---

## 🧠 Agents

| Agent | Role |
|------|------|
| Resume Generator | Creates base resume |
| JD Analyzer | Extracts skills & keywords |
| Resume Tailor | Optimizes resume for ATS |
| Cover Letter Writer | Generates personalized cover letter |

---

## 🔄 Workflow

User Input  
↓  
Resume Generator Agent  
↓  
JD Analyzer Agent  
↓  
Resume Tailoring Agent  
↓  
Cover Letter Agent  
↓  
Final Output  

---

## 🛠️ Tech Stack
- CrewAI
- Python
- OpenAI API
- Gradio

---

## ▶️ Run Locally

```bash
git clone https://github.com/your-username/ai-resume-agent-crewai.git
cd ai-resume-agent-crewai
pip install -r requirements.txt
