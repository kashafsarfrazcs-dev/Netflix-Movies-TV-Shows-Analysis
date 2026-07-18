import streamlit as st
import pandas as pd

from visualizations import (
    type_distribution,
    content_growth,
    top_countries,
    top_genres,
    rating_distribution,
    release_year_trend,
    duration_analysis,
    top_directors,
    monthly_additions,
    genre_treemap,
    country_genre_sunburst,
    content_heatmap
)


# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="Netflix Analytics Dashboard",
    page_icon="🎬",
    layout="wide"
)


# -----------------------------------
# Load Dataset
# -----------------------------------

@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/cleaned/netflix_cleaned.csv"
    )

    return df


df = load_data()



# -----------------------------------
# Header
# -----------------------------------

st.title(" Netflix Movies & TV Shows Analysis Dashboard")

st.markdown(
    """
    An interactive data analytics dashboard exploring Netflix
    content trends, genres, ratings, countries and release patterns.
    """
)



# -----------------------------------
# Sidebar Filters
# -----------------------------------

st.sidebar.title(" Dashboard Filters")


selected_type = st.sidebar.multiselect(
    "Content Type",
    df["type"].unique(),
    default=df["type"].unique()
)


selected_rating = st.sidebar.multiselect(
    "Rating",
    df["rating"].unique(),
    default=df["rating"].unique()
)



filtered_df = df[
    (df["type"].isin(selected_type)) &
    (df["rating"].isin(selected_rating))
]



# -----------------------------------
# KPI Section
# -----------------------------------

st.header("📌 Overview")


col1, col2, col3, col4, col5 = st.columns(5)


with col1:
    st.metric(
        "Total Titles",
        filtered_df.shape[0]
    )


with col2:
    st.metric(
        "Movies",
        len(
            filtered_df[
                filtered_df["type"] == "Movie"
            ]
        )
    )


with col3:
    st.metric(
        "TV Shows",
        len(
            filtered_df[
                filtered_df["type"] == "TV Show"
            ]
        )
    )


with col4:
    st.metric(
        "Countries",
        filtered_df["country"].nunique()
    )


with col5:
    st.metric(
        "Latest Release",
        filtered_df["release_year"].max()
    )



# -----------------------------------
# Content Overview
# -----------------------------------

st.header(" Content Overview")


st.plotly_chart(
    type_distribution(filtered_df),
    use_container_width=True
)


st.plotly_chart(
    content_growth(filtered_df),
    use_container_width=True
)



# -----------------------------------
# Geographic Analysis
# -----------------------------------

st.header(" Geographic Analysis")


st.plotly_chart(
    top_countries(filtered_df),
    use_container_width=True
)



st.plotly_chart(
    country_genre_sunburst(filtered_df),
    use_container_width=True
)



# -----------------------------------
# Genre & Category Analysis
# -----------------------------------

st.header(" Genre Analysis")


col1, col2 = st.columns(2)


with col1:

    st.plotly_chart(
        top_genres(filtered_df),
        use_container_width=True
    )


with col2:

    st.plotly_chart(
        genre_treemap(filtered_df),
        use_container_width=True
    )



# -----------------------------------
# Ratings Analysis
# -----------------------------------

st.header(" Ratings Analysis")


st.plotly_chart(
    rating_distribution(filtered_df),
    use_container_width=True
)



# -----------------------------------
# Time Analysis
# -----------------------------------

st.header(" Time Based Analysis")


st.plotly_chart(
    release_year_trend(filtered_df),
    use_container_width=True
)


st.plotly_chart(
    monthly_additions(filtered_df),
    use_container_width=True
)


st.plotly_chart(
    content_heatmap(filtered_df),
    use_container_width=True
)



# -----------------------------------
# Content Details
# -----------------------------------

st.header("🎥 Content Details")


col1, col2 = st.columns(2)


with col1:

    st.plotly_chart(
        duration_analysis(filtered_df),
        use_container_width=True
    )


with col2:

    st.plotly_chart(
        top_directors(filtered_df),
        use_container_width=True
    )



# -----------------------------------
# Dataset Preview
# -----------------------------------

st.header(" Dataset Preview")


st.dataframe(
    filtered_df.head(100),
    use_container_width=True
)