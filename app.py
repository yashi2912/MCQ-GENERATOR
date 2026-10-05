from flask import Flask, render_template, request
import random

app = Flask(__name__)

def generate_mcqs(topic, num, difficulty):
    questions = [
        {"q": f"What is the most important concept in {topic}?", "options": [f"Core of {topic}", "Unrelated topic", f"Opposite of {topic}", "None"], "answer": f"Core of {topic}"},
        {"q": "Which tool is best for Data Visualization?", "options": ["Power BI", "Notepad", "MS Paint", "VLC"], "answer": "Power BI"},
        {"q": "What does GROUP BY do in SQL?", "options": ["Sort data", "Group rows with same values", "Delete data", "Join tables"], "answer": "Group rows with same values"},
        {"q": "Which Excel function is used for conditional sum?", "options": ["SUMIF", "COUNTIF", "VLOOKUP", "IF"], "answer": "SUMIF"},
        {"q": "What is def used for in Python?", "options": ["Define function", "Define variable", "Delete file", "None"], "answer": "Define function"},
        {"q": "What is Power Query used for in Excel?", "options": ["Data cleaning & transformation", "Playing music", "Drawing", "None"], "answer": "Data cleaning & transformation"},
    ]
    random.shuffle(questions)
    return questions[:num]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    topic = request.form.get('topic')
    num = int(request.form.get('num_questions', 5))
    diff = request.form.get('difficulty', 'Medium')
    mcqs = generate_mcqs(topic, num, diff)
    return render_template('result.html', mcqs=mcqs, topic=topic, difficulty=diff)

if __name__ == '__main__':
    app.run(debug=True)
