import streamlit as st

st.title("はじめてのStreamlit")

name = st.text_input("お名前を入力してください")

if st.button("あいさつする"):
    if name == "":
        st.write("名前が入力されていません")
    else:
        st.write(f"こんにちは、{name}さん！")