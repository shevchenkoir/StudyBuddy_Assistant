import streamlit as st
from core.chat_context import ConversationHistory

def get_session_history():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = ConversationHistory()
    return st.session_state.chat_history