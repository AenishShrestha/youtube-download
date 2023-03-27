import streamlit as st
import pytube

video_url = st.text_input("Enter URL:")
if video_url:
    video_instance = pytube.YouTube(video_url)
    video_id = video_instance.video_id
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    st.video(video_url)
    if st.button("Download Video"):
        st.success("File will be downloaded shortly.")
        stream = video_instance.streams.get_highest_resolution()
        stream.download()
        st.success("Video downloaded successfully!")
