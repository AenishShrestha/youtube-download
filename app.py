import streamlit as st
import pytube
import base64
import re
from io import BytesIO

def remove_special_characters(text):
    pattern = r'[^a-zA-z0-9\s]'
    text = re.sub(pattern, '', text)
    return text

video_url = st.text_input("Enter URL:")
if video_url:
    video_instance = pytube.YouTube(video_url)
    video_id = video_instance.video_id
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    st.video(video_url)
    file_name =f'{video_instance.title}'
    file_name = remove_special_characters(file_name)
    file_name = f'{file_name}.mp4'
    st.write(file_name)
    button = st.button("Download ⚡️")
    if button:
        with st.spinner('File will be downloaded shortly. Downloading...'):
            try:
                stream = video_instance.streams.get_highest_resolution()
                video_file = stream.download(filename=file_name)
                

                with open(file_name, 'rb') as f:
                    bytes = f.read()
                    b64 = base64.b64encode(bytes).decode()
                    href = f'<a href="data:file/zip;base64,{b64}" download=\'{file_name}\'>\
                        Here is your link \
                    </a>'
                    st.markdown(href, unsafe_allow_html=True)
                st.success("Your File Is Ready To Be Downloaded!")
                st.balloons()
                

            except :
                st.error('Sorry Try Again Later')
