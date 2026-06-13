import json

from langchain_google_genai import (
    ChatGoogleGenerativeAI
)

from langchain_core.prompts import (
    ChatPromptTemplate
)

from app.core.config import settings


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=settings.GEMINI_API_KEY,
    temperature=0
)


def analyze_skill_gap(
    skills: list[str],
    target_role: str
):
    print("Current Skills:", skills)
    print("Target Role:", target_role)

    prompt = ChatPromptTemplate.from_template(
        """
        You are an expert career coach.

        Current Skills:

        {skills}

        Target Role:

        {target_role}

        Return ONLY JSON.

        Format:

        {{
            "current_skills": [],
            "missing_skills": [],
            "recommendations": []
        }}
        """
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "skills": skills,
            "target_role": target_role
        }
    )

    content = response.content

    if content.startswith("```json"):
        content = (
            content
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

    return json.loads(content)