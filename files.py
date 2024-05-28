import streamlit as st
import pandas as pd

st.subheader('uploading the CSV file')
df=st.file_uploader('upload the csv file : ',type=['csv','xlsx'])

st.subheader('Loading the CSV File')
df=pd.read_csv(Products.csv")
if df is not None:
    st.table(df.head())

st.subheader('loading image directly')
st.image(img.png")
st.subheader('Working with Images')
img_file = st.file_uploader("Upload the Image file : ", type = ['png', 'jpeg'])
if img_file is not None:
    st.image(img_file)
st.subheader('Working with Videos')
video_file = st.file_uploader("Upload the Video file : ", type = ['mkv', 'mp4'])
if video_file is not None:
    st.video(video_file, start_time = 0)

st.subheader('Working with Audio')
audio_file = st.file_uploader("Upload the audio file : ", type = ['mp3', 'wav'])
if audio_file is not None:
    st.audio(audio_file.read())
