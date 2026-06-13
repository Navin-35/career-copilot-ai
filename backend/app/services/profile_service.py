import json

from langchain_google_genai import (
    ChatGoogleGenerativeAI
)

from langchain_core.prompts import ChatPromptTemplate

from app.core.config import settings


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=settings.GEMINI_API_KEY,
    temperature=0
)


def analyze_resume_text(
    resume_text: str
):

    prompt = ChatPromptTemplate.from_template(
        """
        Analyze the following resume.

        Return ONLY valid JSON.

        Format:

        {{
            "skills": [],
            "projects": [],
            "education": [],
            "experience": []
        }}

        Resume:

        {resume}
        """
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "resume": resume_text
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