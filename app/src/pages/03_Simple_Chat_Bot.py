import streamlit as st

# Must be the first Streamlit command
st.set_page_config(page_title="Therapy Chat Simulator", page_icon="💭")

from modules.nav import SideBarLinks
import random
import time

SideBarLinks()

st.title("Therapy Chat Simulator 💭")

# Initialize chat history for different personas
if "current_persona" not in st.session_state:
    st.session_state.current_persona = "child"
if "messages" not in st.session_state:
    st.session_state.messages = []

# Persona selection
st.sidebar.markdown("### Select Chat Persona")
persona = st.sidebar.radio(
    "Who would you like to chat with?",
    ["Child 👶", "Supervisor 👨‍⚕️", "Guardian 👪", "Specialist 👩‍⚕️"],
    index=0,
    key="persona_selector"
)

# Map display names to internal names
persona_map = {
    "Child 👶": "child",
    "Supervisor 👨‍⚕️": "supervisor",
    "Guardian 👪": "guardian",
    "Specialist 👩‍⚕️": "specialist"
}

# Clear chat if persona changes
if st.session_state.current_persona != persona_map[persona]:
    st.session_state.messages = []
    st.session_state.current_persona = persona_map[persona]

# Display appropriate introduction based on persona
persona_intros = {
    "child": """
This chat simulates a child during art therapy sessions. The responses reflect common 
emotional expressions and behaviors of children dealing with chronic conditions.

Example questions:
- How are you feeling today?
- What would you like to draw?
- Tell me about your drawing
- What colors make you happy?
""",
    "supervisor": """
This chat simulates a therapy supervisor who oversees and guides therapy sessions.

Example questions:
- What do you think about this case?
- How should I approach this situation?
- Can you review my session notes?
- What techniques do you recommend?
""",
    "guardian": """
This chat simulates a guardian/parent of a child in therapy.

Example questions:
- How is my child progressing?
- What can we do at home?
- Are there any concerns?
- When is the next session?
""",
    "specialist": """
This chat simulates an art therapy specialist who can provide expert guidance.

Example questions:
- What techniques work best for trauma?
- How can I interpret these drawings?
- What materials do you recommend?
- Can you suggest new approaches?
"""
}

st.markdown(persona_intros[st.session_state.current_persona])

def get_response(prompt, persona):
    responses = {
        "child": {
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
            "default": [
                "Can you help me with my drawing?",
                "Sometimes it's hard to say how I feel...",
                "Will you draw something with me?",
                "I like coming to art therapy",
                "Can we use the sparkly markers today?"
            ]
        },
        "supervisor": {
            "case": [
                "Based on the case history, I'd recommend focusing on emotional expression through color choice.",
                "Have you considered incorporating family drawing sessions?",
                "The child's progress shows positive response to art therapy interventions.",
                "Let's discuss alternative approaches for managing anxiety during sessions."
            ],
            "technique": [
                "For this situation, guided imagery combined with art could be effective.",
                "Consider using the progressive disclosure technique in your next session.",
                "The mandala drawing exercise might help with focus and calm.",
                "Try incorporating storytelling with the artwork creation."
            ],
            "default": [
                "What specific challenges are you encountering in your sessions?",
                "How are you documenting the therapeutic progress?",
                "Let's schedule a detailed review of your cases next week.",
                "Have you noticed any patterns in the child's artwork?"
            ]
        },
        "guardian": {
            "progress": [
                "We've noticed positive changes in their emotional expression through art.",
                "They're becoming more comfortable sharing their feelings during sessions.",
                "The latest artwork shows increasing confidence and engagement.",
                "We're seeing good progress in their ability to process emotions."
            ],
            "home": [
                "Try setting up a quiet art corner at home for creative expression.",
                "Regular drawing sessions can help maintain progress between therapy.",
                "Encourage them to share stories about their artwork with you.",
                "Simple art supplies at home can provide emotional outlet when needed."
            ],
            "default": [
                "Would you like to schedule our next family session?",
                "How has their behavior been at home lately?",
                "We can discuss specific concerns you have about their progress.",
                "Let's talk about ways to support their therapy at home."
            ]
        },
        "specialist": {
            "technique": [
                "Color therapy can be particularly effective for processing trauma.",
                "Consider using the bilateral drawing technique for anxiety reduction.",
                "The squiggle technique often reveals underlying emotions effectively.",
                "Sand art can help with tactile sensory integration issues."
            ],
            "interpretation": [
                "The use of dark colors might indicate unprocessed emotions.",
                "Notice the spatial relationships in their family drawings.",
                "Repetitive patterns often suggest a need for control and stability.",
                "The size and placement of figures can reveal relationship dynamics."
            ],
            "default": [
                "What specific therapeutic goals are you working towards?",
                "Let's analyze the progression of their artwork over time.",
                "Have you tried incorporating mixed media techniques?",
                "We could explore alternative expressive art modalities."
            ]
        }
    }
    
    prompt_lower = prompt.lower()
    if persona == "child":
        if any(word in prompt_lower for word in ["feel", "feeling", "mood", "today"]):
            category = "feeling"
        elif any(word in prompt_lower for word in ["draw", "drawing", "picture", "art"]):
            category = "drawing"
        else:
            category = "default"
    elif persona == "supervisor":
        if any(word in prompt_lower for word in ["case", "situation", "review"]):
            category = "case"
        elif any(word in prompt_lower for word in ["technique", "approach", "method"]):
            category = "technique"
        else:
            category = "default"
    elif persona == "guardian":
        if any(word in prompt_lower for word in ["progress", "doing", "better"]):
            category = "progress"
        elif any(word in prompt_lower for word in ["home", "help", "support"]):
            category = "home"
        else:
            category = "default"
    elif persona == "specialist":
        if any(word in prompt_lower for word in ["technique", "method", "approach"]):
            category = "technique"
        elif any(word in prompt_lower for word in ["interpret", "meaning", "analysis"]):
            category = "interpretation"
        else:
            category = "default"
    
    return random.choice(responses[persona][category])

def response_generator(response, persona):
    # Different typing patterns for different personas
    delays = {
        "child": {"word_delay": 0.3, "thinking_prob": 0.3, "thinking_delay": 1.5},
        "supervisor": {"word_delay": 0.1, "thinking_prob": 0.1, "thinking_delay": 0.5},
        "guardian": {"word_delay": 0.2, "thinking_prob": 0.2, "thinking_delay": 1.0},
        "specialist": {"word_delay": 0.15, "thinking_prob": 0.15, "thinking_delay": 0.7}
    }
    
    words = response.split()
    for i, word in enumerate(words):
        if i > 0 and random.random() < delays[persona]["thinking_prob"]:
            time.sleep(delays[persona]["thinking_delay"])
        yield word + " "
        time.sleep(delays[persona]["word_delay"])

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar=message.get("avatar", None)):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input(f"Chat with {persona}..."):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get and display response
    response = get_response(prompt, st.session_state.current_persona)
    
    # Avatar mapping
    avatar_map = {
        "child": "👶",
        "supervisor": "👨‍⚕️",
        "guardian": "👪",
        "specialist": "👩‍⚕️"
    }
    
    # Display response
    with st.chat_message("assistant", avatar=avatar_map[st.session_state.current_persona]):
        response_placeholder = st.empty()
        full_response = ""
        
        for chunk in response_generator(response, st.session_state.current_persona):
            full_response += chunk
            response_placeholder.markdown(full_response + "▌")
        response_placeholder.markdown(full_response)

    # Add to chat history
    st.session_state.messages.append({
        "role": "assistant",
        "content": response,
        "avatar": avatar_map[st.session_state.current_persona]
    })
