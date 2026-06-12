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


def supervisor_agent(
    question: str
):

    prompt = ChatPromptTemplate.from_template(
        """
        You are an AI supervisor.

        Decide which agent should answer.

        Available agents:

        resume
        skill_gap
        roadmap
        career_chat

        Question:

        {question}

        Return ONLY one word.

        """
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "question": question
        }
    )

    return response.content.strip().lower()