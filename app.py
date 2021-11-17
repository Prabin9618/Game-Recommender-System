import streamlit as st
import pandas as pd
import pickle
import requests
import base64

#importing games list and model
games_list = pickle.load(open('PC_Games.pkl','rb'))
games = pd.DataFrame(games_list)

cs = pickle.load(open('cs.pkl','rb'))

games_list_pub = pickle.load(open('PC_Games_withpub.pkl','rb'))
games_pub = pd.DataFrame(games_list_pub)

cs1 = pickle.load(open('cs1.pkl','rb'))

#function to fetch images of the game
def pic(name):
    req_get = requests.get("https://api.rawg.io/api/games?key=b6bbc547751541d8a825fbf47216ab81&search="+str(name)+"&page_size=1")
    data = req_get.json()
    result = data['results'][0]['background_image']
    return(result)

#function to recommend game
def recommend(name):
    id = games[games.Title == name].index[0]
    scores = list(enumerate(cs[id]))
    sorted_scores = sorted(scores, key = lambda x:x[1], reverse=True)[1:6]
    
    games_list = []
    game_desc = []
    user_score = []
    games_image = []
    
    for item in sorted_scores:
        games_list.append(games.iloc[item[0]].Title)
        game_desc.append(games.iloc[item[0]].Description)
        user_score.append(games.iloc[item[0]]['User Score'])
        result = pic(games.iloc[item[0]].Title)
        games_image.append(result)
    return games_list,game_desc,user_score,games_image

def recommendsimilar(name):
    id = games_pub[games_pub.Title == name].index[0]
    scores = list(enumerate(cs1[id]))
    sorted_scores = sorted(scores, key = lambda x:x[1], reverse=True)[1:6]
    
    games_list = []
    games_image = []
    
    for item in sorted_scores:
        games_list.append(games_pub.iloc[item[0]].Title)
        result = pic(games_pub.iloc[item[0]].Title)
        games_image.append(result)
    return games_list,games_image

#setting custom wallpaper
main_bg = "wallpaper.jpg"
main_bg_ext = "jpg"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)

#UI building and function calling
st.title('What to play next?')

selected_game = st.selectbox('Select a game you liked: ',games['Title'].values)

if st.button('Recommend'):
    name,desc,score,image = recommend(selected_game)
    col1 = st.columns(1)
    st.subheader(name[0])
    st.markdown(desc[0])
    st.subheader(score[0])
    st.image(image[0])
        
    st.subheader(name[1])
    st.markdown(desc[1])
    st.subheader(score[1])
    st.image(image[1])
        
    st.subheader(name[2])
    st.markdown(desc[2])
    st.subheader(score[2])
    st.image(image[2])
    
    st.subheader(name[3])
    st.markdown(desc[3])
    st.subheader(score[3])
    st.image(image[3])
    
    st.subheader(name[4])
    st.markdown(desc[4])
    st.subheader(score[4])
    st.image(image[4])
    
    st.header('You might also like from the same publisher...')
    name_pub,image_pub = recommendsimilar(selected_game)
    col1,col2,col3 = st.columns(3)
    with col1:
        st.markdown(name_pub[0])
        st.image(image_pub[0])
    with col2:
        st.markdown(name_pub[1])
        st.image(image_pub[1])
    with col3:
        st.markdown(name_pub[2])
        st.image(image_pub[2])