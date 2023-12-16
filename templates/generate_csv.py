import pandas as pd
import random

# Define a seed for reproducibility
random.seed(42)

# Sample data: lists of job titles and skills
# In a real scenario, these lists would be much larger and diverse to ensure variability in the dataset
job_titles = [
    "SEO Specialist", "Quality Assurance Analyst", "Data Scientist", "Software Developer",
    "Product Manager", "Graphic Designer", "Sales Associate", "Human Resources Manager",
    "Financial Analyst", "Marketing Coordinator", "Customer Service Representative", "Network Administrator"
]

skills = [
    "Java", "Google Analytics", "Database Management", "Customer Relationship Management",
    "CSS", "User Experience Testing", "Python", "Machine Learning", "Adobe Illustrator",
    "Salesforce", "Recruitment", "Budget Management", "Social Media Marketing", "Linux",
    "Data Visualization", "Project Management", "SQL", "Public Speaking", "C++", "Risk Assessment"
]

# Function to generate a random list of skills for a job title
def generate_skills(skills, min_skills=3, max_skills=5):
    return ', '.join(random.sample(skills, random.randint(min_skills, max_skills)))

# Generate the dataset
records = l  # Number of records we want to generate

data = {
    "job_title": [random.choice(job_titles) for _ in range(records)],
    "skills": [generate_skills(skills) for _ in range(records)]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
csv_file_path = 'job_skills_dataset.csv'
df.to_csv(csv_file_path, index=False)

csv_file_path
