# Play Store Reviews Analyser

This project is a web application that scrapes reviews from the Google Play Store for any app(you just need to out the playstore APP ID), classifies them into categories, performs sentiment analysis, and displays the results on a web page (please set up your own SerpAPI key in the scrape_reviews.js file).

# Logic of the Web Application
1. **Implementation of `scrape_reviews.js`**:
   - The script checks if the latest reviews exist by verifying the creation date of the `fetch.json` file.
   - If `fetch.json` was created today, it assumes the latest reviews have already been fetched and does not run the scraper.
   - If `fetch.json` does not exist or was not created today, it runs the scraper to fetch the latest reviews from the Google Play Store and saves them to `fetch.json`.
   - This logic wont work when you will try to run this locally as it will presume that the fetch.json file was created today, because it would have been downloaded on the same day from the git repository so you will have to delete the current fetch.json file and then launch the application (MAKE SURE TO USE YOUR OWN API KEY).
   - Place your API key in scrape_reviews.js at this line:
   - ```sh
     const apiKey = 'YOUR_API_KEY_HERE';
     ```

2. **Implementation of `classify_reviews.py`**:
   - This script loads the reviews from `fetch.json`.
   - It classifies each review into categories such as Bugs, Complaints, Crashes, Praises, and Other based on keywords.
   - It performs sentiment analysis on each review using NLTK's VADER sentiment analyzer.
   - The classified reviews, along with their sentiment scores, are saved to `classified_reviews.json`.

3. **Launch of the HTML Front End**:
   - The `script.py` script orchestrates the execution of the above steps.
   - After running `scrape_reviews.js` and `classify_reviews.py`, it starts a Flask web server.
   - The Flask server serves the `index.html` file and provides an endpoint to access the classified reviews (`/classified-reviews`).

This sequence ensures that the application always has the latest reviews, classifies them appropriately, and makes the results accessible through a web interface.

# Video Demonstration: How to get SerpAPI key
https://youtu.be/-H9yN_jl4FQ?si=hWX34mclXiRuoC5K

## Table of Contents

- Installation
- Usage
- Project Structure
- Scripts
- Dependencies
- API Endpoints
- Setup and Run Locally
- Cost Estimation
- License
- Credits

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yug-sinha/DICE_REVIEWS.git
   cd DICE_REVIEWS
   ```
   - might throw a few errors, can be ignored

2. **Install Python dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Install Node.js dependencies:**
   ```sh
   npm install
   ```

## Usage

1. **Run the main script:**
   ```sh
   python script.py
   ```

2. **Access the web application:**
   Open your browser and go to `http://localhost:5000/`.

## Scripts

### scrape_reviews.js

This script scrapes reviews from the Google Play Store using the SerpAPI and saves them to `fetch.json`.

### classify_reviews.py

This script classifies the reviews into categories (Bugs, Complaints, Crashes, Praises, Other) and performs sentiment analysis using NLTK's VADER sentiment analyzer. The results are saved to `classified_reviews.json`.

### script.py

This script orchestrates the execution of `scrape_reviews.js` and `classify_reviews.py`, and then starts a Flask web server to serve the results.

## Dependencies

- **Python**: Ensure you have Python 3.6+ installed.
- **Node.js**: Ensure you have Node.js installed.
- **Flask**: For serving the web application.
- **NLTK**: For sentiment analysis.
- **SerpAPI**: For scraping reviews from the Google Play Store.
- **Luxon**: For date manipulation in JavaScript.

## API Endpoints

### GET /

## Setup and Run Locally

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yug-sinha/DICE_REVIEWS.git
   cd DICE_REVIEWS
   ```

2. **Install Python dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Install Node.js dependencies:**
   ```sh
   npm install
   ```

4. **Run the main script:**
   ```sh
   python script.py
   ```

5. **Access the web application:**
   Open your browser and go to `http://localhost:5000/`.

## License

This project is licensed under the MIT License.

## Video Demonstration
https://github.com/user-attachments/assets/1bfff606-b0ce-45de-aa56-0d6b68ab0989


---

Source: Conversation with Copilot, 11/6/2024

I have used ChatGPT, Microsofts Copilot AI, Blackbox AI, YouTube, SerpAPI, and StackOverFlows help to build this application

---
