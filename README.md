# 📊 Netflix Data Analytics Project (2024)

This project performs a complete exploratory data analysis (EDA) and visualization on the **Netflix Shows and Movies Dataset** using Python. The goal is to uncover trends in content type, release years, countries, genres, durations, and more.

---

## 📁 Dataset

- **Name:** `netflix_titles.csv`
- **Source:** [Kaggle Netflix Dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- **Fields:** show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description

---

## ⚙️ Technologies Used

- Python 3
- Pandas, NumPy
- Matplotlib, Seaborn
- Jupyter Notebook / Google Colab

---

## 📌 Project Structure

netflix-data-analysis/
│
├── netflix_titles.csv # Dataset
├── netflix_analysis.ipynb # Full EDA and visualizations
├── output_charts/ # All 20+ generated charts
├── README.md # Project documentation

---

## 📊 Visualizations (20 Charts)

| Chart No. | Title                                           | Description                                         |
|-----------|--------------------------------------------------|-----------------------------------------------------|
| 1         | Type Distribution                                | Count of Movies vs TV Shows                         |
| 2         | Titles Added Per Year                            | Trend of titles added each year                     |
| 3         | Titles Added Per Month                           | Monthly addition pattern                            |
| 4         | Cumulative Titles Growth                         | How Netflix’s library has grown over time           |
| 5         | Top 10 Producing Countries                       | Countries contributing the most content             |
| 6         | Top 15 Genres                                    | Most common content categories                      |
| 7         | Movie Duration Histogram                         | Distribution of movie lengths                       |
| 8         | TV Show Seasons Histogram                        | Distribution of seasons for TV shows                |
| 9         | Top 10 Directors                                 | Most frequent directors on Netflix                  |
| 10        | Top 10 Actors                                    | Most frequent actors                                |
| 11        | Movies vs TV Shows Added Yearly (Stacked)        | Content trend breakdown                             |
| 12        | Rating Distribution                              | Content ratings breakdown (e.g., PG, TV-MA)         |
| 13        | Content Added by Country and Year                | Heatmap of country-wise additions                   |
| 14        | Content Length Word Count Histogram              | Length of descriptions                              |
| 15        | Word Cloud of Titles                             | Frequent words in content titles                    |
| 16        | Word Cloud of Descriptions                       | Most used words in descriptions                     |
| 17        | Year-wise Average Movie Duration                 | How movie durations change by year                  |
| 18        | Year-wise Count of TV Shows                      | TV shows growth trend                               |
| 19        | Year-wise Count of Movies                        | Movie content trend                                 |
| 20        | Multi-Genre Content Proportion                   | Titles belonging to multiple genres                 |

---

## 🧹 Data Cleaning Performed

- Removed null values in key fields
- Parsed `date_added` to datetime
- Split multi-genre fields for better counting
- Standardized column names
- Removed duplicates

---

## 🚀 How to Run

### Option 1: Google Colab
1. Open the `.ipynb` file in [Google Colab](https://colab.research.google.com/).
2. Upload the `netflix_titles.csv` file when prompted.
3. Run all cells to generate all charts.

### Option 2: Jupyter Notebook
1. Clone/download the repo.
2. Place `netflix_titles.csv` in the same folder.
3. Open `netflix_analysis.ipynb` in Jupyter.
4. Run all cells.

---

## 📦 Output

All charts will be saved in the `output_charts/` directory and can be included in your final-year project report or presentation.

---

## 👨‍🎓 Author

- **Name:** Dinesh R
- **Project:** Final Year B.Tech – Data Science
- **College:** Anna University, Suguna College of Engineering




## 📌 License

This project is for educational use only.


