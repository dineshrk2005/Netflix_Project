# ===== Netflix EDA — 20 Charts (Single Colab Cell) =====



# 1) Imports & setup
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from itertools import combinations


sns.set(style="whitegrid")
FIG_DIR = "figures"
os.makedirs(FIG_DIR, exist_ok=True)

def save_plot(name):
    plt.tight_layout()
    path = os.path.join(FIG_DIR, name)
    plt.savefig(path, dpi=140, bbox_inches="tight")
    plt.show()
    plt.close()
    print(f"Saved: {path}")

# 2) Load CSV (update the path to your local file if needed)
csv_name = r"c:\Users\Asus\OneDrive\Desktop\Netflix project\data_sets\netflix_titles.csv"
df = pd.read_csv(csv_name)
print("Loaded shape:", df.shape)

# 3) Cleaning & feature engineering
text_cols = ["title", "director", "cast", "country", "listed_in"]
for col in text_cols:
    df[col] = df[col].fillna("").str.strip()

df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
df["year_added"] = df["date_added"].dt.year
df["month_added"] = df["date_added"].dt.month

df["duration_value"] = df["duration"].astype(str).str.extract(r"(\d+)").astype(float)
df["duration_unit"] = df["duration"].astype(str).str.extract(r"\d+\s*(.*)")

df["primary_country"] = (
    df["country"].fillna("").str.split(",").str[0].str.strip().replace("", "Unknown")
)

genre_long = (
    df.assign(genre=df["listed_in"].fillna("").str.split(","))
      .explode("genre")
)
genre_long["genre"] = genre_long["genre"].str.strip()
genre_long = genre_long[genre_long["genre"] != ""]

# 4) Charts (20)

# 1
df["type"].value_counts().plot(kind="bar")
plt.title("Movies vs TV Shows")
plt.xlabel("Type"); plt.ylabel("Count")
save_plot("type_distribution.png")

# 2
df["type"].value_counts().plot.pie(autopct="%1.1f%%", startangle=90)
plt.title("Movies vs TV Shows (Pie)"); plt.ylabel("")
save_plot("movies_vs_shows_pie.png")

# 3
df.groupby("year_added")["show_id"].count().plot(marker="o")
plt.title("Titles Added per Year")
plt.xlabel("Year"); plt.ylabel("Number of Titles")
save_plot("titles_added_per_year.png")

# 4
df.groupby("month_added")["show_id"].count().reindex(range(1,13)).plot(kind="bar")
plt.title("Titles Added by Month")
plt.xlabel("Month"); plt.ylabel("Number of Titles")
save_plot("titles_added_by_month.png")

# 5
yearly = df.groupby("year_added")["show_id"].count().dropna()
yearly.cumsum().plot(marker="o")
plt.title("Cumulative Netflix Titles Over Years")
plt.xlabel("Year"); plt.ylabel("Cumulative Count")
save_plot("cumulative_titles.png")

