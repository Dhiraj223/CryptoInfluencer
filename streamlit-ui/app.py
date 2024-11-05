import streamlit as st
from cryptinfluencer import get_llm_response, setup_pinecone, filter_pinecone, VectorStore

def CryticAgent(username, user_query):
    chunks = [{"text": user_query}]
    vectorstore = VectorStore()
    vectorstore.add_texts(chunks=chunks, user_id=username)
    vectors = vectorstore.vectors
    index_name = "cryptostore"
    index = setup_pinecone(index_name=index_name, vectors=vectors)
    previous_interactions = filter_pinecone(index=index, user_id=username)
    response = get_llm_response(memory=previous_interactions, user_query=user_query)
    return response

# Page configuration
st.set_page_config(
    page_title="CryptoWhiz Chat",
    page_icon=":moneybag:",
    layout="wide"
)

# Apply custom CSS with improved color contrast
st.markdown("""
    <style>
    .user-message {
        background-color: #1E88E5;
        color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .bot-message {
        background-color: #424242;
        color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .user-message strong, .bot-message strong {
        color: #FFFFFF;
    }
    .stTextInput>div>div>input {
        color: white !important;
    }
    textarea {
        color: white !important;
    }
    div[data-baseweb="input"] {
        background-color: white !important;
    }
    div[data-baseweb="input"] input {
        color: #000000 !important;
    }
    .stButton>button {
        background-color: #1E88E5;
        color: white;
    }
    .stButton>button:hover {
        background-color: #1976D2;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state variables
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Sidebar
with st.sidebar:
    st.title("CryptoWhiz Chat")
    username = st.text_input("Enter your Username:", key="username")
    if username:
        st.write(f"Welcome to CryptoWhiz, {username}! How can I help you today?")
    
    # Add a clear chat button in sidebar
    if st.button("Clear Chat History"):
        st.session_state.chat_history = []
        st.rerun()

# Main chat interface
st.title("Chat with CryptoWhiz")

# Display chat history
for chat in st.session_state.chat_history:
    with st.container():
        st.markdown(f'<div class="user-message"><strong>{username}:</strong> {chat["user"]}</div>', 
                   unsafe_allow_html=True)
        st.markdown(f'<div class="bot-message"><strong>CryptoWhiz:</strong> {chat["crypto_whiz"]}</div>', 
                   unsafe_allow_html=True)

# Create a form for the chat input
with st.form(key="chat_form", clear_on_submit=True):
    user_query = st.text_input(
        "Enter your query:",
        key="user_query_input",
        placeholder="Type your message here...",
        label_visibility="collapsed"
    )
    submit_button = st.form_submit_button("Send")

# Handle form submission
if submit_button and user_query:
    if user_query.lower() == "quit":
        st.write(f"Thank you for using our service, {username}. Have a great day!")
    else:
        # Get response from CryticAgent
        with st.spinner("CryptoWhiz is thinking..."):
            response = CryticAgent(username=username, user_query=user_query)
        
        # Store the interaction in chat history
        st.session_state.chat_history.append({
            "user": user_query,
            "crypto_whiz": response
        })
        
        # Rerun to update the chat display
        st.rerun()

# Add a warning if username is not provided
if not username:
    st.warning("Please enter a username in the sidebar to start chatting.")