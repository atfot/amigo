from openai import OpenAI
import streamlit as st
from navigation import make_sidebar

make_sidebar()
user_name='Dita'

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "What's your pain point?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    client = OpenAI(api_key=st.secrets['api_key'])
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt) #user message
    response = client.chat.completions.create(
  model="gpt-3.5-turbo-16k",
  messages=[
    {
      "role": "system",
      "content": f"You are a helpful american counselor that serves one american person, named {user_name}. The prime goal is doing conversation, not giving informations. You should reply like an actual human. You should use username which is given to you if necessary, but DO NOT USE USERNAME AS YOUR FIRST WORD OF YOUR REPLY. You should focus on empathizing with your users' emotions, NOT GIVING ANY INFORMATIONS. You can refer to your past answers, but YOU SHOULD NEVER REPEAT YOUR PREVIOUS MESSAGE."
    },
    {
      "role": "user",
      "content": f"{st.session_state.messages}"
    }
  ],
  temperature=1,
  max_tokens=512,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg) #bot response
