# Marketing Data Analysis Portfolio Project

A data-driven breakdown of marketing performance from 2023–2025, using SQL, Python and Power BI to uncover trends in conversions, engagement, and customer satisfaction.

## 📁 Project Structure
```
marketing-data-analysis-portfolio/
├── data/ # Output data (CSV with sentiment scores)
├── dashboard/ # Power BI dashboard file
├── scripts/ # Python sentiment analysis
├── sql/ # SQL scripts used for cleaning and analysis
```

## 🔧 Tools & Technologies

- **SQL Server**: Data extraction, cleaning, and transformation
- **Python (pandas, NLTK/VADER)**: Sentiment analysis on customer reviews
- **Power BI**: Dashboard for reporting insights
- **Git & GitHub**: Version control and portfolio publishing

## 🔍 Key Features

- VADER-based sentiment scoring of customer review text
- Sentiment categorisation combining review text and star rating
- Bucketing of sentiment scores into analysis-friendly ranges
- Export of enriched review data to CSV
- Interactive dashboard visualising key insights

## 📊 Sample Output Columns

- `SentimentScore`: Compound score (-1.0 to +1.0)
- `SentimentCategory`: Positive, Negative, Mixed Positive, Mixed Negative, Neutral
- `SentimentBucket`: Score ranges (e.g., "0.5 to 1.0", "-0.49 to 0.0")

## 📦 File Highlights

- `scripts/customer_reviews_enrichment.py`: Main Python analysis script
- `data/fact_customer_reviews_with_sentiment.csv`: Cleaned + scored review data
- `dashboard/Marketing Analytics Analysis Dashboard.pbix`: Power BI dashboard
- `sql/`: SQL queries for data preparation and transformation

## 📈 Project Outcome

This project demonstrates end-to-end data analysis skills:
- Connecting SQL data to Python
- Enriching raw data with sentiment scores
- Preparing structured outputs for visualisation
- Communicating insights through Power BI

## 📬 Contact

Feel free to fork this project or reach out on [LinkedIn](https://linkedin.com/in/karolina-malec) if you'd like to collaborate or learn more.

## 📌 Data Source

The dataset used in this project was found online and is publicly available for free use.  
It was provided as part of an open portfolio project and used here for educational and non-commercial purposes.

