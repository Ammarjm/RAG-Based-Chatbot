from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def create_retriever():

# 1. Load the Text file
    loader = TextLoader("balqa_ai.txt", encoding="utf-8")
    documents = loader.load()

# 2. Cut the document into smaller pieces

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=20
    )

    chunks = text_splitter.split_documents(documents)

# 3. Create embeddings

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"}
    )

# 4. Store embeddings in FAISS

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

# 5. Create retriever

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever

if __name__ == "__main__":

    retriever = create_retriever()

    question = "When was the Faculty of Artificial Intelligence established?"

    results = retriever.invoke(question)

    print("\nRetrieved Information:\n")

    for i, document in enumerate(results, start=1):
        print(f"Chunk {i}:")
        print(document.page_content)
        print("-" * 50)

