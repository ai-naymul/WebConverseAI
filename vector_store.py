from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


class VectorStore:
    def __init__(self) -> None:
        pass
    
    def get_vector_store_from_url(url):
        loader = WebBaseLoader(url)
        document = loader.load()

        text_splitter = RecursiveCharacterTextSplitter()
        document_chunks = text_splitter.split_documents(documents=document)

        vector_store = Chroma.from_documents(document_chunks, embedding=GoogleGenerativeAIEmbeddings(google_api_key=GOOGLE_API_KEY))
        return vector_store