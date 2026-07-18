import plotly.express as px


# -------------------------------------------------
# Movies vs TV Shows
# -------------------------------------------------

def type_distribution(df):

    count = df["type"].value_counts().reset_index()
    count.columns = ["Type", "Count"]

    fig = px.pie(
        count,
        names="Type",
        values="Count",
        title="Movies vs TV Shows Distribution",
        hole=0.4
    )

    return fig



# -------------------------------------------------
# Content Added Over Years
# -------------------------------------------------

def content_growth(df):

    yearly = (
        df["year_added"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    yearly.columns = ["Year", "Count"]

    fig = px.line(
        yearly,
        x="Year",
        y="Count",
        markers=True,
        title="Netflix Content Added Over Years"
    )

    return fig



# -------------------------------------------------
# Top Countries
# -------------------------------------------------

def top_countries(df):

    countries = (
        df["country"]
        .str.split(", ")
        .explode()
        .value_counts()
        .head(10)
        .reset_index()
    )

    countries.columns = ["Country", "Count"]

    fig = px.bar(
        countries,
        x="Count",
        y="Country",
        orientation="h",
        title="Top 10 Countries Producing Netflix Content"
    )

    return fig



# -------------------------------------------------
# Top Genres
# -------------------------------------------------

def top_genres(df):

    genres = (
        df["listed_in"]
        .str.split(", ")
        .explode()
        .value_counts()
        .head(10)
        .reset_index()
    )

    genres.columns = ["Genre", "Count"]

    fig = px.bar(
        genres,
        x="Genre",
        y="Count",
        title="Top Netflix Genres"
    )

    return fig



# -------------------------------------------------
# Rating Distribution
# -------------------------------------------------

def rating_distribution(df):

    ratings = (
        df["rating"]
        .value_counts()
        .reset_index()
    )

    ratings.columns = ["Rating", "Count"]

    fig = px.bar(
        ratings,
        x="Rating",
        y="Count",
        title="Netflix Rating Distribution"
    )

    return fig



# -------------------------------------------------
# Release Year Trend
# -------------------------------------------------

def release_year_trend(df):

    years = (
        df["release_year"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    years.columns = ["Year", "Count"]

    fig = px.area(
        years,
        x="Year",
        y="Count",
        title="Content Released Over Years"
    )

    return fig



# -------------------------------------------------
# Duration Analysis
# -------------------------------------------------

def duration_analysis(df):

    fig = px.histogram(
        df,
        x="duration_value",
        color="type",
        title="Content Duration Analysis"
    )

    return fig



# -------------------------------------------------
# Top Directors
# -------------------------------------------------

def top_directors(df):

    directors = (
        df[df["director"] != "Unknown"]["director"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    directors.columns = ["Director", "Count"]

    fig = px.bar(
        directors,
        x="Count",
        y="Director",
        orientation="h",
        title="Top 10 Directors"
    )

    return fig



# -------------------------------------------------
# Monthly Content Added
# -------------------------------------------------

def monthly_additions(df):

    months = (
        df["month_added"]
        .value_counts()
        .reset_index()
    )

    months.columns = ["Month", "Count"]

    fig = px.bar(
        months,
        x="Month",
        y="Count",
        title="Content Added by Month"
    )

    return fig
# -------------------------------------------------
# Genre Treemap
# -------------------------------------------------

def genre_treemap(df):

    genres = (
        df["listed_in"]
        .str.split(", ")
        .explode()
        .value_counts()
        .reset_index()
    )

    genres.columns = ["Genre", "Count"]

    fig = px.treemap(
        genres,
        path=["Genre"],
        values="Count",
        title="Netflix Content by Genre"
    )

    return fig



# -------------------------------------------------
# Country Genre Sunburst
# -------------------------------------------------

def country_genre_sunburst(df):

    temp = df[
        ["country", "listed_in"]
    ].dropna()


    temp["country"] = (
        temp["country"]
        .str.split(", ")
    )

    temp = temp.explode("country")


    temp["genre"] = (
        temp["listed_in"]
        .str.split(", ")
        .str[0]
    )


    fig = px.sunburst(
        temp,
        path=[
            "country",
            "genre"
        ],
        title="Country and Genre Relationship"
    )

    return fig



# -------------------------------------------------
# Content Added Heatmap
# -------------------------------------------------

def content_heatmap(df):

    heatmap_data = (
        df.groupby(
            [
                "year_added",
                "month_added"
            ]
        )
        .size()
        .reset_index(
            name="Count"
        )
    )


    fig = px.density_heatmap(
        heatmap_data,
        x="month_added",
        y="year_added",
        z="Count",
        title="Netflix Content Added Heatmap"
    )


    return fig