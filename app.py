from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Ubuntu 24.04 Binder Running"

if __name__ == "__main__":
    os.system("cat /etc/os-release")
    app.run(host="0.0.0.0", port=7860)
