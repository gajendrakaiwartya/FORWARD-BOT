import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Hello from Koyeb - Bot is running!"

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    # Use PORT from env, default to 8080 if not provided
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
