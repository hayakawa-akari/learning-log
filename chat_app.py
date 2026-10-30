import streamlit as st
from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

st.title("Claudeとチャット")

# 1. 履歴の入れ物がなければ、空で作る
if "messages" not in st.session_state:
    st.session_state.messages = []

# 2. これまでの履歴を吹き出しで表示
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

# 3. 新しい発言を受け取る
user_input = st.chat_input("メッセージを入力してください")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # 4. 履歴ごとClaudeに送る
    response = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=500,
        messages=st.session_state.messages,
    )
    reply = "".join(b.text for b in response.content if b.type == "text")

    # 5. 返事も履歴に足して、表示する
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)