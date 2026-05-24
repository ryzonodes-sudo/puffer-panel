from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Binder is working!"

print("Binder started")
