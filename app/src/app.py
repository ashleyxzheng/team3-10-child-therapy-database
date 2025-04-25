import streamlit as st
import requests
import json
from PIL import Image
import os
from datetime import datetime

# Configure Streamlit page
st.set_page_config(
    page_title="Child Therapy Training Platform",
    page_icon="🎨",
    layout="wide"
)

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_role' not in st.session_state:
    st.session_state.user_role = None

def login():
    st.title("Child Therapy Training Platform")
    
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        
        if submitted:
            # TODO: Implement actual authentication with Flask backend
            # For now, using placeholder authentication
            if username and password:
                st.session_state.logged_in = True
                st.session_state.user_role = "therapist"
                st.rerun()

def show_virtual_child_profiles():
    st.header("Virtual Child Profiles")
    
    # Sample virtual child data
    children = [
        {
            "name": "Aarav Shah",
            "age": 8,
            "condition": "Juvenile diabetes",
            "art_preferences": ["Drawing", "Painting"],
            "emotional_traits": ["Imaginative", "Expressive", "Adventurous"]
        },
        {
            "name": "Dani Johnson",
            "age": 5,
            "condition": "Type 1 Diabetes",
            "art_preferences": ["Coloring", "Crafts"],
            "emotional_traits": ["Creative", "Sensitive"]
        }
    ]
    
    cols = st.columns(2)
    for idx, child in enumerate(children):
        with cols[idx]:
            st.subheader(child["name"])
            st.write(f"Age: {child['age']}")
            st.write(f"Condition: {child['condition']}")
            st.write("Art Preferences:")
            for pref in child["art_preferences"]:
                st.write(f"- {pref}")
            st.write("Emotional Traits:")
            for trait in child["emotional_traits"]:
                st.write(f"- {trait}")
            
            if st.button(f"Start Session with {child['name']}", key=f"child_{idx}"):
                st.session_state.selected_child = child
                st.rerun()

def show_therapy_session():
    st.header(f"Therapy Session with {st.session_state.selected_child['name']}")
    
    # Art therapy tools section
    st.subheader("Art Therapy Tools")
    tool = st.selectbox(
        "Select Art Tool",
        ["Drawing Canvas", "Color Palette", "Emotion Cards", "Story Prompts"]
    )
    
    # Session notes
    st.subheader("Session Notes")
    notes = st.text_area("Enter session notes...")
    
    # Emotional response tracking
    st.subheader("Emotional Response")
    emotions = st.multiselect(
        "Observed Emotions",
        ["Happy", "Sad", "Anxious", "Calm", "Frustrated", "Excited"]
    )
    
    if st.button("End Session"):
        # TODO: Save session data to database
        st.success("Session completed and saved!")
        st.session_state.pop('selected_child', None)
        st.rerun()

def main():
    if not st.session_state.logged_in:
        login()
    else:
        st.sidebar.title("Navigation")
        page = st.sidebar.radio(
            "Go to",
            ["Virtual Children", "Active Session", "Progress Reports"]
        )
        
        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()
        
        if page == "Virtual Children":
            if 'selected_child' not in st.session_state:
                show_virtual_child_profiles()
            else:
                show_therapy_session()
        elif page == "Active Session":
            if 'selected_child' in st.session_state:
                show_therapy_session()
            else:
                st.info("Please select a virtual child to start a session.")
        elif page == "Progress Reports":
            st.header("Progress Reports")
            st.info("Progress tracking and reporting coming soon!")

if __name__ == "__main__":
    main()
