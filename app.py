import streamlit as st
from openai import OpenAI


# Show title and description.
st.title("💬 Chatbot")
st.write(
   "This is a simple chatbot that uses OpenAI's GPT-3.5 model to generate responses. "
   "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
   "You can also learn how to build this app step by step by [following our tutorial](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)."
)
openai_api_key = st.secrets["api_key"] 
# Create an OpenAI client.
client = OpenAI(api_key=openai_api_key)
prompt = st.chat_input("What is up?")

with st.chat_message("user"):
   st.markdown(prompt)

# Generate a response using the OpenAI API.

stream = client.chat.completions.create(
        model="gpt-4o-mini",  # O el modelo que prefieras, como "gpt-3.5-turbo-16k"
        messages=[
            {"role": "system", "content": "You are an assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=800,
        temperature=0,
        #stream=True,
    )
#with st.chat_message("assistant"):
#   response = st.write_stream(stream)
