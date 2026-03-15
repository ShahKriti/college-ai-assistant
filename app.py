from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os
from nlp.nlp_engine import get_response

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/departments")
def departments():
    return render_template("departments.html")

@app.route("/academics")
def academics():
    return render_template("academics.html")

@app.route("/courses")
def courses():
    return render_template("courses.html")

@app.route("/admissions")
def admissions():
    return render_template("admissions.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


# ⭐ Chatbot Route
@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    reply = get_response(user_message)

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)