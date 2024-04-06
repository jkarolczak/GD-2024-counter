import os

import streamlit as st

PARTICIPANTS = os.getenv("PARTICIPANTS", "").split(",")

if __name__ == "__main__":
    original_title = '<h1 style="font-family: serif; color:white; font-size: 20px;"></h1>'
    st.markdown(original_title, unsafe_allow_html=True)

    background_image = """
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background-image: url("https://ligands.blob.core.windows.net/brainteaser/files/bg.png");
        background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
        background-position: center;  
        background-repeat: no-repeat;
    }
    </style>
    """

    st.markdown(background_image, unsafe_allow_html=True)

    input_style = """
    <style>
    header {
        visibility: hidden !important;
    }
    
    input[type="text"] {
        background-color: transparent;
        color: #a19eae;  // This changes the text color inside the input box
    }
    div[data-baseweb="base-input"] {
        background-color: transparent !important;
    }
    [data-testid="stAppViewContainer"] {
        background-color: transparent !important;
    }
    input {
        font-size: 90px !important;
        text-align: center;
    }
    </style>
    """
    st.markdown(input_style, unsafe_allow_html=True)

    n_participants = len(PARTICIPANTS)
    cols = st.columns(n_participants)
    st.session_state.scores = [0] * n_participants

    st.markdown("")
    st.markdown("")
    for col_idx, col in enumerate(cols):
        with col:
            st.markdown(f"# {PARTICIPANTS[col_idx]}")
            st.number_input("", value=st.session_state.scores[col_idx], key=f"score_{col_idx}")
