import streamlit as st
import json, os, re, zipfile, io
from datetime import datetime

st.set_page_config(page_title="Keep → Notion Converter", page_icon="📋")
st.title("📋 Keep → Notion Converter")
st.caption("Upload your export file and get a Notion-ready zip.")

def safe_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "_", name)

def convert(file_bytes):
    conversations = json.loads(file_bytes)
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as z:
        for convo in conversations:
            dt = datetime.fromtimestamp(convo.get("create_time", 0))
            date_str = dt.strftime("%Y-%m-%d")
            year_str = dt.strftime("%Y")

            title = safe_filename(convo.get("title", "Untitled").strip())
            filename = f"{year_str}/{date_str} - {title}.md"
            yaml_header = f"---\ntitle: \"{title}\"\ndate: {date_str}\ntags: [export, notes]\n---\n\n# {title}\n"
            md_lines = [yaml_header]

            for msg in convo.get("mapping", {}).values():
                m = msg.get("message")
                if not m: continue
                role = m["author"]["role"].capitalize()
                c = m.get("content", {})
                parts = []
                if "parts" in c:
                    for p in c["parts"]:
                        if isinstance(p, str): parts.append(p)
                        elif isinstance(p, dict): parts.append(p.get("text", json.dumps(p, indent=2)))
                        else: parts.append(str(p))
                elif "text" in c:
                    parts.append(c["text"])
                text = "\n".join(parts).strip()
                if text:
                    md_lines.append(f"**{role}:**\n\n{text}\n")

            z.writestr(filename, "\n---\n".join(md_lines))

    zip_buffer.seek(0)
    return zip_buffer

uploaded = st.file_uploader("Upload your conversations.json", type="json")

if uploaded:
    st.success(f"File uploaded: {uploaded.name}")
    if st.button("Convert & Download ZIP"):
        with st.spinner("Converting..."):
            zip_data = convert(uploaded.read())
        st.download_button(
            label="⬇️ Download ZIP",
            data=zip_data,
            file_name="notion_import.zip",
            mime="application/zip"
        )