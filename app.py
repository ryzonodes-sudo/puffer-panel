from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>PufferPanel Binder Working</h1>
    <p>Ubuntu 24.04 VPS Ready</p>
    <p>Docker Installed</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
