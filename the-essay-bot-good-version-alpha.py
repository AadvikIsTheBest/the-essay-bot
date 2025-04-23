import streamlit as st
import random
from io import StringIO
from docx import Document

# --- Data ---
subjects = {
    "History": [
        "How the Civil Rights Movement changed America",
        "The causes and effects of World War I",
        "Ancient Rome's influence on modern society"
    ],
    "Science": [
        "The importance of renewable energy",
        "How ecosystems maintain balance",
        "The science behind climate change"
    ],
    "Literature": [
        "The theme of courage in classic literature",
        "Comparing heroes in mythology and fiction",
        "How stories help us understand ourselves"
    ],
    "Technology": [
        "The effects of social media on communication",
        "Artificial intelligence and the future of jobs",
        "The pros and cons of remote learning"
    ]
}

styles = ["Formal", "Informative", "Persuasive", "Narrative"]

# --- Functions ---
def suggest_topic(subject):
    return random.choice(subjects.get(subject, ["Try another subject. No suggestions available."]))

def build_detailed_outline(topic):
    return {
        "Introduction": f"Hook the reader, provide background on '{topic}', and present a strong thesis statement.",
        "Body Paragraph 1": "Point #1: Define or introduce your first key idea. Include a strong example.",
        "Body Paragraph 2": "Point #2: Develop a second idea, contrast or support the first point.",
        "Body Paragraph 3": "Point #3: Broaden your perspective or include counterpoints and responses.",
        "Conclusion": "Restate the thesis, summarize your arguments, and leave the reader with a final thought."
    }

def generate_paragraph(section, topic, style):
    templates = {
        "Introduction": f"{topic} is an important subject in today's world. In this essay, I will explore its significance, challenges, and future impact.",
        "Body Paragraph 1": f"To begin, one of the core issues regarding {topic} is its role in daily life. For instance...",
        "Body Paragraph 2": f"Another crucial aspect of {topic} involves... This demonstrates that...",
        "Body Paragraph 3": f"Additionally, we should consider alternative views on {topic}. Some believe..., while others think...",
        "Conclusion": f"In conclusion, {topic} affects many parts of our lives. Understanding it helps us make better decisions and plan for the future."
    }
    return templates.get(section, "")

def export_docx(essay_dict):
    doc = Document()
    for section, content in essay_dict.items():
        doc.add_heading(section, level=2)
        doc.add_paragraph(content)
    buffer = StringIO()
    doc.save("essay.docx")
    return "essay.docx"

# --- Streamlit App ---
st.set_page_config(page_title="Essay Genius AI", layout="centered")
st.title("🧠 Essay Genius AI")

st.markdown("Use this tool to generate essay ideas, outlines, and full drafts for school-level essays.")

subject = st.selectbox("Choose a subject:", list(subjects.keys()))
style = st.selectbox("Choose a writing style:", styles)
topic_choice = st.radio("How do you want to choose your topic?", ["Surprise me", "I have my own"])

if topic_choice == "Surprise me":
    topic = suggest_topic(subject)
else:
    topic = st.text_input("Enter your own topic:")

if topic:
    st.success(f"Chosen Topic: {topic}")

    st.subheader("📋 Essay Outline")
    outline = build_detailed_outline(topic)
    for section, detail in outline.items():
        st.markdown(f"**{section}:** {detail}")

    st.subheader("✍️ Full Draft")
    essay = {}
    for section in outline:
        content = generate_paragraph(section, topic, style)
        paragraph = st.text_area(f"{section}", value=content, height=150)
        essay[section] = paragraph

    st.subheader("📥 Export Essay")
    if st.button("Download as .docx"):
        filepath = export_docx(essay)
        with open(filepath, "rb") as f:
            st.download_button("Click to Download", f, file_name="essay.docx")

st.markdown("---")
st.caption("Created with ❤️ for students and teachers.")
