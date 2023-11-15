from flask import Flask, render_template, request
from summarizer import Summarizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarizer():
    if request.method == 'POST':
        text = request.form['text']
        model = Summarizer()
        summary = model(text, ratio=0.2)  # You can adjust the ratio as needed
        return render_template('index.html', text=text, summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
