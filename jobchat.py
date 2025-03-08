from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    """Get a response from Gemini."""
    response = chat.send_message(question, stream=True)
    return response

def is_profession_related(query):
    """Check if the query is related to professions or careers."""
    try:
        # Load keywords from joblist.txt
        with open("joblist.txt", "r") as file:
            keywords = [line.strip().lower() for line in file]
    except FileNotFoundError:
        st.error("The file 'joblist.txt' was not found. Please ensure it exists.")
        return False

    # Check if any keyword is in the query
    return any(keyword in query.lower() for keyword in keywords)

def get_profession_links(query):
    """Generate direct links to job search platforms for the given profession."""
    encoded_query = query.replace(" ", "+")
    links = {
        "LinkedIn": f"https://www.linkedin.com/jobs/search/?keywords={encoded_query}",
        "Naukri": f"https://www.naukri.com/{encoded_query}-jobs",
        "Indeed": f"https://www.indeed.com/q-{encoded_query}-jobs.html"
    }
    return links

# UI Enhancements
st.set_page_config(page_title="Job Chat", layout="wide")

# Theme Selection
theme = st.sidebar.radio("Select Theme:", ["Light Mode", "Dark Mode"], horizontal=True)

# Custom CSS for Themes
if theme == "Dark Mode":
    st.markdown("""
        <style>
            body { background-color: #2E2E2E; color: white; }
            .title { color: #FF5733; font-size: 36px; font-weight: bold; text-align: center; }
            .box { background-color: #333333; padding: 20px; border-radius: 10px; margin: 10px; color: white; }
            .box-title { font-size: 24px; border-bottom: 2px solid #FF5733; margin-bottom: 10px; }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
            body { background-color: #FFFFFF; color: black; }
            .title { color: #FF5733; font-size: 36px; font-weight: bold; text-align: center; }
            .box { background-color: #F9F9F9; padding: 20px; border-radius: 10px; margin: 10px; }
            .box-title { font-size: 24px; border-bottom: 2px solid #FF5733; margin-bottom: 10px; }
        </style>
    """, unsafe_allow_html=True)

# Header
st.markdown("<div class='title'>JOB CHAT</div>", unsafe_allow_html=True)

# Search Bar
search_query = st.text_input("Search jobs...", placeholder="Type a profession")
search_btn = st.button("Search")

# Layout: Three Columns
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.markdown("<div class='box-title'>Description</div>", unsafe_allow_html=True)
    if search_btn and search_query:
        if is_profession_related(search_query):
            response = get_gemini_response(f"Give a brief overview of the profession: {search_query}")
            for chunk in response:
                st.write(chunk.text)
        else:
            st.error("Please ask a profession-related question.")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.markdown("<div class='box-title'>Related Links</div>", unsafe_allow_html=True)
    if search_btn and search_query:
        links = get_profession_links(search_query)
        for platform, link in links.items():
            st.markdown(f"- [{platform}]({link})", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.markdown("<div class='box-title'>Search History</div>", unsafe_allow_html=True)
    if "search_history" not in st.session_state:
        st.session_state.search_history = []
    if search_btn and search_query:
        st.session_state.search_history.append(search_query)
    for history in st.session_state.search_history:
        st.markdown(f"- {history}")
    st.markdown("</div>", unsafe_allow_html=True)
