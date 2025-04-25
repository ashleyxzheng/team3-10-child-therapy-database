import streamlit as st
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About Child Therapy Management System")

st.markdown(
    """
    ## Overview
    The Child Therapy Management System is a comprehensive platform designed to facilitate art therapy sessions 
    for children with chronic diseases. Our system connects therapists, art therapy specialists, children, and 
    their guardians in a supportive digital environment.

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

# Add a section for contact or support if needed
st.sidebar.markdown("### Need Help?")
st.sidebar.info(
    """
    For support or questions, please contact:
    - System Administrator
    - Technical Support Team
    """
)
