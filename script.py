import pandas as pd
import re
from textblob import TextBlob
import ftfy  # Import ftfy to fix text encoding issues

# Load the dataset
file_path = r'user_review.xls'
reviews_df = pd.read_excel(file_path, engine='xlrd')

# Display the first few rows of the dataframe to understand its structure
print(reviews_df.head())

# Clean the data by removing null values
reviews_df = reviews_df.dropna()

# Remove unnecessary columns (assuming the relevant column is 'review')
# Adjust the column names according to your dataset
reviews_df = reviews_df[['review']]  # Replace 'review' with the actual column name if different

# Preprocess the text: fix encoding issues, lowercasing, and removing punctuation
def preprocess_text(text):
    text = ftfy.fix_text(text)  # Fix encoding issues
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove all punctuation
    return text

reviews_df['cleaned_review'] = reviews_df['review'].apply(preprocess_text)

# Perform sentiment analysis
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'neutral'

reviews_df['sentiment'] = reviews_df['cleaned_review'].apply(get_sentiment)

# Generate summary report
sentiment_distribution = reviews_df['sentiment'].value_counts()
print(sentiment_distribution)

# Save the DataFrame with new columns to a new CSV file
output_file_path = r'C:\Users\nages\Desktop\work\AI Certs\user_review_with_sentiment.csv'
reviews_df.to_csv(output_file_path, index=False)

# Save the sentiment distribution to a CSV file for the report
sentiment_distribution.to_csv(r'C:\Users\nages\Desktop\work\AI Certs\sentiment_distribution.csv', index=True)
