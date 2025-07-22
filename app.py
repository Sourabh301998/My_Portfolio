from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load Resume Insights
def load_resume_insights():
    with open('static/data/resume_insights.json') as f:
        return json.load(f)

# Load Project Details
def load_projects():
    with open('static/data/projects.json') as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resume')
def resume():
    insights = load_resume_insights()
    return render_template('resume.html', insights=insights)

@app.route('/projects')
def projects():
    projects = load_projects()
    return render_template('projects.html', projects=projects)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
