import streamlit as st
import pandas as pd
import requests
import os

st.set_page_config(page_title="Mission Control", page_icon="🦞", layout="wide")

st.title("🚀 Mission Control: Jay Angeline Pipeline")

# Placeholder for real Sheets API logic (using current successful ADC auth)
def get_tracker_data():
    return pd.DataFrame([
        {"Task": "Magic Shapes Language Rewrite", "Status": "In Progress", "IP": "Cosmere"},
        {"Task": "Poppins Hub Refactor", "Status": "Backlog", "IP": "Mary Poppins"},
        {"Task": "Voice Interview (David)", "Status": "To Do", "IP": "System"},
        {"Task": "Expanse Faction Split", "Status": "Backlog", "IP": "The Expanse"},
    ])

# UI for communication directly in the app
st.sidebar.title("💬 Jay's Comms")
user_input = st.sidebar.text_input("Send message to Jay:")
if user_input:
    # In a full build, this would enqueue a task for the agent
    st.sidebar.success(f"Received: {user_input}")

st.sidebar.markdown("---")
st.sidebar.markdown("### Strategic Briefing")
if st.sidebar.button("Generate New Briefing"):
    st.sidebar.info("Briefing generation triggered...")

st.sidebar.markdown("---")
st.sidebar.markdown("### System Status: **Operational**")

df = get_tracker_data()
col1, col2, col3 = st.columns(3)

with col1:
    st.header("📋 To Do")
    for _, row in df[df['Status'] == 'To Do'].iterrows():
        st.info(f"**{row['Task']}**\n\n({row['IP']})")

with col2:
    st.header("⏳ In Progress")
    for _, row in df[df['Status'] == 'In Progress'].iterrows():
        st.warning(f"**{row['Task']}**\n\n({row['IP']})")

with col3:
    st.header("✅ Backlog / Finished")
    for _, row in df[df['Status'] == 'Backlog'].iterrows():
        st.success(f"**{row['Task']}**\n\n({row['IP']})")
