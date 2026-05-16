import json, os, re, zipfile
from datetime import datetime

INPUT_FILE = "conversations.json"
OUTPUT_FOLDER = "conversation_markdown"
ZIP_FILE = "conversation_markdown.zip"

def safe_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "_", name)

def save_as_markdown():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        conversations = json.load(f)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    for convo in conversations:
        dt = datetime.fromtimestamp(convo.get("create_time", 0))
        date_str, year_str = dt.strftime("%Y-%m-%d"), dt.strftime("%Y")
        year_folder = os.path.join(OUTPUT_FOLDER, year_str)
        os.makedirs(year_folder, exist_ok=True)

        title = safe_filename(convo.get("title", "Untitled").strip())
        filename = f"{date_str} - {title}.md"
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
            elif "text" in c: parts.append(c["text"])
            text = "\n".join(parts).strip()
            if text: md_lines.append(f"**{role}:**\n\n{text}\n")

        with open(os.path.join(year_folder, filename), "w", encoding="utf-8") as md:
            md.write("\n---\n".join(md_lines))
    print(f"Saved to {OUTPUT_FOLDER}")

def zip_output():
    if os.path.exists(ZIP_FILE): os.remove(ZIP_FILE)
    with zipfile.ZipFile(ZIP_FILE, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(OUTPUT_FOLDER):
            for file in files:
                z.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), OUTPUT_FOLDER))
    print(f"Zipped to {ZIP_FILE}")

if __name__ == "__main__":
    save_as_markdown()
    zip_output()