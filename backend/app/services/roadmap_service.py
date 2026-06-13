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


def generate_learning_roadmap(
    current_skills,
    missing_skills,
    target_role
):

    prompt = ChatPromptTemplate.from_template(
        """
        You are an expert career mentor.

        Current Skills:
        {current_skills}

        Missing Skills:
        {missing_skills}

        Target Role:
        {target_role}

        Create a detailed 4-week roadmap.

        Return ONLY JSON.

        Format:

        {{
            "week_1": [],
            "week_2": [],
            "week_3": [],
            "week_4": []
        }}
        """
    )
    print("Current Skills:", current_skills)
    print("Missing Skills:", missing_skills)
    print("Target Role:", target_role)

    chain = prompt | llm

    response = chain.invoke(
        {
            "current_skills": current_skills,
            "missing_skills": missing_skills,
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