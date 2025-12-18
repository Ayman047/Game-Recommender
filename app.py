import streamlit as st
import pickle
import pandas as pd
import base64


st.set_page_config(
    page_title="ProPlay Advisor",
    page_icon="🎮",
    layout="wide"
)


def set_bg_video(video_path):
    with open(video_path, "rb") as video_file:
        video_bytes = video_file.read()

    encoded = base64.b64encode(video_bytes).decode()

    st.markdown(
        f"""
        <style>
        html, body, .stApp {{
            background: none !important;
        }}

        .video-bg {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            object-fit: cover;
            z-index: -100;
        }}
        </style>

        <video class="video-bg" autoplay loop muted playsinline>
            <source src="data:video/mp4;base64,{encoded}" type="video/mp4">
        </video>
        """,
        unsafe_allow_html=True
    )


set_bg_video(
    r"C:\Users\Ayman\Documents\projects\Game-Recommender\Game-Recommendation-System-main\assets\background.mp4"
)


games_dict = pickle.load(open("games_dict.pkl", "rb"))
games = pd.DataFrame(games_dict)
similarity = pickle.load(open("similarity.pkl", "rb"))


def recommend(game):
    idx = games[games["Title"] == game].index[0]
    distances = similarity[idx]

    games_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    return [games.iloc[i[0]].Title for i in games_list]


st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

*, html, body, [class*="css"], button, input, select, textarea, label, div, span, p {
    font-family: 'Press Start 2P' !important;
    color: white !important;
}

div[data-baseweb="select"] {
    background-color: black !important;
    border: 2px solid white !important;
}

div[data-baseweb="select"] * {
    background-color: black !important;
}

.stButton button {
    background-color: black !important;
    border: 2px solid white !important;
    padding: 12px;
    font-size: 10px;
    color: white !important;
    box-shadow: none;
    transition: box-shadow 0.25s ease;
}

.stButton button:hover {
    box-shadow:
        0 0 8px rgba(255, 255, 255, 0.8),
        0 0 16px rgba(255, 255, 255, 0.5);
}

.main-title {
    text-align: center;
    font-size: 28px;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 10px;
    opacity: 0.8;
    margin-bottom: 40px;
}

.rec {
    font-size: 11px;
    padding: 10px 0;
    border-bottom: 1px dashed #555;
    color: #32CD32 !important;
}

.rec:last-child {
    border-bottom: none;
}

.stSelectbox, .stButton {
    margin-bottom: 20px;
}
</style>
""",
    unsafe_allow_html=True
)


st.markdown(
    "<div class='main-title'>The Game Recommender ⋆˚꩜｡</div>",
    unsafe_allow_html=True
)
st.markdown(
    "<div class='subtitle'>INSERT COIN · PRESS START</div>",
    unsafe_allow_html=True
)


left, spacer, right = st.columns([3, 1, 3])

with left:
    st.markdown("### 💥SELECT GAME💥")
    selected_game = st.selectbox(
        "",
        games["Title"].values,
        key="game_select"
    )

    recommend_btn = st.button("▶ START", key="start_btn")

    st.markdown("### CURRENT GAME")
    st.write(selected_game)


with right:
    if recommend_btn:
        recs = recommend(selected_game)
        st.markdown("### ✨RECOMMENDED GAMES✨")
        st.markdown("<br>", unsafe_allow_html=True)

        for i, game in enumerate(recs, 1):
            st.markdown(
                f"<div class='rec'>{i}. {game}</div>",
                unsafe_allow_html=True
            )
