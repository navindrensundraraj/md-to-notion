# 📋 Keep → Notion Converter

A simple web app to migrate your Google Keep notes to Notion — born out of a personal need to finally get all my notes organised in one place.

## 🧠 The Story

I had years of notes scattered across Google Keep and wanted to move everything into Notion. The problem? There was no clean way to do it. Google Keep lets you export your data as a ZIP containing `.json` files, but Notion can't just import that directly.

So I built this tool to bridge the gap — it takes your exported conversations/notes, converts them into structured Markdown files with proper frontmatter, organises them by year, and packages them into a zip ready to import into Notion.

## ✨ Features

- Upload your `conversations.json` export file
- Automatically converts notes to Markdown with YAML frontmatter
- Organises files by year into folders
- Downloads a zip file ready for Notion import
- No data stored — everything is processed in memory
- Free to use, open source

## 🚀 Try it Live

👉 [md-to-notion.streamlit.app](https://md-to-notion-6aitewqx32yrejp8rxltqn.streamlit.app)

No installation needed — just upload and download.

## 🛠️ How to Use

1. Go to [Google Takeout](https://takeout.google.com/) and export your Google Keep data
2. Locate the `conversations.json` file from the export
3. Upload it to the app
4. Click **Convert & Download ZIP**
5. Import the zip into Notion via **Settings → Import → Other**

## 💻 Run Locally

```bash
# Clone the repo
git clone https://github.com/teabag331/md-to-notion.git
cd md-to-notion

# Install dependencies
pip install streamlit

# Run the app
python -m streamlit run app.py
```

## 📁 Project Structure

```
md-to-notion/
├── app.py              # Streamlit web app
├── convert_to_md.py    # Core conversion script (CLI version)
├── requirements.txt    # Python dependencies
└── README.md
```

## 🧰 Built With

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/) — for the web interface
- Deployed on [Streamlit Cloud](https://streamlit.io/cloud) (free tier)

## 📄 License

MIT License — free to use, modify, and share.

---

*Built out of frustration and a messy notes app. Hope it helps someone else too.*
