import streamlit as st
import pickle



def recommend(movie):
    movie_index = movies_list[movies_list["title"] == movie].index[0]
    distances = similarity[movie_index]
    sorted_movie_list = sorted(list(enumerate(distances)), reverse=True,
                               key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in sorted_movie_list:
        poster_path = movies_list["poster_path"][i[0]]
        recommended_movies.append(movies_list.iloc[i[0]].title)
        recommended_posters.append("https://image.tmdb.org/t/p/original"+poster_path)

    return recommended_movies,  recommended_posters


movies_list = pickle.load(open("movies.pkl", "rb"))
movies_list_title = movies_list["title"].values

similarity = pickle.load(open("similarity.pkl", "rb"))

st.title("Project Movie Recommender System")

selected_movie_name = st.selectbox(
    "What is the movie name?",
    movies_list_title
)

if st.button("Recommend"):
    recommendation, movie_posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.write(recommendation[0])
        st.image(movie_posters[0])
    with col2:
        st.write(recommendation[1])
        st.image(movie_posters[1])
    with col3:
        st.write(recommendation[2])
        st.image(movie_posters[2])
    with col4:
        st.write(recommendation[3])
        st.image(movie_posters[3])
    with col5:
        st.write(recommendation[4])
        st.image(movie_posters[4])




# procfile
# setup.sh -> os related commands