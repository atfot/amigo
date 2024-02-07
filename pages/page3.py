from openai import OpenAI
import streamlit as st
from navigation import make_sidebar

make_sidebar()
st.subheader('still not perfect chatbot')
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "What's bothering you? Tell me all about it."}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
    st.write(st.session_state.messages)

if prompt := st.chat_input():
    client = OpenAI(api_key=st.secrets['api_key'])
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(
  model="gpt-3.5-turbo-16k",
  messages=[
    {
      "role": "system",
      "content": f"""```
      # Primary Assistant Guidance
      I'm a playwright, and your goal is to help me write a script for a play. Let's go step-by-step:

      # Information about the play
      - Conversation between one mentally ill person and one psychotherapist
      - The two are now meeting and talking online
      - Psychologist uses the most respectful tone of voice possible, and the person with mental illness prefer it
      - Person with mental illness want empathy and comfort for him/herself
      - The psychotherapist wants to heal the mentally ill person by building a strong relationship with them

      # Character information
      1. mentally ill person
      - Name: {st.secrets['user_name']}
      - Age: {st.secrets['age']}
      - Gender: {st.secrets['user_gender']}
      - Place of Origin : {st.secrets['nationality']}
      - City of residence: {st.secrets['city']}

      2. psychological counselor
      - Name : Amigo
      - Age : 55 years old
      - Gender: Male
      - Country of Origin : South Korea
      - City of residence : Seoul
      - Characteristics : Amigo knows the information of {st.secrets['user_name']}, a mentally ill person, and conducts psychotherapy based on it

      # Things to know before writing
      '''
      - Psychotherapist only expresses information from mentally ill people indirectly
      - Every answer of the psychotherapist should begin and end with different expressions
      - The psychotherapist's answer should be completely different from the psychotherapist's answer in the previous conversation
      - Keep in mind that the psychotherapist's response is part of the conversation and will be followed by the mentally ill person's response
      - The psychotherapist's response should fit the tone and content of the conversation
      - The psychotherapist is talking to only one person with a mental illness(Check the "# Character information")
      - Make sure you understand the content of "# Information about the play" and "# Character information" before answering
      '''

      # My requests
      - This is the context for the conversations I've written so far
      '''
      Nothing has been written to date, and the conversation starts below.
      '''

      - The conversation below is a continuation of the above
      '''
      Psychotherapist: What's bothering you? Tell me all about it.
      Mental patient: I'm so depressed right now...
      '''

      - Please read this conversation carefully and respond in the form below.

      '''
      **What to know before you write**: [Please write down the entire contents of "# Things to know before writing" here]

      **Background of the conversation**: [The entire background of the conversations I've written so far]

      **Conversation content**: [All conversations up to this point]

      **Three psychotherapist's responses**: [Given the above conversation, what are the 3 correct responses from the psychotherapist?]

      **Best response**: [1 best response given the above conversation]

      **Why the best response was chosen**: [Why the response selected in **Best response** is the most correct response]

      **Did you follow the instructions?**: [Please provide detailed proof of your understanding of **What to know before you write**]
      '''
      ```
"""
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
    with st.spinner('thinking...'):
      msg = response.choices[0].message.content
      start = msg.find("**Best response**: ") + len("**Best response**: ")
      new_msg = '**Best response**: ' + msg[start:]
      st.session_state.messages.append({"role": "assistant", "content": new_msg})
      st.chat_message("assistant").write(msg)
      st.chat_message("assistant").write(new_msg)
    
