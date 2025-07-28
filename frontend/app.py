import streamlit as st
from backend.main import main


# create title
st.title("EmpowerEnergy Prototype")
st.write("This is the initial prototype for EmpowerEnergy -- enjoy!")

analyze_clicked = st.button("Analyze Document")
inv_feed = st.empty()
dev_feed = st.empty()

clear_clicked = st.button("Clear")

# add button to upload a pdf file
file = st.file_uploader("Upload File Here", type=["pdf"])

if file and analyze_clicked:
    analyze = main(file)
    inv_feed.text_area(label="Investor Summary: ", value=analyze[0], height=50, disabled=True)
    dev_feed.text_area(label="Developer Feedback: ", value=analyze[1], height=50, disabled=True)

# clear text



