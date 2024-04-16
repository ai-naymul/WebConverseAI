from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from dotenv import load_dotenv
load_dotenv()
import os
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


class RetrieverChain:
    def __init__(self) -> None:
        pass

    def get_context_retriever_chain(vector_store):
        llm = GoogleGenerativeAI(GOOGLE_API_KEY)
        retriever = vector_store.as_retriever()
        prompt = ChatPromptTemplate.from_messages(
            [
                MessagesPlaceholder(variable_name='chat_history'),
                ('user', '{inputs}'),
                ("user", "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation")
            ]
        )

        retriever_chain = create_history_aware_retriever(llm, retriever, prompt)

        return retriever_chain

    def get_conversational_rag_chain(retriever_chain):
        llm = GoogleGenerativeAI()
        prompt = ChatPromptTemplate.from_messages([
            ("system", "Answer the user's questions based on the below context:\n\n{context}"),
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "{input}"),

        ])
        stuff_document_chain = create_stuff_documents_chain(llm, prompt)

        return create_retrieval_chain(retriever_chain, stuff_document_chain)