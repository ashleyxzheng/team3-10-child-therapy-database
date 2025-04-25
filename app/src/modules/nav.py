# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st


#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")


def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")


#### ------------------------ Examples for Role of pol_strat_advisor ------------------------
def PolStratAdvHomeNav():
    st.sidebar.page_link(
        "pages/00_Pol_Strat_Home.py", label="Political Strategist Home", icon="👤"
    )


def WorldBankVizNav():
    st.sidebar.page_link(
        "pages/01_World_Bank_Viz.py", label="World Bank Visualization", icon="🏦"
    )


def MapDemoNav():
    st.sidebar.page_link("pages/02_Map_Demo.py", label="Map Demonstration", icon="🗺️")


## ------------------------ Examples for Role of usaid_worker ------------------------
def ApiTestNav():
    st.sidebar.page_link("pages/12_API_Test.py", label="Test the API", icon="🛜")


def PredictionNav():
    st.sidebar.page_link(
        "pages/11_Prediction.py", label="Regression Prediction", icon="📈"
    )


def ClassificationNav():
    st.sidebar.page_link(
        "pages/13_Classification.py", label="Classification Demo", icon="🌺"
    )


#### ------------------------ System Admin Role ------------------------
def AdminPageNav():
    st.sidebar.page_link("pages/20_Admin_Home.py", label="System Admin", icon="🖥️")
    st.sidebar.page_link(
        "pages/21_ML_Model_Mgmt.py", label="ML Model Management", icon="🏢"
    )


# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    Controls the links displayed in the left-side panel of the app.
    """
    st.sidebar.markdown("### Navigation")

    # Add navigation links based on user role
    if not st.session_state.get('authenticated', False):
        if show_home:
            st.sidebar.page_link("Home.py", label="Home")
        st.sidebar.page_link("pages/30_About.py", label="About")
    else:
        role = st.session_state.get('role', '')
        
        if role == 'therapist':
            st.sidebar.page_link("pages/10_Therapist_Home.py", label="Home")
            st.sidebar.page_link("pages/11_Patient_List.py", label="Patient List")
            st.sidebar.page_link("pages/12_Art_Therapy.py", label="Art Therapy")
        elif role == 'art_specialist':
            st.sidebar.page_link("pages/20_Specialist_Home.py", label="Home")
            st.sidebar.page_link("pages/21_Review_Art.py", label="Review Art")
        elif role == 'child':
            st.sidebar.page_link("pages/30_Child_Home.py", label="Home")
            st.sidebar.page_link("pages/31_Art_Canvas.py", label="Art Canvas")
        elif role == 'guardian':
            st.sidebar.page_link("pages/40_Guardian_Home.py", label="Home")
            st.sidebar.page_link("pages/41_Child_Progress.py", label="Child Progress")
        
        st.sidebar.page_link("Home.py", label="Logout")
        st.sidebar.page_link("pages/30_About.py", label="About")
