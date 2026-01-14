import os
from flask import Flask, render_template_string, request
from boltiotai import openai

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not set")

openai.api_key = OPENAI_API_KEY

app = Flask(__name__)


def generate_educational_content(course_title):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant"
            },
            {
                "role": "user",
                "content": (
                    f"Generate educational content for a course titled {course_title}. "
                    "Include course objective, sample syllabus, three measurable learning outcomes, "
                    "assessment methods, and recommended readings."
                )
            }
        ]
    )
    return response["choices"][0]["message"]["content"]


@app.route("/", methods=["GET", "POST"])
def home():
    output = ""

    if request.method == "POST":
        course_title = request.form["course_title"]
        try:
            output = generate_educational_content(course_title)
        except Exception:
            output = "Error generating content. Please try again later."

    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
    <title>Educational Content Generator</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container mt-4">
    <h2>Educational Content Generator</h2>

    <form method="POST">
        <input class="form-control mb-2" name="course_title"
               placeholder="Enter course title" required>
        <button class="btn btn-primary">Generate</button>
    </form>

    <pre class="mt-3" style="white-space: pre-wrap;">{{ output }}</pre>
</div>
</body>
</html>
""", output=output)


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)
