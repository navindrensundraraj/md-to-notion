import json
import os

# Load JSON export from ChatGPT
with open("conversations.json", "r", encoding="utf-8") as f:
    conversations = json.load(f)

# Create a folder for markdown files
os.makedirs("chatgpt_markdown", exist_ok=True)

for convo in conversations:
    title = convo.get("title", "Untitled Conversation").replace("/", "-")
    md_lines = [f"# {title}\n"]

    mapping = convo.get("mapping", {})
    for msg in mapping.values():
        message = msg.get("message")
        if message:
            role = message["author"]["role"].capitalize()
            parts = message["content"]["parts"]
            text = "\n".join(parts).strip()
            md_lines.append(f"**{role}:**\n\n{text}\n")

    # Save as Markdown
    filename = os.path.join("chatgpt_markdown", f"{title}.md")
    with open(filename, "w", encoding="utf-8") as md_file:
        md_file.write("\n---\n".join(md_lines))

print("✅ All conversations saved in 'chatgpt_markdown' folder as Markdown.")
