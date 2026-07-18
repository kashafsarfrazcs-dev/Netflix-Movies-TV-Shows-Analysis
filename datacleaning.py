import pandas as pd
import os


# -----------------------------
# Load Dataset
# -----------------------------

DATA_PATH = "data/netflix_titles.csv"

df = pd.read_csv(DATA_PATH)

print("Original Dataset Shape:")
print(df.shape)


# -----------------------------
# Basic Information
# -----------------------------

print("\nDataset Information:")
print(df.info())


print("\nMissing Values:")
print(df.isnull().sum())


print("\nDuplicate Rows:")
print(df.duplicated().sum())


# -----------------------------
# Remove Duplicate Records
# -----------------------------

df = df.drop_duplicates()


# -----------------------------
# Handle Missing Values
# -----------------------------

df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Unknown")


# -----------------------------
# Date Cleaning
# -----------------------------

df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)


# Extract useful date features

df["year_added"] = df["date_added"].dt.year
df["month_added"] = df["date_added"].dt.month_name()


# -----------------------------
# Duration Cleaning
# -----------------------------

df["duration_value"] = (
    df["duration"]
    .str.extract("(\d+)")
    .astype(float)
)


# -----------------------------
# Genre Processing
# -----------------------------

df["genre"] = df["listed_in"].apply(
    lambda x: x.split(",")[0] if isinstance(x, str) else "Unknown"
)


# -----------------------------
# Final Dataset Check
# -----------------------------

print("\nCleaned Dataset Shape:")
print(df.shape)


print("\nCleaned Dataset Preview:")
print(df.head())


# -----------------------------
# Save Cleaned Dataset
# -----------------------------

if not os.path.exists("data/cleaned"):
    os.makedirs("data/cleaned")


df.to_csv(
    "data/cleaned/netflix_cleaned.csv",
    index=False
)


print("\nCleaned dataset saved successfully!")