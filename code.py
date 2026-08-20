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
        box-shadow: 0 10px 25px rgba(0, 0, 0,0.1);
        border: 1px solid #eaeaea;
        border-radius: 20px;
        text-align: center;
        font-family: Arial, sans-serif;
    }

    .card h1 {
        color: #ff6b35;
    }

    .card h3 {
        margin-bottom: 5px;
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
        box-shadow: 0 10px 25px rgba(0, 0, 0,0.1);
        border: 1px solid #eaeaea;
        border-radius: 20px;
        text-align: center;
        font-family: Arial, sans-serif;
    }

    .card h1 {
        color: #ff6b35;
    }

    .card h3 {
        margin-bottom: 5px;
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
