import streamlit as st
import pytube
import base64
from io import BytesIO


video_url = st.text_input("Enter URL:")
if video_url:
    video_instance = pytube.YouTube(video_url)
    video_id = video_instance.video_id
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    st.video(video_url)
    file_name =f'{video_instance.title}'
    st.write(file_name)
    if st.button("Download Video"):
        st.success("File will be downloaded shortly.")
        stream = video_instance.streams.get_highest_resolution()
        title = 'test.mp4'
        video_file = stream.download(filename=title)
        with open(title, 'rb') as f:
            bytes = f.read()
            b64 = base64.b64encode(bytes).decode()
            href = f'<a href="data:file/zip;base64,{b64}" download=\'{title}\'>\
                Here is your link \
            </a>'
            st.markdown(href, unsafe_allow_html=True)

        st.success("Your File Is Ready To Be Downloaded!")
