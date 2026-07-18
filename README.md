# Netflix Movies & TV Shows Analysis Dashboard

##  Project Overview

The *Netflix Movies & TV Shows Analysis Dashboard* is an end-to-end Data Analytics project developed to explore and analyze Netflix's content library.

This project uses real-world Netflix data to identify meaningful patterns and trends related to:

- Movies and TV Shows distribution
- Content growth over time
- Popular genres
- Top content-producing countries
- Audience ratings
- Movie duration analysis
- Directors and actors insights

The final outcome is an interactive dashboard built using *Python and Streamlit* that transforms raw data into meaningful visual insights.

---

#  Objectives

The main objectives of this project are:

- Understand and analyze a real-world dataset.
- Perform data cleaning and preprocessing.
- Apply feature engineering techniques.
- Conduct Exploratory Data Analysis (EDA).
- Create meaningful visualizations.
- Build an interactive analytics dashboard.

---

#  Dataset Information

## Dataset Source

*Kaggle - Netflix Movies and TV Shows Dataset*

Dataset File:


netflix_titles.csv


## Dataset Size

- Total Records: *8,807*
- Total Columns: *12*

## Important Features

| Feature | Description |
|---|---|
| show_id | Unique identifier of content |
| type | Movie or TV Show |
| title | Content title |
| director | Director information |
| cast | Actors information |
| country | Production country |
| date_added | Date added to Netflix |
| release_year | Original release year |
| rating | Audience classification |
| duration | Movie duration or seasons |
| listed_in | Genres/categories |
| description | Content summary |

---

#  Technologies Used

## Programming Language

 Python

## Data Analysis

- Pandas
- NumPy

## Data Visualization

- Matplotlib
- Seaborn

## Dashboard Development

- Streamlit

## Tools

- VS Code
- Git
- GitHub

---

# Project Workflow


Raw Dataset
      |
      ↓
Data Understanding
      |
      ↓
Data Cleaning
      |
      ↓
Feature Engineering
      |
      ↓
Exploratory Data Analysis
      |
      ↓
Visualization
      |
      ↓
Interactive Dashboard


---

# Data Cleaning Process

The raw dataset was processed to improve data quality.

## Missing Value Handling

Handled missing values in important columns:

- Director
- Country
- Rating
- Cast

## Duplicate Removal

Removed duplicate records to ensure accurate analysis.

python
df.drop_duplicates()


## Data Transformation

Converted complex columns into analysis-friendly formats.

Examples:

- Date extraction
- Duration conversion
- Multiple category separation

---

# Feature Engineering

Feature engineering was performed to create additional useful information.

## Year Added Feature

Extracted year from:


date_added


Used for:

- Content growth analysis
- Time-based trends


## Duration Value Feature

Converted:


120 min


into:


120


Used for numerical duration analysis.

---

# Exploratory Data Analysis

## 1. Movies vs TV Shows Analysis

### Question:
What type of content dominates Netflix?

Visualization:

- Bar Chart

Insight:

Netflix contains a higher number of movies compared to TV shows.

---

## 2. Netflix Content Growth Trend

### Question:
How has Netflix expanded its library over time?

Visualization:

- Line Chart

Insight:

Netflix experienced significant growth in content availability.

---

## 3. Country Contribution Analysis

Analyzed countries producing Netflix content.

Techniques:

- split()
- explode()
- value_counts()

Visualization:

- Horizontal Bar Chart

---

## 4. Genre Analysis

Identified the most common Netflix categories.

Visualization:

- Bar Chart

Examples:

- Drama
- Comedy
- Documentary
- Action

---

## 5. Rating Analysis

Analyzed audience classifications.

Examples:

- TV-MA
- TV-14
- PG-13

Visualization:

- Distribution Chart

---

## 6. Movie Duration Analysis

Analyzed movie length patterns.

Visualization:

- Histogram

Finding:

Most movies are approximately between 90–120 minutes.

---

## 7. Director and Actor Analysis

Processed multiple values in:

- Director column
- Cast column

Using:


split()
explode()


to analyze individual contributors.

---

#  Dashboard Features

The Streamlit dashboard provides:

## KPI Cards

Displays:

- Total Netflix Titles
- Movies Count
- TV Shows Count
- Countries Count


##  Interactive Filters

Users can explore content using filters.

##  Visualizations

Dashboard includes:

- Bar Charts
- Line Charts
- Histograms
- Distribution Charts

---


# Project Structure


Netflix-Movies-TV-Shows-Analysis

│
├── app.py
├── datacleaning.py
├── visualizations.py
├── requirements.txt
│
├── data
│   ├── netflix_titles.csv
│   └── cleaned
│       └── netflix_cleaned.csv
│
├── screenshots
│
└── Documentation.docx


---

#  Installation & Usage

## Clone Repository

git clone https://github.com/kashafsarfrazcs-dev/Netflix-Movies-TV-Shows-Analysis.git


## Install Dependencies

pip install -r requirements.txt


## Run Dashboard

streamlit run app.py


The application will open in your browser.

---

# Learning Outcomes

This project helped me develop practical skills in:

- Data Cleaning  
- Data Preprocessing  
- Feature Engineering  
- Exploratory Data Analysis  
- Data Visualization  
- Dashboard Development  
- Working with Real-World Datasets  

---

#  Future Enhancements

Future improvements may include:

- Netflix recommendation system
- NLP analysis on movie descriptions
- User rating prediction
- Cloud deployment
- Advanced interactive filters

---

#  Author

*Kashaf Sarfraz*

Computer Science Student | Data Analytics Enthusiast
