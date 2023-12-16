import os
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from pdfminer.high_level import extract_text
import pickle

app = Flask(__name__)

# Load the model and MultiLabelBinarizer
with open('models/model.pkl', 'rb') as file:
    model, mlb = pickle.load(file)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure UPLOAD_FOLDER exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def extract_skills(text):
    skills = []
    for line in text.split('\n'):
      if 'SKILLS :' in line:
        skills.extend([skill.strip() for skill in line.split(':')[1].split(',') if skill.strip()])
    return list(set(skills))

def transform_skills(skills, mlb):
    known_skills = set(skills).intersection(set(mlb.classes_))
    return mlb.transform([list(known_skills)])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', message='')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return render_template('index.html', message='No file part')
    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', message='No selected file')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        text = extract_text(file_path)
        skills = extract_skills(text)
        skills_array = transform_skills(skills, mlb)
        recommended_job = model.predict(skills_array)
        print(recommended_job)
        # Perform any additional processing and return the result
        return render_template('index.html', recommended_job=recommended_job, message='File successfully uploaded')
    return render_template('index.html', message='Invalid file type')

if __name__ == '__main__':
    app.run(debug=True)
