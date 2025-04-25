import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks
import os
from PIL import Image

SideBarLinks()

st.write("# About Child Therapy Management System")

st.markdown(
    """
    ## Overview
    The Child Therapy Management System is a comprehensive platform designed to facilitate art therapy sessions 
    for children with chronic diseases. An online platform designed to train pediatric psychologists 
    in using art therapy to support children with chronic illnesses. The platform features interactive modules and
    virtual patients. Our system connects therapists, art therapy specialists, children, and their guardians in a 
    supportive digital environment. 


    ## Key Features
    - **Interactive Art Therapy**: Engaging art therapy modules designed for children with chronic conditions
    - **Multi-User Platform**: Dedicated interfaces for therapists, art specialists, children, and guardians
    - **Progress Tracking**: Monitor emotional expression and therapeutic progress
    - **Secure Environment**: Safe and private space for therapy sessions
    
    ## Our Mission
    To provide an accessible and effective platform that enhances the therapeutic experience for children 
    dealing with chronic diseases through art therapy, while fostering collaboration between healthcare 
    professionals and families.

    ## Technical Details
    - Frontend: Streamlit
    - Backend: Flask REST API
    - Database: MySQL
    - Deployment: Docker containerized architecture

    ## Team
    This project is developed as part of CS 3200 - Database Design.
    """
)

st.markdown("## Art Therapy Forms")

# Sample data for art therapy forms with base64 encoded placeholder images
data = {
    "Form": ["Painting 🎨", "Carving 🗿", "Sculpting 🏺", "Textiles 🧶", "Drawing ✏️"],
    "Description": [
        "Express creativity through colors and textures using various techniques like finger painting, acrylics, or watercolors.",
        "Work with tangible materials like wood or stone to create durable art pieces while focusing and destressing.",
        "Create three-dimensional pieces using clay or other materials to engage tactile senses and gain a sense of control.",
        "Engage in handicrafts like knitting, crocheting, and sewing for precision-oriented creative expression.",
        "Use pens, pencils, or markers to create two-dimensional pieces, helping reduce anxiety through visual expression."
    ],
    "Benefits": [
        "Decreases anxiety, improves mood, encourages self-expression",
        "Builds focus, provides sense of accomplishment, reduces stress",
        "Enhances tactile engagement, builds confidence, improves motor skills",
        "Reduces anxiety, builds patience, creates functional art",
        "Promotes emotional release, increases control, supports symbolic expression"
    ]
}

df = pd.DataFrame(data)

# Display art therapy forms in an organized layout with images
for index, row in df.iterrows():
    st.markdown(f"### {row['Form']}")
    
    # Create three columns: image, description, benefits
    col1, col2, col3 = st.columns([1, 1.5, 1.5])
    
    # Display a colored box with the emoji in the first column
    with col1:
        emoji = row['Form'].split()[-1]  # Get the emoji from the form name
        st.markdown(
            f"""
            <div style="
                background-color: #f0f2f6;
                border-radius: 10px;
                padding: 20px;
                text-align: center;
                font-size: 48px;
                height: 100px;
                display: flex;
                align-items: center;
                justify-content: center;
            ">
                {emoji}
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Display description and benefits in the other columns
    with col2:
        st.markdown("**Description:**")
        st.write(row["Description"])
    
    with col3:
        st.markdown("**Benefits:**")
        st.write(row["Benefits"])
    
    st.markdown("---")

# Updated contact section with team photos
st.sidebar.markdown("### Contact Us")
st.sidebar.info(
    """
    For support or questions, please contact:
    - Anushka Anand
    - Krish Kumar
    - Dawson French
    - Olivia Hill
    - Connor Tessaro
    - Ashley Zheng
    """
)
