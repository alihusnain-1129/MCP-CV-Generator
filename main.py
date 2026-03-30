from fastmcp import FastMCP

mcp = FastMCP("CV Generator MCP")

def analyze_input(file_content: str = "", text_input: str = ""):
    return file_content if file_content else text_input


@mcp.tool()
def summarize_cv(file_content: str = "", text_input: str = "") -> str:
    text = analyze_input(file_content, text_input)

    return f"""
You are an expert CV writer.

Analyze the following text and generate a concise professional summary.

Instructions:
- Keep it 3–4 lines
- Make it impactful and role-specific
- Do NOT copy text directly
- Rewrite professionally

Template style:
"Proactive AI/ML Engineer with hands-on experience in developing and deploying machine learning models, building scalable web applications using Django, integrating AI-powered chatbots through LLM APIs. Designing MCP servers for advanced AI tool integration and automation."

Input:
{text}
"""

@mcp.tool()
def generate_education(file_content: str = "", text_input: str = "") -> str:
    text = analyze_input(file_content, text_input)

    return f"""
Extract and format the Education section from the given text.

Instructions:
- Include Degree, Field, University, Location, Dates
- Keep it concise and professional

Template:
"Bachelor of Science, Computer Science | University Name, City, Country [Start–End]"

Input:
{text}
"""

@mcp.tool()
def generate_experience(file_content: str = "", text_input: str = "") -> str:
    text = analyze_input(file_content, text_input)

    return f"""
Generate a professional Experience section.

Instructions:
- Include Role, Company, Location, Dates
- Write 3–4 bullet points
- Start each bullet with action verbs
- Focus on impact and achievements

Template:
AI/ML Intern – Company Name, Location [Start - End]
● Bullet point
● Bullet point
● Bullet point

Input:
{text}
"""

@mcp.tool()
def generate_projects(file_content: str = "", text_input: str = "") -> str:
    text = analyze_input(file_content, text_input)

    return f"""
Generate a Projects section.

Instructions:
- Include project title + description
- Focus on technologies and outcomes
- Keep it concise

Template:
"Project Name – Description with tools and impact"

Input:
{text}
"""

@mcp.tool()
def generate_certifications(file_content: str = "", text_input: str = "") -> str:
    text = analyze_input(file_content, text_input)

    return f"""
Extract Certifications & Awards from the given input.

Instructions:
- Include certifications, awards, memberships, and achievements
- Keep bullet format
- Keep it concise and professional

Template:
Certifications & Awards:
• Certification Name — Organization, Date (Optional Details)
• Role / Award — Organization, Year

STRICT RULES:
- Output ONLY the final section
- Do NOT include explanations

Input:
{text}
"""

@mcp.tool()
def extract_skills(full_text: str) -> str:
    return f"""
Extract relevant skills and assign proficiency levels.

Instructions:
- Categorize skills (Programming, ML, Tools, etc.)
- Assign levels: Beginner / Intermediate / Advanced / Expert
- Adapt based on role (AI/ML, Web, etc.)

Template:
Programming & Scripting: Python (Expert)
Machine Learning & AI: Machine Learning (Advanced), Deep Learning (Advanced)
Web Development & APIs: REST APIs (Expert), Django (Expert)

Input:
{full_text}
"""


@mcp.tool()
def generate_profile(
    summary: str,
    education: str,
    experience: str,
    projects: str,
    certifications: str,
    skills: str
) -> str:

    return f"""
Create a complete professional CV profile.

Instructions:
- Combine all sections cleanly
- Keep formatting professional
- Do NOT repeat content

Structure:
Summary
Education
Experience
Projects
Skills

Content:
Summary:
{summary}

Education:
{education}

Experience:
{experience}

Projects:
{projects}

Certifications & Awards:
{certifications}

Skills:
{skills}
"""

if __name__ == "__main__":
    mcp.run()