from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()

st.header("LLM Hackathon Problem Statement Generator")
llm =ChatGroq(
    model="llama-3.3-70b-versatile",temperature=1.2,max_tokens=1000
    
)

idea=st.selectbox("Select a domain for your hackathon project",["Healthcare","Education","Finance","Environment","Entertainment"])
level=st.selectbox("Select the difficulty level of the problem statement",["Beginner","Intermediate","Advanced"])
difficulty=st.selectbox("Select the type of problem statement you want",["Research","Implementation","Optimization"])

template=PromptTemplate(template="suggest me some good {difficulty} problem statements to make a hackathon project on {idea} for {level} level participants", input_variables=["difficulty","idea","level"],validate_template=True)




if st.button("Generate Problem Statements"):
    result = llm.invoke(template.format(difficulty=difficulty,idea=idea,level=level))

    st.write(result.content)


