from pipeline.rag_chain import RAGChain
import streamlit as st
from constants import IMAGE_LINK

# Initialize the RAGChain pipeline
chain_obj = RAGChain()
rag_chain = chain_obj.get_chain()

# Set Streamlit page configuration for better appearance
st.set_page_config(
    page_title="Aurora Industry Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Sidebar for branding and instructions
with st.sidebar:
    st.image(IMAGE_LINK, use_container_width=True)
    st.markdown("""
    ## About Aurora
    Aurora is your industry assistant. Ask any question related to your documents and get instant, reliable answers.
    
    **How to use:**
    - Enter your question in the box below.
    - Click **Submit** to get an answer.
    - If the answer is not found, you'll get a polite response.
    """)

# Main title and header
st.title("🤖 Aurora Industry Chatbot")
st.subheader("Welcome to Aurora. Good Life Ahead!")

# Add a text input box for user queries
user_input = st.text_input(
    "Enter your question here:",
    placeholder="Type your industry-related question..."
)

# Add a submit button and display the answer in a styled box
if st.button('Submit', use_container_width=True) and user_input:
    # Invoke the RAG chain to get the answer
    response = rag_chain.invoke(user_input)
    st.markdown(
        f"""
        <div style='background-color: #212121; padding: 1.5em; border-radius: 10px; margin-top: 1em;'>
            <strong>Answer:</strong><br>{response}
        </div>
        """,
        unsafe_allow_html=True
    )