import streamlit as st
from modules.nav import SideBarLinks
import random
import time

SideBarLinks()

st.set_page_config(page_title="Child Therapy Chat", page_icon="👶")

st.title("Child Therapy Chat Simulator 👶")

st.markdown("""
This chat bot simulates responses from a child during an art therapy session. 
The responses are based on common emotional expressions and behaviors of children 
dealing with chronic conditions.

Example questions you can ask:
- How are you feeling today?
- What would you like to draw?
- Tell me about your drawing
- What colors make you happy?
- Do you want to try a different art activity?
""")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

def get_child_response(prompt):
    # Dictionary of themed responses
    responses = {
        "feeling": [
            "I feel a bit tired today, but drawing makes me happy!",
            "The hospital makes me scared sometimes...",
            "I'm excited to draw with you!",
            "I miss playing with my friends from school",
            "The medicine makes me feel weird sometimes"
        ],
        "drawing": [
            "I want to draw my family and my pet dog!",
            "Can I draw superheroes? They help people like the doctors help me",
            "I like drawing with bright colors, they make me feel better",
            "Maybe I can draw what I dream about?",
            "I want to draw the garden I see from my hospital window"
        ],
        "colors": [
            "Blue is my favorite! It's like the sky on a nice day",
            "Red makes me think of strong feelings",
            "Yellow makes me feel happy, like sunshine!",
            "Green reminds me of the park where I used to play",
            "Purple is magical, like in my favorite stories"
        ],
        "activities": [
            "Can we try finger painting?",
            "I like making collages with pictures from magazines",
            "Clay is fun to squish when I feel nervous",
            "Maybe we can draw a comic story together?",
            "I want to try watercolors today"
        ],
        "default": [
            "Can you help me with my drawing?",
            "Sometimes it's hard to say how I feel...",
            "Will you draw something with me?",
            "I like coming to art therapy",
            "Can we use the sparkly markers today?"
        ]
    }
    
    # Determine response category based on keywords
    prompt_lower = prompt.lower()
    if any(word in prompt_lower for word in ["feel", "feeling", "mood", "today"]):
        category = "feeling"
    elif any(word in prompt_lower for word in ["draw", "drawing", "picture", "art"]):
        category = "drawing"
    elif any(word in prompt_lower for word in ["color", "favourite", "like"]):
        category = "colors"
    elif any(word in prompt_lower for word in ["try", "activity", "different", "else"]):
        category = "activities"
    else:
        category = "default"
    
    response = random.choice(responses[category])
    return response

def response_generator(response):
    # Simulate a child typing with variable delays
    words = response.split()
    for i, word in enumerate(words):
        # Add some "thinking" pauses
        if i > 0 and random.random() < 0.2:
            time.sleep(1)  # Longer pause
        yield word + " "
        time.sleep(0.1 + random.random() * 0.2)  # Variable typing speed

# Display chat messages from history on rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask the child a question..."):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get and display child's response
    response = get_child_response(prompt)

    # Display child response in chat message container
    with st.chat_message("assistant", avatar="👶"):
        response_placeholder = st.empty()
        full_response = ""
        
        # Simulate child typing the response
        for chunk in response_generator(response):
            full_response += chunk
            response_placeholder.markdown(full_response + "▌")
        response_placeholder.markdown(full_response)

    # Add child's response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
