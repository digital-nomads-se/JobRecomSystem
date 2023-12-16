import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split

def load_data(file_path):
    df = pd.read_csv(file_path)
    df['skills'] = df['skills'].apply(lambda x: x.split(','))
    return df

def preprocess_data(df):
    mlb = MultiLabelBinarizer()
    X = mlb.fit_transform(df['skills'])
    y = df['job_title']
    return X, y, mlb

def split_data(X, y):
    return train_test_split(X, y, test_size=0.2, random_state=42)

def extract_skills(text):
    skills = []
    for line in text.split('\n'):
      if 'SKILLS :' in line:
        skills.extend([skill.strip() for skill in line.split(':')[1].split(',') if skill.strip()])
    return list(set(skills))

def transform_skills(skills, mlb):
    known_skills = set(skills).intersection(set(mlb.classes_))
    return mlb.transform([list(known_skills)])
