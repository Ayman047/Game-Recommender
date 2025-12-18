# 🎮 Game Recommender

A **Retro-themed Game Recommendation System** built with **Python** and **Streamlit**, designed to give personalized game suggestions based on content similarity.
---

## 🔹 Features

- **Search and Recommend:** Select a game and get the top 5 similar games.
- **Content-based Filtering:** Recommendations are based on game descriptions, developers, publishers, categories, and genres.
- **Retro UI:** Styled with `Press Start 2P` font, glowing buttons, and a space-themed background video.
- **Interactive Interface:** Built with **Streamlit** for instant web deployment.
- **Portable and Lightweight:** Uses preprocessed data (`games_dict.pkl` & `similarity.pkl`) for fast recommendations.

---

## 🛠 Tech Stack

- **Python 3.x**
- **Pandas** – for data manipulation
- **NumPy** – numerical computations
- **NLTK** – natural language processing (stemming)
- **Scikit-learn** – vectorization & cosine similarity
- **Streamlit** – interactive web app
- **Pickle** – save/load preprocessed data



---

## 🚀 How to Run

1. **Clone the repo**

```bash
git clone https://github.com/Ayman047/Game-Recommender.git
cd Game-Recommender
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the app**

```bash
streamlit run app.py
```

## 🧰 How It Works

1. **Data Preprocessing**

- Game metadata is cleaned from data.csv.
- Text from descriptions, developers, publishers, categories, and genres is combined into a single Tags column.
- Stemming and lowercasing are applied for better matching. 

2. **Vectorization**

- CountVectorizer converts tags into a numerical matrix. 
- Cosine similarity is calculated between all games. 

3. **Recommendation**

- Select a game from the app.
- The system finds the top 5 most similar games using cosine similarity.

## 💡 Future Improvements

- Add user ratings or play history for personalized collaborative filtering.
- Integrate Steam API to fetch live data.
- Add search by genre or developer in addition to title-based recommendations.
- Improve UI animations for a more immersive retro experience.
