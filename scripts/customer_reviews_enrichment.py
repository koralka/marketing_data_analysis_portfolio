# pip install pandas nltk pyodbc sqlalchemy

import pandas as pd
import pyodbc
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# VADER lexicon for sentiment analysis if not already present
nltk.download('vader_lexicon')

# function to fetch data from a SQL database using SQL query
def fetch_data_from_sql():
    # defining the connection string with parameters for the database connection
    conn_str = (
        "Driver={SQL Server};" # driver for SQL Server
        "Server=DESKTOP-2LBRR89\SQLEXPRESS;"  # SQL Server instance
        "Database=PortfolioProject_MarketingAnalytics;"  
        "Trusted_Connection=yes;"  # Windows Authentication for the connection
    )
    # connection to the database
    conn = pyodbc.connect(conn_str)

    # SQL query to fetch customer reviews data
    query = "SELECT ReviewID, CustomerID, ProductID, ReviewDate, Rating, ReviewText FROM dbo.customer_reviews"

    # fetch the data into a DataFrame
    df = pd.read_sql(query, conn)

    conn.close()

    return df


# customer reviews data from the SQL database
customer_reviews_df = fetch_data_from_sql()

# VADER sentiment analyzer for analysing the sentiment of text data
sia = SentimentIntensityAnalyzer()

# function to calculate sentiment scores using VADER
def calculate_sentiment(review):
    # sentiment scores from the review text
    sentiment = sia.polarity_scores(review)
    # return the compound score
    return sentiment['compound']

# function that categorises sentiment using both the sentiment score and the review rating
def categorise_sentiment(score, rating):
    if score > 0.05:  # positive sentiment score
        if rating >= 4:
            return 'Positive'  # high rating and positive sentiment
        elif rating == 3:
            return 'Mixed Positive'  # neutral rating but positive sentiment
        else:
            return 'Mixed Negative'  # low rating but positive sentiment
    elif score < -0.05:  # negative sentiment score
        if rating <= 2:
            return 'Negative'  # low rating and negative sentiment
        elif rating == 3:
            return 'Mixed Negative'  # neutral rating but negative sentiment
        else:
            return 'Mixed Positive'  # high rating but negative sentiment
    else:  # Neutral sentiment score
        if rating >= 4:
            return 'Positive'  # high rating with neutral sentiment
        elif rating <= 2:
            return 'Negative'  # low rating with neutral sentiment
        else:
            return 'Neutral'  # neutral rating and neutral sentiment
        
# function to bucket sentiment scores into text ranges:
def sentiment_bucket(score):
    if score >= 0.5:
        return '0.5 to 1.0'  # strongly positive sentiment
    elif 0.0 <= score < 0.5:
        return '0.0 to 0.49'  # mildly positive sentiment
    elif -0.5 <= score < 0.0:
        return '-0.49 to 0.0'  # mildly negative sentiment
    else:
        return '-1.0 to -0.5'  # strongly negative sentiment

# applying sentiment analysis to calculate sentiment scores for each review
customer_reviews_df['SentimentScore'] = customer_reviews_df['ReviewText'].apply(calculate_sentiment)

# applying sentiment categorisation using both text and rating
customer_reviews_df['SentimentCategory'] = customer_reviews_df.apply(
    lambda row: categorise_sentiment(row['SentimentScore'], row['Rating']), axis=1)  

# applying sentiment bucketing to categorise scores into defined ranges
customer_reviews_df['SentimentBucket'] = customer_reviews_df['SentimentScore'].apply(sentiment_bucket)

# first few rows of the DataFrame with sentiment scores, categories, and buckets
print(customer_reviews_df.head())

# saving the DataFrame with sentiment scores, categories, and buckets to a new CSV file
customer_reviews_df.to_csv('fact_customer_reviews_with_sentiment.csv', index=False)
