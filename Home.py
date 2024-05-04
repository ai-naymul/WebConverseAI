import streamlit as st
from langchain_core.messages import AIMessage,HumanMessage

from vector_store import VectorStore
from retriever_chain import RetrieverChain

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')



vector = VectorStore

rtr_chain = RetrieverChain()


def get_response(user_input):
    rter = rtr_chain.get_context_retriever_chain(vector_store=st.session_state.vector_store)
    conversation_rag_chain = rtr_chain.get_conversational_rag_chain(rter)
    
    response = conversation_rag_chain.invoke({
        "chat_history": st.session_state.chat_history,
        "input": user_input
    })
    
    return response['answer']


st.set_page_config(page_title="WebConverseAI - Chat with Websites: An AI-Powered Conversational Interface")
st.title("Chat with Websites: An AI-Powered Conversational Interface")

st.subheader('Website URL')
text_input_container = st.empty()
website_url = text_input_container.text_input("Enter a website url")
# website_url = st.text_input('')
if website_url != "":
    text_input_container.empty()
    st.info(website_url)
if website_url:
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            AIMessage(content="Hello, I am a bot. How can I help you?"),
        ]
    if "vector_store" not in st.session_state:
        st.session_state.vector_store =  vector.get_vector_store_from_url(url=website_url)

    # user input
    user_query = st.chat_input("Type your message here...")
    if user_query is not None and user_query != "":
        response = get_response(user_query)
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        st.session_state.chat_history.append(AIMessage(content=response))
        
    
    # conversation
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)
