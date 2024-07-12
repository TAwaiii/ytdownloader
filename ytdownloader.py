import streamlit as st
from pytube import YouTube
import os

st.set_page_config(page_title="YTdownloader", page_icon="(:")
st.divider()
st.title("YT downloader")
st.divider()
link_input = st.text_input(label="Enter link")

if st.button("RUN"):
    if link_input:
        yt = YouTube(link_input)
        video_title = yt.title
        video_path = os.path.join('c:\\Users\\Folio 9470m\\Videos', f"{video_title}.mp4")

        if not os.path.exists(video_path):
            yd = yt.streams.get_highest_resolution()
            yd.download('c:\\Users\\Folio 9470m\\Videos')
            st.success(f"Video '{video_title}' downloaded successfully.")
        else:
            st.info(f"Video '{video_title}' is already downloaded.")
    else:
        st.error("Please enter a valid YouTube link.")