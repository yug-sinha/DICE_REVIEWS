import json
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Load the reviews from the JSON file
def load_reviews(filename='fetch.json'):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reviews = json.load(file)
        print(f"Loaded {len(reviews)} reviews from {filename}")
        return reviews
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file {filename} is not a valid JSON file.")
        return []

# Define the categories
categories = ['Bugs', 'Complaints', 'Crashes', 'Praises', 'Other']

# Function to classify reviews
def classify_review(review_text):
    review_text_lower = review_text.lower()
    
    # Define keywords for each category
    bugs_keywords = ['bug', 'glitch', 'issue', 'problem', 'error', 'fix']
    complaints_keywords = ['complaint', 'hate', 'dislike', 'bad', 'poor', 'annoying', 'frustrating']
    crashes_keywords = ['crash', 'crashing', 'freeze', 'hang', 'unresponsive']
    praises_keywords = ['love', 'great', 'excellent', 'awesome', 'good', 'amazing', 'fantastic', 'wonderful', 'perfect']

    # Check for each category in order of priority
    if any(keyword in review_text_lower for keyword in bugs_keywords):
        return 'Bugs'
    elif any(keyword in review_text_lower for keyword in crashes_keywords):
        return 'Crashes'
    elif any(keyword in review_text_lower for keyword in complaints_keywords):
        return 'Complaints'
    elif any(keyword in review_text_lower for keyword in praises_keywords):
        return 'Praises'
    else:
        return 'Other'

# Function to perform sentiment analysis
def sentiment_analysis(review_text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(review_text)
    return sentiment_scores

# Function to classify all reviews
def classify_reviews(reviews):
    for review in reviews:
        if 'review_snippet' in review:
            review_text = review['review_snippet']
            category = classify_review(review_text)
            sentiment = sentiment_analysis(review_text)
            review['category'] = category
            review['sentiment'] = sentiment
    return reviews

# Save the classified reviews to a new JSON file
def save_classified_reviews(reviews, filename='classified_reviews.json'):
    try:
        with open(filename, 'w') as file:
            json.dump(reviews, file, indent=4)
        print(f"Classified and saved {len(reviews)} reviews to {filename}")
    except IOError:
        print(f"Error: Could not write to file {filename}")

# Main function
def main():
    reviews = load_reviews()
    if reviews:
        classified_reviews = classify_reviews(reviews)
        save_classified_reviews(classified_reviews)

if __name__ == "__main__":
    main()
