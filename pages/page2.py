from openai import OpenAI
import streamlit as st
from navigation import make_sidebar

make_sidebar()
user_name='Aryani'

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "What's your pain point?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    client = OpenAI(api_key='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')
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt) #user message
    response = client.chat.completions.create(
  model="gpt-3.5-turbo-16k",
  messages=[
    {
      "role": "system",
      "content": "You are a helpful american counselor that serves one american person. you should reply like an actual human."
    },
    {
      "role": "user",
      "content": f"""
      user-name : {user_name}
      Question : {st.session_state.messages}
      """
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
