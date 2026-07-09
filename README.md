# SchoolMate — Lead Today

An AI-powered study platform built around Ghana's GES (Ghana Education Service) curriculum.

**Created by Elijah Danso**

## What's here

- Flask backend (`app.py`)
- Jinja2 templates with a Ghana-themed UI (national colors: red, gold, green, black)
- Responsive CSS (mobile-friendly)
- Gemini AI integration points, marked `TODO(Cyber)`, ready for backend/API work

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
```

Then open `.env` and add a real Gemini API key (get one free at
https://aistudio.google.com/apikey). Until you do, the app runs in **demo mode**
and returns placeholder AI answers so the frontend can be tested end-to-end.

Run it:
```bash
python app.py
```

Visit `http://localhost:5000`

## For Cyber (backend/API integration)

The only file that needs real AI wiring is `app.py`, inside the `get_ai_response()`
function. It currently returns a demo placeholder. Swap in the real Gemini call —
the example code is commented directly above it.

## Structure

```
schoolmate/
├── app.py                 # Flask app + routes
├── requirements.txt
├── .env.example            # Copy to .env, add real key (never commit .env)
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── subjects.html
│   └── ask.html
└── static/
    └── css/style.css       # Ghana-themed responsive styling
```
