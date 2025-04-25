import streamlit as st
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About Child Therapy Management System")

st.markdown(
    """
    ## Overview
    The Child Therapy Management System is a comprehensive platform designed to facilitate art therapy sessions 
    for children with chronic diseases. Our system connects therapists, art therapy specialists, children, and 
    their guardians in a supportive digital environment. An online platform designed to train pediatric psychologists 
    in using art therapy to support children with chronic illnesses. The platform features interactive modules and
    virtual patients.


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


    ## Art Therapy Forms: 

    1. Painting
    Painting is a popular option for art therapy. It allows the individual to express themselves creatively and experiment with color and texture. Painting can help to decrease anxiety and improve mood. Individuals can use various painting techniques, like finger painting, acrylics, or watercolors to create art.

    2. Carving
    Carving is a great option for individuals who want to work with a tangible and durable medium. Carving can include:
    - Woodworking
    - Stone carving
    - Sculpting using items like clay or wax
    This type of art therapy can help individuals to focus and destress while also providing a sense of accomplishment as they see their creations come to life.

    3. Sculpting
    Sculpting, like carving, can be done using various mediums. It involves creating three-dimensional pieces that can be tactile, allowing individuals to engage their sense of touch. Sculpting can help provide a sense of control and accomplishment, especially for individuals who are feeling overwhelmed.

    4. Using Textiles
    Textile art includes any kind of handicrafts, such as knitting, crocheting, and sewing. This form of art therapy is ideal for individuals who like working with their hands and who enjoy precision and detail-oriented work. Textile art can decrease anxiety and depression and foster a sense of accomplishment as individuals create functional or decorative pieces.

    5. Drawing
    Drawing is another popular option for art therapy. It involves using pens, pencils, or markers to create two-dimensional pieces. Drawing can help to reduce anxiety and provide a sense of control as individuals create something for themselves. Drawing can be used to symbolically represent something or create something more abstract that evokes a feeling.
    """
)

# Sample data with image URLs
data = {
    "Name": ["Painting", "Carving", "Sculpting"],
    "Age": ["Painting is a popular option for art therapy. It allows the individual to express themselves creatively and experiment with color and texture. Painting can help to decrease anxiety and improve mood. Individuals can use various painting techniques, like finger painting, acrylics, or watercolors to create art.", "Carving is a great option for individuals who want to work with a tangible and durable medium. Carving can include: woodworking, stone carving, sculpting using items like clay or wax. This type of art therapy can help individuals to focus and destress while also providing a sense of accomplishment as they see their creations come to life.", "Sculpting, like carving, can be done using various mediums. It involves creating three-dimensional pieces that can be tactile, allowing individuals to engage their sense of touch.", "Sculpting can help provide a sense of control and accomplishment, especially for individuals who are feeling overwhelmed."],
    "Image": [
        "https://webstockreview.net/images/draw-clipart.jpg",
        "https://static.vecteezy.com/system/resources/previews/019/470/509/non_2x/illustration-wood-carving-chisel-isolated-on-white-background-carpentry-hand-tools-with-wooden-handle-free-vector.jpg",
        "https://clipart-library.com/2023/girl-does-clay-sculpting_698371-2.jpg"
    ]
}

df = pd.DataFrame(data)

st.title("Table with Images")

# Loop to create a pseudo-table
for index, row in df.iterrows():
    cols = st.columns([1, 1, 2])
    cols[0].write(row["Name"])
    cols[1].write(row["Age"])
    cols[2].image(row["Image"], width=80)

# Add a section for contact or support if needed
st.sidebar.markdown("### Need Help?")
st.sidebar.info(
    """
    For support or questions, please contact:
    - System Administrator
    - Technical Support Team
    """
)
