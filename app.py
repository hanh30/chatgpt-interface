import streamlit as st
import os
from openai import OpenAI

# Set up OpenAI API key
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY")
    )


# st.title("OpenAI Chat Interface")

# Initialize session state for messages if it doesn't exist
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Function to get response from OpenAI API
def get_openai_response(user_input):
    try:
        # Use GPT-4 (or another model)
        # response = openai.ChatCompletion.create(
        #     model="gpt-4",
        #     messages=st.session_state["messages"]
        # )

        response = client.chat.completions.create(
            messages=st.session_state["messages"],
            model="gpt-4",
        )
        # return response["choices"][0]["message"]["content"]
        return response.choices[0].message.content
        # return response
    except Exception as e:
        return f"Error: {e}"

# Chat box for user input
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Your Message", key="input")
    submit_button = st.form_submit_button(label="Send")

# Display the conversation in chat-like format
if submit_button and user_input:
    # Append user message to the chat history
    st.session_state["messages"].append({"role": "user", "content": user_input})
    
    # Get the AI response
    ai_response = get_openai_response(user_input)
    
    # Append AI response to the chat history
    st.session_state["messages"].append({"role": "assistant", "content": ai_response})

# Display conversation
for message in st.session_state["messages"]:
    role = "You" if message["role"] == "user" else "AI"
    st.markdown(f"**{role}:** {message['content']}")

