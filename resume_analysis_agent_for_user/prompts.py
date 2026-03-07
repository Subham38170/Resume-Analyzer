
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
You are a Senior Technical Recruiter and Expert ATS Optimizer. 

Your goal is to perform a high-fidelity match analysis between a candidate's Resume and a Job Description. 

Inputs:
Resume: {resume_text}
Job Description: {jd_data}

Evaluation Framework:
1. Contextual Matching: Look beyond exact keyword matches. Recognize synonyms (e.g., "AWS" vs "Amazon Web Services") and transferable technical domains.
2. Skill Categorization:
   - Hard Skills: Technical tools, languages, and frameworks.
   - Soft Skills/Domain: Leadership, methodology (Agile), and industry-specific knowledge.
3. Gap Analysis: Identify what critical requirements are missing that would be deal-breakers.

Scoring Guidelines:
- 85-100: Excellent match. The candidate has the core tech stack and relevant experience.
- 70-84: Strong match. Has most core skills but lacks 1-2 secondary requirements.
- 50-69: Potential match. Has the foundation but requires training in specific areas.
- Below 50: Significant gaps in experience or tech stack.

Refined Scoring Rule:
- If the domain is a total mismatch (e.g., Nurse applying for Java Dev), score 0-15.
- If the candidate has the core tech stack but lacks specific niche tools, do NOT penalize heavily; score in the 75-85 range.

Return the output strictly in JSON format:
{{
  "skills_res_score": "Provide a nuanced 3-point summary: 1) Top strengths/matches, 2) Key missing gaps, 3) Cultural/Domain fit. End with a 1-10 rating.",
  "overall_score": 0,
  "ats_score": 0
}}

Important: 
- The overall_score is (ats_score / 10).
- Be objective but fair. Do not include any text outside the JSON block.
""")

