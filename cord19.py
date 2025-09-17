"""
CORD-19 Metadata Explorer
"""

import pandas as pd


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


if __name__ == "__main__":
    df = load_data()
    explore_data(df)
    df_clean = clean_data(df)
