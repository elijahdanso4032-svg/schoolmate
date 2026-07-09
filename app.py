"""
SchoolMate - AI-powered study platform for Ghana's GES curriculum
Created by Elijah Danso

This app uses Google's Gemini API for AI-powered study help.
Integration points for the AI logic are marked with TODO(Cyber) comments
for backend/API integration.
"""

import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key")

# TODO(Cyber): Replace with real Gemini API key in .env — see .env.example
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "DEMO_KEY_REPLACE_ME")

# GES curriculum subjects (sample — expand as needed)
SUBJECTS = [
    {"name": "Mathematics", "level": "JHS", "icon": "\U0001F4D0"},
    {"name": "English Language", "level": "JHS", "icon": "\U0001F4D6"},
    {"name": "Integrated Science", "level": "JHS", "icon": "\U0001F52C"},
    {"name": "Social Studies", "level": "JHS", "icon": "\U0001F30D"},
    {"name": "Physics", "level": "SHS", "icon": "\u269B\uFE0F"},
    {"name": "Chemistry", "level": "SHS", "icon": "\U0001F9EA"},
    {"name": "Biology", "level": "SHS", "icon": "\U0001F9EC"},
    {"name": "Economics", "level": "SHS", "icon": "\U0001F4CA"},
]


@app.route("/")
def home():
    return render_template("index.html", subjects=SUBJECTS)


@app.route("/subjects")
def subjects():
    return render_template("subjects.html", subjects=SUBJECTS)


@app.route("/ask", methods=["GET", "POST"])
def ask():
    """AI study assistant page."""
    answer = None
    if request.method == "POST":
        question = request.form.get("question", "").strip()
        if question:
            answer = get_ai_response(question)
    return render_template("ask.html", answer=answer)


def get_ai_response(question):
    """
    TODO(Cyber): Wire this up to the real Gemini API call.

    Example of what this should do:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(
            f"You are a helpful GES curriculum tutor. Answer this student's "
            f"question clearly and simply: {question}"
        )
        return response.text

    For now, this returns a placeholder so the frontend can be tested
    end-to-end before the real API key is wired in.
    """
    if GEMINI_API_KEY == "DEMO_KEY_REPLACE_ME":
        return (
            "[DEMO MODE] This is a placeholder response. "
            "Add a real Gemini API key to .env to enable live AI answers. "
            f"You asked: \"{question}\""
        )
    # TODO(Cyber): real API call goes here once key is set
    return "AI integration pending — see get_ai_response() in app.py"


@app.route("/api/ask", methods=["POST"])
def api_ask():
    """JSON API endpoint for the AI assistant (for frontend JS use)."""
    data = request.get_json(silent=True) or {}
    question = data.get("question", "").strip()
    if not question:
        return jsonify({"error": "No question provided"}), 400
    return jsonify({"answer": get_ai_response(question)})


if __name__ == "__main__":
    app.run(debug=True)
