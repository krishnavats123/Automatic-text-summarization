from flask import Flask, render_template, request
from summarizer import summarize_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    error = None
    if request.method == "POST":
        input_text = request.form.get("text", "").strip()
        if not input_text:
            error = "Please enter some text to summarize."
        else:
            try:
                summary = summarize_text(input_text)
            except Exception as e:
                error = f"An error occurred during summarization: {str(e)}"
    return render_template("index.html", summary=summary, error=error)

if __name__ == "__main__":
    app.run(debug=True)
