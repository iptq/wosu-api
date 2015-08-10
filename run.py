from flask import Flask
app = Flask(__name__)

@app.route("/")
def help_page():
    return "Hello, world!"
    
app.run(port=5000)