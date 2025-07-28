import streamlit as st
from backend.main import main as gen

# create title
st.title("EmpowerEnergy Prototype")
st.write("This is the initial prototype for EmpowerEnergy -- enjoy!")

file = st.file_uploader("Upload File Here", type=["pdf"])
analyze_clicked = st.button("Analyze Document")
clear_clicked = st.button("Clear")

init_val = "Waiting to Analyze Document"

# add button to upload a pdf file
if file and analyze_clicked:
    analyze = gen(file)
    inv_feed = st.text_area(label="Investor Feedback", value=analyze[0], height=300)
    dev_feed = st.text_area(label="Developer Feedback", value=analyze[1], height=300)
else: 
    inv_feed = st.text_area(label="Investor Feedback", value=init_val, height=300)
    dev_feed = st.text_area(label="Developer Feedback", value=init_val, height=300)




