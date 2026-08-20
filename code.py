import streamlit as st

name = st.text_input("What was your Username?")
subs = st.text_input("How many Subscribers did you have?")
joined = st.text_input("When did you join?")
final_activity = st.text_input("When did you stop playing?")
submit = st.button("Generate Card")

if submit:
    st.markdown(f"""
    <style>
        .stApp {{
            background-color: black;
            text-align: center;
        }}
        .card {{
            color: white;
        }}
        .card h1 {{
            color: orange;
        }}
    </style>

    <div class="card">
        <h1>Rec Room Final Report Card</h1>
        <h2>@{name}</h2>

        <h3>Player Since:</h3>
        <p>{joined}</p>

        <h3>Final Activity:</h3>
        <p>{final_activity}</p>

        <h3>Subscribers:</h3>
        <p>{subs}</p>
    </div>
    """, unsafe_allow_html=True)
