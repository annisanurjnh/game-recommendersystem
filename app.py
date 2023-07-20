import pickle
import streamlit as st
import requests
from PIL import Image

def recommend(title):
    index = new_df[new_df['title'] == title].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_games_names = []
    recommended_games_posters = []
    recommended_games_developer = []
    recommended_games_ratings = []
    for i in distances[1:7]:
        games_id = new_df.iloc[i[0]].image_url
        recommended_games_posters.append(games_id)
        recommended_games_names.append(new_df.iloc[i[0]].title)
        recommended_games_developer.append(new_df.iloc[i[0]].developer)
        recommended_games_ratings.append(new_df.iloc[i[0]].average_rating)

    return recommended_games_names,recommended_games_posters,recommended_games_developer,recommended_games_ratings

# Mengubah tema menjadi "dark"
st.markdown(
    """
    <style>
        .reportview-container {
            background: #1a1a1a;
            color: #fff;
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .sidebar .sidebar-content {
            background: #1a1a1a;
        }

        /* Gambar background untuk perangkat seluler */
        @media (max-width: 767px) {
            .stApp {
                background-image: url("https://imgur.com/uENp6tw.png");
                background-size: 100% 100%;
                background-repeat: no-repeat;
            }
        }

        /* Gambar background untuk desktop */
        @media (min-width: 768px) {
            .stApp {
                background-image: url("https://i.imgur.com/L9NPXnd.png");
                background-size: 100% 100%;
                background-repeat: no-repeat;
            }
        }
    </style>
    """,
    unsafe_allow_html=True
)

title = Image.open('title2.png')
st.image(title)
st.subheader('  ')

new_df = pickle.load(open('games_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

games_list = new_df['title'].values
selected_games = st.selectbox(
    "Type or Select The Game From These :",
    games_list
)

if st.button('Show Recommendation'):
    recommended_games_names,recommended_games_posters,recommended_games_developer,recommended_games_ratings = recommend(selected_games)
    col1,col2 = st.columns(2)
    with col1:
        st.subheader(recommended_games_names[0])
        st.text(recommended_games_developer[0])
        st.caption(':star2: '+(recommended_games_ratings[0]))
        st.image(recommended_games_posters[0])
    with col1:
        st.subheader(recommended_games_names[1])
        st.text(recommended_games_developer[1])
        st.caption(':star2: '+(recommended_games_ratings[1]))
        st.image(recommended_games_posters[1])
    with col1:
        st.subheader(recommended_games_names[2])
        st.text(recommended_games_developer[2])
        st.caption(':star2: '+(recommended_games_ratings[2]))
        st.image(recommended_games_posters[2])
		
    with col2:
        st.subheader(recommended_games_names[3])
        st.text(recommended_games_developer[3])
        st.caption(':star2: '+(recommended_games_ratings[3]))
        st.image(recommended_games_posters[3])
    with col2:
        st.subheader(recommended_games_names[4])
        st.text(recommended_games_developer[4])
        st.caption(':star2: '+(recommended_games_ratings[4]))
        st.image(recommended_games_posters[4])
    with col2:
        st.subheader(recommended_games_names[5])
        st.text(recommended_games_developer[5])
        st.caption(':star2: '+(recommended_games_ratings[5]))
        st.image(recommended_games_posters[5])