# 6
df["primary_country"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Countries by Number of Titles")
plt.xlabel("Country"); plt.ylabel("Count")
save_plot("top_countries.png")

# 7
genres = df["listed_in"].str.split(",").explode().str.strip()
genres.value_counts().head(15).plot(kind="bar")
plt.title("Top 15 Genres")
plt.xlabel("Genre"); plt.ylabel("Count")
save_plot("top_genres.png")

# 8
df[df["type"]=="Movie"]["duration_value"].dropna().plot(kind="hist", bins=30)
plt.title("Movie Duration Distribution (minutes)")
plt.xlabel("Minutes"); plt.ylabel("Frequency")
save_plot("movie_duration_hist.png")

# 9
df[df["type"]=="TV Show"]["duration_value"].dropna().plot(kind="hist", bins=15)
plt.title("TV Shows – Number of Seasons")
plt.xlabel("Seasons"); plt.ylabel("Frequency")
save_plot("tv_seasons_hist.png")

# 10
directors = df["director"].str.split(",").explode().str.strip()
directors = directors[directors != ""]
directors.value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Directors")
plt.xlabel("Director"); plt.ylabel("Count")
save_plot("top_directors.png")

# 11
actors = df["cast"].str.split(",").explode().str.strip()
actors = actors[actors != ""]
actors.value_counts().head(10).plot(kind="barh")
plt.title("Top 10 Actors")
plt.xlabel("Number of Titles"); plt.ylabel("Actor")
save_plot("top_actors.png")

# 12
df.pivot_table(index="year_added", columns="type", values="show_id", aggfunc="count") \
  .plot(kind="bar", stacked=True)
plt.title("Movies vs TV Shows Over Years (Stacked)")
plt.xlabel("Year"); plt.ylabel("Number of Titles")
save_plot("movies_vs_shows_yearly.png")

# 13
genre_year = genre_long.groupby(["year_added", "genre"]).size().unstack().fillna(0)
top5_genres = genre_year.sum().nlargest(5).index
genre_year[top5_genres].plot()
plt.title("Top 5 Genres Trend Over the Years")
plt.xlabel("Year"); plt.ylabel("Number of Titles")
save_plot("genre_trend_over_years.png")

# 14
top_c = df["primary_country"].value_counts().head(5).index
df[df["primary_country"].isin(top_c)] \
  .groupby(["year_added","primary_country"]).size().unstack().plot()
plt.title("Content Growth by Top 5 Countries")
plt.xlabel("Year"); plt.ylabel("Number of Titles")
save_plot("country_content_growth.png")

# 15
df.groupby(["year_added","type"]).size().unstack().plot(marker="o")
plt.title("Movies vs TV Shows (Yearly Split - Line)")
plt.xlabel("Year"); plt.ylabel("Count")
save_plot("yearly_movie_vs_show_split.png")

# 16
top15_d = directors.value_counts().head(15)
sns.barplot(x=top15_d.values, y=top15_d.index)
plt.title("Top 15 Directors (Content Count)")
plt.xlabel("Number of Titles"); plt.ylabel("Director")
save_plot("content_per_director.png")

# 17
top10_actors = actors.value_counts().head(10).index
matrix = pd.DataFrame(0, index=top10_actors, columns=top10_actors, dtype=int)
for row in df["cast"].dropna():
    row_actors = [a.strip() for a in row.split(",") if a.strip() in top10_actors]
    for a1, a2 in combinations(row_actors, 2):
        matrix.loc[a1, a2] += 1
        matrix.loc[a2, a1] += 1
plt.figure(figsize=(8,6))
sns.heatmap(matrix, annot=True, fmt="d", cmap="Blues")
plt.title("Actor Collaboration Heatmap (Top 10 Actors)")
save_plot("actor_collaboration_network.png")

# 18
text = " ".join(df["listed_in"].dropna())
wordcloud = WordCloud(width=1000, height=500, background_color="black").generate(text)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Genre Wordcloud")
save_plot("genre_wordcloud.png")

# 19
df["release_year"].value_counts().sort_index().plot(kind="bar")
plt.title("Distribution of Title Release Years")
plt.xlabel("Release Year"); plt.ylabel("Count")
save_plot("release_year_distribution.png")

# 20
heatmap_data = df.pivot_table(index="year_added", columns="month_added",
                              values="show_id", aggfunc="count").fillna(0)
plt.figure(figsize=(10,6))
sns.heatmap(heatmap_data, cmap="Reds", annot=True, fmt=".0f")
plt.title("Content Added per Month vs Year")
plt.xlabel("Month"); plt.ylabel("Year")
save_plot("heatmap_month_year.png")

# 5) Save cleaned CSV + ZIP charts
clean_path = "netflix_titles_clean.csv"
df.to_csv(clean_path, index=False)
print("Cleaned CSV saved:", clean_path)
