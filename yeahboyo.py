from textblob import TextBlob

def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the sentiment polarity (-1 to 1)
    sentiment_polarity = blob.sentiment.polarity
    
    # Classify sentiment
    if sentiment_polarity > 0:
        return "Positive"
    elif sentiment_polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Main function
def main():
    text = input("Enter the text you want to analyze: ")
    sentiment = analyze_sentiment(text)
    print("Sentiment:", sentiment)

if __name__ == "__main__":
    main()
