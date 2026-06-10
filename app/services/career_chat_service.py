from langchain_google_genai import (
    ChatGoogleGenerativeAI
)

from langchain_core.prompts import (
    ChatPromptTemplate
)

from app.core.config import settings

from app.services.rag_service import (
    search_knowledge_base
)


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=settings.GEMINI_API_KEY
)


def career_chat(
    question: str
):

    docs = search_knowledge_base(
        question
    )

    context = "\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )

    prompt = ChatPromptTemplate.from_template(
        """
        Answer using ONLY this context:

        {context}

        Question:

        {question}
        """
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    return response.content