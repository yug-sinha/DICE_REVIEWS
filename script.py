import subprocess
import os
import datetime
from flask import Flask, send_from_directory

def run_script(script_name):
    result = subprocess.run(['python', script_name], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {script_name}: {result.stderr}")
    else:
        print(f"Successfully ran {script_name}")

def run_node_script(script_name):
    result = subprocess.run(['node', script_name], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {script_name}: {result.stderr}")
    else:
        print(f"Successfully ran {script_name}")

def file_created_today(file_path):
    if os.path.exists(file_path):
        creation_time = os.path.getctime(file_path)
        creation_date = datetime.datetime.fromtimestamp(creation_time).date()
        print(f"fetch.json creation date: {creation_date}")
        return creation_date == datetime.datetime.today().date()
    return False

fetch_file = 'fetch.json'

# Check if fetch.json was created today
if file_created_today(fetch_file):
    print("The past week's reviews have already been extracted.")
else:
    print("Fetching new reviews...")
    # Step 1: Run scrape_reviews.js
    run_node_script('scrape_reviews.js')

# Step 2: Run classify_reviews.py
run_script('classify_reviews.py')

# Step 3: Launch the Flask web application
app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/classified-reviews')
def classified_reviews():
    return send_from_directory('.', 'classified_reviews.json')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('.', 'favicon.ico')

if __name__ == '__main__':
    print("Starting Flask web application...")
    app.run(debug=True, use_reloader=False)
    print("Web application is running at: http://localhost:5000/")
