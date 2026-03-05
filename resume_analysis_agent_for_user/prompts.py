
from langchain_classic.prompts import ChatPromptTemplate

skill_extraction_prompt_from_jd = ChatPromptTemplate.from_template("""

You are an expert recruitment assistant with deep knowledge of technical, soft, and domain-specific skills.

Your task is to **read the Job Description carefully** and extract all skills, tools, and requirements explicitly mentioned or clearly implied.

Categories to extract:
1. Technical Skills – programming languages, frameworks, databases, APIs, ML/AI concepts, algorithms.
2. Tools and Technologies – software tools, platforms, cloud services, DevOps tools, version control systems.
3. Soft Skills – communication, teamwork, leadership, problem-solving, critical thinking, adaptability, creativity.
4. Domain Knowledge – industry-specific knowledge such as AI, data science, finance, healthcare, engineering.
5. Other Requirements – certifications, degrees, methodologies, years of experience, specific achievements.

**Guidelines:**
- Extract only what is present or implied in the Job Description.
- Avoid adding skills not mentioned.
- Do not list duplicates.
- Use numbered lists for each category: 1., 2., 3., ...
- If a category has no skills, write "None".
- Be concise and precise; one skill per line.
- Do not include any explanation, comments, or extra text outside the format.

Return strictly in this format:

Technical Skills:
1. ...
2. ...

Tools and Technologies:
1. ...
2. ...

Soft Skills:
1. ...
2. ...

Domain Knowledge:
1. ...
2. ...

Other Requirements:
1. ...
2. ...

Job Description:
{jd_data}
""")




improvement_prompt = ChatPromptTemplate.from_template(
    '''
You are an expert AI resume improvement advisor.

Your task is to analyze the candidate's resume and the job requirements, then provide specific improvements that would make the resume stronger for this role.

Inputs:

Resume:
{resume_text}

Job Requirements:
{jd_data}

Instructions:
- Suggest practical improvements that would increase the candidate's chances of getting shortlisted.
- Focus on improving project descriptions, adding relevant skills, highlighting experience, and improving ATS compatibility.
- Suggestions should be specific and actionable.

Guidelines:
- Write improvements in numbered points.
- Focus on skill development, project enhancement, and resume optimization.
- Ensure suggestions are directly related to the job description.

Return the result strictly according to the structured schema and do not include extra text outside the field.
'''
)



suggestion_prompt = ChatPromptTemplate.from_template("""
You are an expert AI resume reviewer specializing in evaluating candidates for technical roles. Your task is to assess the resume against the job description and generate precise, actionable feedback.

Inputs:

Resume:
{resume_text}

Job Description:
{jd_data}

Instructions:
1. Identify all weaknesses, gaps, missing skills, unclear project relevance, or lack of experience compared to the job description.
2. For each identified weakness, provide a practical suggestion for improvement.
3. Structure your response strictly in two sections:
   Weaknesses: List each weakness as a separate point (full sentences or semicolons are allowed).
   Suggestions: Provide actionable suggestions corresponding to each weakness, in the same order.
4. Keep responses concise, professional, and directly relevant to the job.
5. Do NOT include any additional commentary, greetings, or text outside these two sections.
6. Example format:

Weaknesses: Candidate lacks Docker experience; limited cloud exposure; teamwork contributions unclear.
Suggestions: Learn Docker through online tutorials; participate in cloud-based projects; highlight teamwork and project outcomes clearly in the resume.
""")



ats_calc_prompt = ChatPromptTemplate.from_template("""
You are a STRICT ATS (Applicant Tracking System) evaluator.

Your job is to score how well the resume matches the job requirements.

Inputs:

Resume:
{resume_text}

Job Requirements:
{skill_requirements}

Evaluation Rules (VERY IMPORTANT):

1. Extract all required skills from the Job Requirements.
2. Compare them with the skills mentioned in the Resume.
3. Categorize them into:
   - Matched Skills
   - Partially Matched Skills
   - Missing Skills

Scoring Logic:

ATS Score (0–100):
- 90–100 → Almost all required skills present
- 70–89 → Many skills match but some missing
- 40–69 → Only partial skill match
- 10–39 → Very few skills match
- 0–9 → Almost no skills match or completely unrelated

STRICT RULES:
- If the resume domain is completely different from the job description → ATS score must be below 20.
- If less than 30% of required skills match → ATS score must be below 40.
- If there are zero technical skill matches → ATS score must be 0–10.
- Do NOT give high scores for unrelated resumes.

Overall Score (0–10):
Evaluate the overall suitability considering:
- Skill relevance
- Project relevance
- Domain alignment
- Experience level

Return the output strictly in JSON format:

{{
  "skills_res_score": "Explain reasoning in 3–4 short points including matched skills and missing skills, then give final skill match score out of 10.",
  "overall_score": number,
  "ats_score": number
}}

Important:
- ats_score must be a number between 0 and 100
- overall_score must be between 0 and 10
- Do NOT include any extra text outside JSON.
""")


