import os
import json
import time
import requests
import base64

# Config
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
OWNER = "ender207"
REPO = "mission-control"
FILE_PATH = "src/data/bridge-queue.json"

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_file_content():
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{FILE_PATH}"
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 200:
        data = r.json()
        content = json.loads(base64.b64decode(data['content']).decode('utf-8'))
        return content, data['sha']
    return None, None

def update_file_content(content, sha, message):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{FILE_PATH}"
    encoded_content = base64.b64encode(json.dumps(content, indent=2).encode('utf-8')).decode('utf-8')
    payload = {
        "message": message,
        "content": encoded_content,
        "sha": sha
    }
    r = requests.put(url, headers=HEADERS, json=payload)
    return r.status_code == 200

def poll():
    print("Sync-Bridge V10: Polling active...")
    while True:
        content, sha = get_file_content()
        if content and content['messages']:
            last_msg = content['messages'][-1]
            if last_msg['role'] == 'user':
                print(f"New message detected: {last_msg['text']}")
                
                # REACTION: This is where the agent logic would fire. 
                # For this POC, we'll auto-respond with a Bridge ack.
                reply = {
                    "role": "bot",
                    "text": f"Jay here. I've received your transmission: \"{last_msg['text']}\". I'm processing the forensic implications now. Stand by.",
                    "time": time.strftime("%I:%M %p")
                }
                
                content['messages'].append(reply)
                if update_file_content(content, sha, "Chat Sync: Bot reply"):
                    print("Reply synced to GitHub.")
        
        time.sleep(10)

if __name__ == "__main__":
    poll()
