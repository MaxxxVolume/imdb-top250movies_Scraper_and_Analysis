import streamlit as st
import joblib 
import pandas as pd

# 1. Title & Description
st.set_page_config('IMDb Rating Predictor', page_icon='🎞️')
st.title('IMDb Rating Predictor')
st.write("""
         Helloooo! This app uses a Machine Learning Model (Random Forest),
         to predict how a movie would be rated at IMDb.
         """)

# Loading the page
@st.cache_resource
def load_model():
    return joblib.load('imdb_rating_predictor.pkl')

try:
    model=load_model()

except FileNotFoundError:
    st.error('Error: The file "imdb_rating_predictor.pkl" could not be found')
    st.stop()

# user inputs
st.sidebar.header('Enter Movie-Facts')

# feature 1: Release Year
year = st.sidebar.slider('Release Year', 1920,2025,2010)

# feature 2: Duration
duration_min = st.sidebar.slider('Runtime (min)', 60, 240, 120)
duration_secs = duration_min * 60

# feature 3: Votes
votes = st.sidebar.number_input('Number of Votes', min_value=1000, max_value=10000000, value=100000, step=10000)

# feature 4: title_length
title_text = st.sidebar.text_input('Movie Title', 'Example Movie')
title_length = len(title_text)

st.sidebar.markdown('---')
st.sidebar.write(f"**Title Length:** {title_length} characters")


# predicting the rating
if st.button("Predict Rating"):
    input_data = pd.DataFrame({
        'Year':[year],
        'Duration (secs)': [duration_secs],
        'Votes':[votes],
        'Title_Length':[title_length]
    })

    # actual prediction
    prediction = model.predict(input_data)[0]

    # displaying result
    st.success(f'Predicted IMDb Rating **{prediction:.1f}** ⭐')

    # details / context
    if prediction > 8.5:
        st.balloons()
        st.write("Damn! That's a Banger.")
    elif prediction >= 7.5:
        st.write("That's a decent movie.")
    elif prediction < 7.5:
        st.write("Loser! You like a movie that's actually bad HAHA.")