import streamlit as st

profile = st.sidebar.selectbox("Select Profile", ["Eclipse", "saltnpepper"])

st.title("Rec Room Final Report Card")

if profile == "Eclipse":
    st.html("""
    <style>
    .card {
        background-color: white;
        color: black;
        padding: 30px;
        border-radius: 20px;
        text-align: center; /* Fixed typo */
        font-family: Arial, sans-serif;
    }

    .card h1 {
        color: #ff6b35;
    }

    .card h3 {
        margin-bottom: 5px; /* Fixed typo */
    }

    .card p {
        margin-top: 0;
    }
    </style>

    <div class="card">
    <h1>Rec Room Final Report Card</h1>
    <h2>Eclipse @Jscott09</h2>
    <h3>Player Since:</h3>
    <p>December 2022</p>
    <h3>Final Activity:</h3>
    <p>March 2026</p>
    <h3>Subscribers:</h3>
    <p>250</p>
    <h3>Rec Room Era:</h3>
    <p>2022-2026</p>
    <h3>Final Words:</h3>
    <p>"RIP Rec Room. I'll always miss this place."</p>
    </div>
""")

elif profile == "saltnpepper":
    st.html("""
    <style>
    .card {
        background-color: white;
        color: black;
        padding: 30px;
        border-radius: 20px;
        text-align: center; /* Fixed typo */
        font-family: Arial, sans-serif;
    }

    .card h1 {
        color: #ff6b35;
    }

    .card h3 {
        margin-bottom: 5px; /* Fixed typo */
    }

    .card p {
        margin-top: 0;
    }
    </style>

    <div class="card">
    <h1>Rec Room Final Report Card</h1>
    <h2>saltnpepper @salfofthepepper</h2>
    <h3>Player Since:</h3>
    <p>November 2024</p>
    <h3>Final Activity:</h3>
    <p>January 2025</p>
    <h3>Subscribers:</h3>
    <p>3</p>
    <h3>Rec Room Era:</h3>
    <p>2024-2025</p>
    </div>
""")
