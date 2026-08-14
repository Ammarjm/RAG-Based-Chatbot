from langchain_core.prompts import PromptTemplate

template = """
You are a helpful AI assistant for Al-Balqa Applied University.

Answer the user's question using only the provided context.

If the answer is not available in the context, say:
"I could not find this information in the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""

prompt = PromptTemplate(
    input_variables=["input_language", "output_language"],
    template=template,
)

# python prompts.py