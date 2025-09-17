"""
CORD-19 Metadata Explorer
"""

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def load_data(path="data/metadata.csv"):
    """Loading CORD-19 metadata from a CSV file."""
    df = pd.read_csv(path, low_memory=False)
    return df


def explore_data(df):
    """Data exploration"""
    print("Data Shape:", df.shape)
    print("\nInfo:")
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum().head(20))
    print("\nDescribing numerical columns:")
    print(df.describe())


def clean_data(df):
    """Data cleaning and preparation"""
    # Converting publish time to datetime
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    df["year"] = df["publish_time"].dt.year

    # Creating abstract word count as an example
    df['abstract_word_count'] = df["abstract"].fillna("").apply(lambda x: len(x.split()))

    #Removing rows with missing title or publish_time
    df_clean = df.dropna(subset=["title", "publish_time"])

    return df_clean


def analyze_and_visualize(df):
    """Analysis and Visualization"""
    # Publications per year
    year_counts = df["year"].value_counts().sort_index()
    plt.figure(figsize=(8, 5))
    plt.bar(year_counts.index, year_counts.values)
    plt.title("Publications by Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Publications")
    plt.savefig("publications_by_year.png")
    plt.close()

    # Top journals
    top_journals = df["journal"].value_counts().head(10)
    plt.figure(figsize=(8, 5))
    top_journals.plot(kind='bar')
    plt.title("Top 10 Journals Publishing COVID-19 Research")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("top_journals.png")
    plt.close()

    # Word cloud of titles
    text = " ".join(df["title"].dropna().tolist())
    wordcloud = WordCloud(width=800, height=400,background_color='white').generate(text)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig("title_wordcloud.png")
    plt.close()

    print("Visualizations saved: publications_by_year.png, top_journals.png, title_wordcloud.png")


if __name__ == "__main__":
    df = load_data()
    explore_data(df)
    df_clean = clean_data(df)
    analyze_and_visualize(df_clean)
