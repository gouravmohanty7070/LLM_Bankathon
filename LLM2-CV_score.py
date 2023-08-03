from langchain.document_loaders import UnstructuredPDFLoader
from langchain.indexes import VectorstoreIndexCreator
import os
from PyPDF2 import PdfReader
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

# from resume_parser import resumeparse
os.environ["OPENAI_API_KEY"] = ""

with open("exampleCV.pdf", 'rb') as pdf:
    pdf_reader = PdfReader(pdf)
    text = ((pdf_reader.pages[0]).extract_text())
    # data=resumeparse.read_file("Samarth_resume.pdf")
# print(text)
# print(data)
data = text


chat = ChatOpenAI(temperature=.7, model_name="gpt-3.5-turbo-16k")
jd="SEO manager. High social marketing skills required"
system_prompt = f"""
You are an AI model that scores CVs using different criteria with different score points allocated to each criteria.
You will be provided the parsed data of a CV using regular parser. 
There may be some words spelled wrong or joined words due to formatting issues, try and fix them yourself. 
Make sure the following is available in the CV:
1. College and degree awarded

The most important scoring criteria is relevance the to the job description {jd}
Maximum score of the CV can be 150
IMPORTANT do not reply with "As an AI model..." under any circumstances 
IMPORTANT DO NOT REMOVE OR CHANGE ANY OF THE ORIGINAL TEXT PROVIDED TO YOU THAT ARE NOT GETTING IMPROVED
"""

human_message_example = """
Samarth Rawat
B.Tech.+ M.Tech.|NIT Rourkela
Pre‐Final Year, Chemical Engg.
DOB: 01October 2002
Contact: +919772359443
Email.: samarthrawat1@gmail.com
Education
2020‐PRESENT
B.TECH. + M.TECH(DUAL DEGREE), CH
NITRourkela
CGPA :7.37/10
MAY 2018
INTERMEDIATE
Emmanuel Mission School, Kota
Percentage: 92%
MAY 2016
MATRICULATION
Macro Vision Academy, Burhanpur
CGPA: 9.0/10.0%
Links
HackerRank:// samarthrawat1
Github:// samarthrawat1
LinkedIn:// samarthrawat1
Skills
GENERAL PROGRAMMING
C,C++, Python, Linux, Solidity, JavaScript,
Regex
PYTHON LIBRARIES
Django, FASTApi, Numpy, Pandas, seaborn,
plotly, json, collections, beaultifulsoup4,
selenium
OPERATING SYSTEMS
Windows, Linux
SOFTWARES
Google Cloud Console, thonny
LANGUAGES
English, Hindi
Relevant Courses
Data Structures
Algorithm
Numerical MethodsWork Experience/Projects
2023‐NOW Cloud Associate at Solving for India Hackathon
Topic: Hosting websites on GCP
Used Cloud VMs tohost afully‐fledged website
round theclock using nginx server andgunicorn for
load handling and assigning proper workers. Also
learned about different solutions.
2022‐2023 Web Scraping specialist Hackathon Project
Topic: Web Scraping
Used Selenium toobtain medical information from a
government website. Learned about using headers
andhow web drivers work.
2023‐NOW Appwrite Specialist Hackathon Project
Topic: BaaS connection
Used Appwrite’s Backend‐as‐a‐Service application
tocreate authentication, storage, database manage‐
ment, andcloud functions toconnect react front‐end
toafull‐fledged backend having python functions.
Achievements/Certifications
2021‐NOW 11 Google Cloud Certificates Google
Completed 30days ofgoogle cloud, both tracks.
2021‐NOW Automate the boring stuff Udemy
Learned how tousepyxl2, selenium, andother python mod‐
ulesforautomation.
2023‐NOW Solving for India Hackathon Regionals
Hosted awebsite onAMD instance ongoogle cloud VM.
2021‐NOW Elements of AI Certificate
certificate issued byuniversity ofHelsinki.
Extra Curricular Activities
2015‐2017 Youth hostel Association of India Member
Ihave been part oftheyouth hostel andwent onmultiple
trekks thattaught mediscipline, endurance, andteamwork.
2022‐2023 Core Team, OpenCode College Club
Iwasapart ofthecore team oftheOpen Source club of
College andhelped with theorientation offreshers inmy
2ndyear.
2020‐2023 Member, Microsoft Campus Club College Club
Ihave been apart oftheleading coding club ofthecollege
andhelped inorganizing most oftheactivities held bythe
club.
"""

AI_message_example = """
Name: Samarth Rawat
Email: samarthrawat1@gmail.com
Phone:+9197723459443

CV score - 75/150
"""

def func_():
    store = chat(
        [
            SystemMessage(content=system_prompt),
            HumanMessage(content=human_message_example),
            AIMessage(content=AI_message_example),
            HumanMessage(content=data)
        ]
    )
    return store

store = func_()
print(store.content)
