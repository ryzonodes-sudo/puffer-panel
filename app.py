from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Binder Working on Ubuntu 24"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
