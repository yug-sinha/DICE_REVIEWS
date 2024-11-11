# Dice Dreams Review Classifier

This project is a web application that scrapes reviews from the Google Play Store for the "Dice Dreams" app, classifies them into categories, performs sentiment analysis, and displays the results on a web page (please set up your own SerpAPI key in the scrape_reviews.js file).

Due to my limited experience with AWS Amplify, I was'nt able to succesfully deploy the application. However, the application is now deployed partially with just its frontend and can be accessed via the following URL:
 - URL: https://main.d31wt9c9s96zr2.amplifyapp.com/
  - Username: segwise.yug
  - Password: yug8086


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

## Project Structure

```
dice_dreams/
│
├── model/
├── node_modules/
├── results/
├── venv/
├── classified_reviews.json
├── classify_reviews.py
├── download_nltk_data.py
├── fetch.json
├── index.html
├── package-lock.json
├── package.json
├── Procfile
├── requirements.txt
├── scrape_reviews.js
└── script.py
```

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

**Request:**
```sh
GET http://localhost:5000/
```

**Response:**
- **200 OK**
  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Dice Dreams Reviews</title>
  </head>
  <body>
      <h1>Welcome to Dice Dreams Reviews</h1>
  </body>
  </html>
  ```

### GET /classified-reviews

**Request:**
```sh
GET http://localhost:5000/classified-reviews
```

**Response:**
- **200 OK**
  ```json
  [
    {
      "name": "Great game!",
      "avatar": "No Avatar",
      "review_rating": 5,
      "review_likes": 10,
      "review_snippet": "I love this game, it's so much fun!",
      "review_date": "November 1, 2024",
      "category": "Praises",
      "sentiment": {
        "neg": 0.0,
        "neu": 0.5,
        "pos": 0.5,
        "compound": 0.8
      }
    },
    ...
  ]
  ```

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

## Cost Estimation

To estimate the cost of running this system in production 24x7 for 30 days with 5 queries a day, we can consider the following:

- **Hosting**: Using a service like Heroku or AWS, the cost can vary. For a basic setup:
  - **Heroku**: Free tier available, but for production, the Hobby Dyno costs $7/month.
  - **AWS**: EC2 t2.micro instance (free tier eligible) or around $8.50/month for a t3.micro instance.

- **API Usage**: SerpAPI charges $75/month after exhausting the free tier. Given 5 queries a day, this would be sufficient.

- **Total Estimated Cost**:
  - **Hosting**: $7 - $8.50/month
  - **API Usage**: $75/month
  - **Total**: $82 - $83.50/month

## License

This project is licensed under the MIT License.

## Credits

- **SerpAPI**: For providing the API to scrape Google Play Store reviews.
- **NLTK**: For sentiment analysis tools.
- **Luxon**: For date manipulation in JavaScript.
- **Flask**: For the web framework.
- **Postman**: For testing API requests and responses.
- **ChatGPT**: For assistance in generating parts of this README.

## Video Demonstration
https://github.com/user-attachments/assets/0b5cba2d-70b2-4ea5-a379-b0e10fe4163b


https://github.com/user-attachments/assets/1bfff606-b0ce-45de-aa56-0d6b68ab0989


---

Source: Conversation with Copilot, 11/6/2024
- Calculate Web App Development Cost On Your Own in 2024 - Monocubed. https://www.monocubed.com/blog/web-app-development-cost/.
- How Much Does Web Application Development Cost in 2025. https://www.technbrains.com/blog/web-application-development-cost/.
- Submitting Applications - Spark 3.5.3 Documentation - Apache Spark. https://spark.apache.org/docs/latest/submitting-applications.html.
- Spark Submit Command Explained with Examples. https://sparkbyexamples.com/spark/spark-submit-command/.
- Setting Up Your Submission Call: A 10-Step Checklist. https://blog.submittable.com/setting-up-your-submission-call-a-10-step-checklist/.
- Running Spark on Kubernetes - Spark 3.5.3 Documentation - Apache Spark. https://spark.apache.org/docs/latest/running-on-kubernetes.html.
- Create examples of request responses to illustrate API use cases. https://learning.postman.com/docs/sending-requests/response-data/examples/.
- REST API Tutorial – REST Client, REST Service, and API Calls Explained .... https://www.freecodecamp.org/news/rest-api-tutorial-rest-client-rest-service-and-api-calls-explained-with-code-examples/.
- Sample API requests - Microsoft Cloud for Retail. https://learn.microsoft.com/en-us/industry/retail/intelligent-recommendations/sample-api.
- Mastering API Responses: The Definitive Guide to JSON Formatting. https://apidog.com/blog/json-api-responses/.
- Sample API Requests | YouTube Data API | Google for Developers. https://developers.google.com/youtube/v3/sample_requests.
- undefined. https://official-joke-api.appspot.com/random_joke.
- undefined. https://bing.com/search?q=.

---
