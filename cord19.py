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

if __name__ == "__main__":
    df = load_data()
    explore_data(df)
