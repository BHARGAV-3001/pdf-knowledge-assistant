from langchain_google_genai import (
    ChatGoogleGenerativeAI
)


def generate_answer(
    question,
    context
):

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2
    )

    prompt = f"""
You are a helpful document assistant.

Use ONLY the provided context.

If the answer is not present in the context,
say "I could not find that information."

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content