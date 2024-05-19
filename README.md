# Sentiment Analysis Program

This program analyzes the sentiment of text input by the user. It uses the TextBlob library, a Python library for processing textual data, to determine whether the sentiment of the text is positive, negative, or neutral.

## Installation

To use this program, you need to have Python installed on your system. You also need to install the TextBlob library. You can install TextBlob using pip:

pip install textblob

## How to Use

1. **Clone the Repository**: Clone or download the repository containing the program files.

2. **Navigate to the Directory**: Using the command line, navigate to the directory where the program files are located.

3. **Run the Program**: Run the program by executing the Python file `sentiment_analysis.py`.

python sentiment_analysis.py

4. **Enter Text**: Once the program is running, enter the text you want to analyze when prompted.

5. **View Sentiment**: After entering the text, the program will analyze the sentiment and display whether it is positive, negative, or neutral.

## Program Structure

The program consists of a single Python script, `sentiment_analysis.py`, which contains the following functions:

- `analyze_sentiment(text)`: This function takes a piece of text as input, analyzes its sentiment using TextBlob, and returns whether the sentiment is positive, negative, or neutral.

- `main()`: This is the main function of the program. It prompts the user to input text, calls the `analyze_sentiment()` function to analyze the sentiment of the input text, and then prints the sentiment.

## Dependencies

This program has the following dependency:

- **TextBlob**: A Python library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.

## Contributions

Contributions to this project are welcome. If you have any suggestions for improvements or new features, feel free to submit a pull request.
