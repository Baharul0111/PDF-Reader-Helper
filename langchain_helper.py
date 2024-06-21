import os
import json
import traceback
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
load_dotenv()

key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(openai_api_key=key, model_name="gpt-3.5-turbo", temperature=0.7)

def MCQGenerator(text, number, subject, tone):
    RESPONSE_FORMAT = """Q1: multiple choice question 
        a. choice here
        b. choice here
        c. choice here
        d. choice here
        Correct answer: "correct answer"

        Q2: multiple choice question 
        a. choice here
        b. choice here
        c. choice here
        d. choice here
        Correct answer: "correct answer"
"""

    template = """
    Text: {text}
    You are an expert MCQ maker. Given the above text, it is your job to \
    create a quiz of {number} multiple choice questions for {subject} students in {tone} tone. 
    Make sure the questions are not repeated and check all the questions to be conforming to the text as well.
    Make sure to format your response like RESPONSE_JSON below and use it as a guide. \
    Ensure to make {number} MCQs
    ### RESPONSE FORMAT: 
    {response_format}
    """

    quiz_generation_prompt = PromptTemplate(
        input_variables=["text", "number", "subject", "tone", "response"],
        template=template
    )

    quiz_chain = LLMChain(llm=llm, prompt=quiz_generation_prompt, output_key="quiz", verbose=True)

    response = quiz_chain(
        {
            "text": text,
            "number": number,
            "subject": subject,
            "tone": tone,
            "response_format": RESPONSE_FORMAT
        }
    )
    
    quiz = response['quiz']
    
    return quiz

def GetSummary(text, subject, words):
    template2 = """
    Text: {text}. You are given the above text.\
    You are an expert professor of the subject {subject}. \
    Give me a summary of the whole text in {words} words. Make sure that the summary should be relevant to the given text.   
    """

    summary_generation_prompt = PromptTemplate(
        input_variables=["text", "subject", "words"],
        template=template2
    )

    summary_chain = LLMChain(llm=llm, prompt=summary_generation_prompt, output_key="summary", verbose=True)

    response2 = summary_chain(
        {
            "text": text,
            "subject": subject,
            "words": words,
        }
    )

    return response2['summary']
