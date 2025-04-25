##################################################
# This is the main/entry-point file for the
# sample application for your project
##################################################

# Set up basic logging infrastructure
import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# import the main streamlit library as well
# as SideBarLinks function from src/modules folder
import streamlit as st
from modules.nav import SideBarLinks

# streamlit supports reguarl and wide layout (how the controls
# are organized/displayed on the screen).
st.set_page_config(layout = 'wide')

# Check if user is authenticated
if not st.session_state.get('authenticated', False):
    st.switch_page("Home.py")

# Use the SideBarLinks function
SideBarLinks()

# Page title and welcome message
st.title('Therapist Dashboard')
st.write(f"Welcome back, {st.session_state.get('first_name', 'Therapist')}!")

# Create a layout with two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("Quick Actions")
    
    # Patient Management
    st.markdown("### 🏥 Patient Management")
    if st.button("View Patient List", use_container_width=True):
        st.switch_page("pages/11_Patient_List.py")
    
    if st.button("Schedule New Session", use_container_width=True):
        st.switch_page("pages/12_Schedule_Session.py")
    
    # Art Therapy Tools
    st.markdown("### 🎨 Art Therapy")
    if st.button("Start Art Therapy Session", use_container_width=True):
        st.switch_page("pages/12_Art_Therapy.py")
    
    if st.button("View Art Gallery", use_container_width=True):
        st.switch_page("pages/13_Art_Gallery.py")

with col2:
    # Recent Activity
    st.markdown("### 📋 Recent Activity")
    st.info("""
    - Last session: Art therapy with John (2 hours ago)
    - New artwork submitted by Sarah
    - Upcoming session with Mike at 3 PM
    """)
    
    # Quick Stats
    st.markdown("### 📊 Statistics")
    st.success("""
    - Active Patients: 12
    - Sessions This Week: 8
    - Pending Reviews: 3
    - Art Pieces Created: 45
    """)

# Bottom section for announcements or important notes
st.markdown("---")
st.markdown("### 📢 Announcements")
st.warning("""
- New art therapy techniques workshop next week
- Remember to submit session reports within 24 hours
- Updated privacy guidelines available in the documentation
""")