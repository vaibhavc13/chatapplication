import streamlit as st
import db_service as db
from ai_service import AIService
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page Config
st.set_page_config(page_title="GrokChatX", page_icon="🤖", layout="wide")

# Initialize DB
db.init_db()
ai_service = AIService()

# Session State Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []
if "current_conversation_id" not in st.session_state:
    st.session_state.current_conversation_id = None
if "api_keys" not in st.session_state:
    # Load from environment variables if available
    st.session_state.api_keys = {
        "grok": os.getenv("GROQ_API_KEY", "")
    }

# Sidebar
with st.sidebar:
    st.title("GrokChatX")
    
    # New Chat Button
    if st.button("New Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.current_conversation_id = None
        st.rerun()
    
    st.divider()
    
    # History
    st.subheader("History")
    conversations = db.get_conversations()
    for conv in conversations:
        if st.button(conv["title"], key=f"conv_{conv['id']}", use_container_width=True):
            st.session_state.current_conversation_id = conv["id"]
            st.session_state.messages = db.get_messages(conv["id"])
            st.rerun()
            
    st.divider()
    
    # Settings
    st.subheader("Settings")
    selected_provider = st.selectbox(
        "AI Provider",
        ["grok"],
        index=0
    )

# Main Chat Interface
st.header("GrokChatX")

# Display Messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
        if "provider" in msg and msg["provider"]:
            st.caption(f"Used: {msg['provider']}")

# Chat Input
if prompt := st.chat_input("Type your message..."):
    # Add User Message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # Create conversation if new
    if not st.session_state.current_conversation_id:
        title = prompt[:30] + "..."
        conv_id = db.create_conversation(title)
        st.session_state.current_conversation_id = conv_id
    
    # Save to DB
    db.add_message(st.session_state.current_conversation_id, "user", prompt)
    
    # Get AI Response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Format messages for API
                api_messages = []
                for msg in st.session_state.messages:
                    api_messages.append({
                        "role": msg.get("role", "user"),
                        "content": msg.get("content", "")
                    })
                
                result = ai_service.route_request(
                    api_messages, 
                    provider=selected_provider,
                    api_keys=st.session_state.api_keys
                )
                response_text = result["response"]
                provider_used = result["provider"]
                
                st.write(response_text)
                st.caption(f"Used: {provider_used}")
                
                # Add Assistant Message to State & DB
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": response_text,
                    "provider": provider_used
                })
                db.add_message(
                    st.session_state.current_conversation_id, 
                    "assistant", 
                    response_text, 
                    provider_used
                )
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
