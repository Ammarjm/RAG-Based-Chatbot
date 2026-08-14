from RAG import create_retriever
from llm_model import llm
from prompts import prompt
from langchain_core.messages import HumanMessage

print('App is running...')

retriever = create_retriever()

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    docs = retriever.invoke(question)

    context = "\n".join(doc.page_content for doc in docs)

    final_prompt = prompt.format(context=context, question=question)

    response = llm.invoke([HumanMessage(content=final_prompt)])

    print(f"\nAI: {response.content}")


# python app.py

