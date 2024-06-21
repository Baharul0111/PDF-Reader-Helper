import streamlit as st
import langchain_helper
import utils
import time

st.title("PDF READER HELPER 📁")

file = st.file_uploader("Choose a PDF file", type="pdf")

if file is not None:
    text = utils.read_file(file)

    option = st.sidebar.selectbox("Pick an option", ("Generate MCQ", "Get Summary"))

    if option == "Get Summary":
        subject = st.text_input("Enter the subject:")
        words = st.number_input("Enter the number of words for the summary:", min_value=10, max_value=100, step=10)
        
        if subject and words:
            with st.spinner('Generating summary...'):
                progress_bar = st.progress(0)
                for percent_complete in range(100):
                    time.sleep(0.01)
                    progress_bar.progress(percent_complete + 1)
                
                response1 = langchain_helper.GetSummary(text, subject, words)
                
            st.subheader("Summary")
            st.write(response1)
            
    elif option == "Generate MCQ":
        number = st.number_input("Enter the number of MCQs you want to generate: ", min_value=3, max_value=12, step=1)
        subject = st.text_input("Enter the subject: ")
        tone = st.selectbox("Select a tone: ", ("easy", "medium", "hard"))
        
        if number and subject and tone:
            with st.spinner('Generating MCQs...'):
                progress_bar = st.progress(0)
                for percent_complete in range(100):
                    time.sleep(0.01)
                    progress_bar.progress(percent_complete + 1)
                
                response2 = langchain_helper.MCQGenerator(text, number, subject, tone)
                
            st.subheader("Quiz")
            st.write(response2)
