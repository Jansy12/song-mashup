#!/usr/bin/env python
# coding: utf-8

# In[15]:


import streamlit as st
from email.message import EmailMessage
import os
from pytube import YouTube, Search
import moviepy.editor as mp
from moviepy.editor import AudioFileClip, concatenate_audioclips
import zipfile
import smtplib

# Function to check constraints
def check_constraints(number_of_videos, audio_duration):
    if int(number_of_videos) >= 10 and int(audio_duration) >= 20:
        return True
    else:
        return False

# Function to send email
def send_email(sender_email, sender_password, recipient_email, subject, message, file_name, file_data):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg.set_content(message)
    msg.add_attachment(file_data, maintype="application", subtype="zip", filename=file_name)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
            return True
    except smtplib.SMTPAuthenticationError:
        st.error("Failed to authenticate. Please check your email and password.")
        return False
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return False

# Streamlit setup
st.set_page_config(layout='centered', page_title='Mashup')
st.header("MASHUP")

# Form input
with st.form("form1", clear_on_submit=True):
    singer_name = st.text_input("Singer Name")
    number_of_videos = st.text_input("Number of Videos")
    duration = st.text_input("Duration of each video (in sec)")
    email = st.text_input("Email ID", placeholder='example@gmail.com')
    submit = st.form_submit_button("Submit")

# Main functionality
if submit:
    if check_constraints(number_of_videos, duration):
        sender_email = "riya.mashupproject@gmail.com"  # Your Gmail address
        sender_password = "helloabcd"   # Your Gmail password
        subject = "Mashup Results"
        message = f"This is a mashup zip file of the audios of the singer {singer_name}.\n\nDone By -\nKhushi Prasad\n102183044\nCOE20"

        path = os.getcwd()
        search_results = []
        vid_files = []
        aud_files = []
        sub_files = []
        aud_clip = []

        s = Search(singer_name)
        for v in s.results:
            search_results.append(v.watch_url)

        for i in range(int(number_of_videos)):
            yt = YouTube(search_results[i])
            fin = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
            os.rename(fin, f'Video-{i}.mp4')
            vid_files.append(f'Video-{i}.mp4')

        for file in vid_files:
            clip = mp.VideoFileClip(os.path.join(path, file))
            clip.audio.write_audiofile(os.path.join(path, f'{os.path.splitext(file)[0]}.mp3'))
            aud_files.append(f'{os.path.splitext(file)[0]}.mp3')

        for file in aud_files:
            sub_file = AudioFileClip(os.path.join(path, file))
            final = sub_file.subclip(0, int(duration))
            final.write_audiofile(os.path.join(path, f'Sub{file}'))
            sub_files.append(f'Sub{file}')

        for file in sub_files:
            aud_clip.append(AudioFileClip(os.path.join(path, file)))

        final_audio = concatenate_audioclips(aud_clip)
        final_audio.write_audiofile(os.path.join(path, 'Mashup.mp3'))

        with zipfile.ZipFile("mashup.zip", "w", zipfile.ZIP_DEFLATED) as zip:
            zip.write(os.path.join(path, 'Mashup.mp3'))

        with open("mashup.zip", "rb") as f:
            file_data = f.read()

        if send_email(sender_email, sender_password, email, subject, message, "mashup.zip", file_data):
            st.success("Email Sent Successfully!")
    else:
        st.error("Please ensure that the number of videos is greater than or equal to 10 and the duration is greater than or equal to 20 seconds.")


# In[4]:


get_ipython().system('pip install streamlit')


# In[5]:


get_ipython().system('pip install pytube')


# In[7]:


get_ipython().system('pip install moviepy')


# In[9]:


get_ipython().system('pip install zipfile')


# In[10]:


get_ipython().system('pip install smtplib')


# In[11]:


import streamlit as st
from email.message import EmailMessage
import os
from pytube import YouTube, Search
import moviepy.editor as mp
from moviepy.editor import AudioFileClip, concatenate_audioclips
import zipfile
import smtplib

# Function to check constraints
def check_constraints(number_of_videos, audio_duration):
    if int(number_of_videos) >= 10 and int(audio_duration) >= 20:
        return True
    else:
        return False

# Function to send email
def send_email(sender_email, sender_password, recipient_email, subject, message, file_name, file_data):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg.set_content(message)
    msg.add_attachment(file_data, maintype="application", subtype="zip", filename=file_name)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
            return True
    except smtplib.SMTPAuthenticationError:
        st.error("Failed to authenticate. Please check your email and password.")
        return False
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return False

# Streamlit setup
st.set_page_config(layout='centered', page_title='Mashup')
st.header("MASHUP")

# Form input
with st.form("form1", clear_on_submit=True):
    singer_name = st.text_input("Singer Name")
    number_of_videos = st.text_input("Number of Videos")
    duration = st.text_input("Duration of each video (in sec)")
    email = st.text_input("Email ID", placeholder='example@gmail.com')
    submit = st.form_submit_button("Submit")

# Main functionality
if submit:
    if check_constraints(number_of_videos, duration):
        sender_email = "riya.mashupproject@gmail.com"  # Your Gmail address
        sender_password = "helloabcd"   # Your Gmail password
        subject = "Mashup Results"
        message = f"This is a mashup zip file of the audios of the singer {singer_name}.\n\nDone By -\nKhushi Prasad\n102183044\nCOE20"

        path = os.getcwd()
        search_results = []
        vid_files = []
        aud_files = []
        sub_files = []
        aud_clip = []

        s = Search(singer_name)
        for v in s.results:
            search_results.append(v.watch_url)

        for i in range(int(number_of_videos)):
            yt = YouTube(search_results[i])
            fin = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
            os.rename(fin, f'Video-{i}.mp4')
            vid_files.append(f'Video-{i}.mp4')

        for file in vid_files:
            clip = mp.VideoFileClip(os.path.join(path, file))
            clip.audio.write_audiofile(os.path.join(path, f'{os.path.splitext(file)[0]}.mp3'))
            aud_files.append(f'{os.path.splitext(file)[0]}.mp3')

        for file in aud_files:
            sub_file = AudioFileClip(os.path.join(path, file))
            final = sub_file.subclip(0, int(duration))
            final.write_audiofile(os.path.join(path, f'Sub{file}'))
            sub_files.append(f'Sub{file}')

        for file in sub_files:
            aud_clip.append(AudioFileClip(os.path.join(path, file)))

        final_audio = concatenate_audioclips(aud_clip)
        final_audio.write_audiofile(os.path.join(path, 'Mashup.mp3'))

        with zipfile.ZipFile("mashup.zip", "w", zipfile.ZIP_DEFLATED) as zip:
            zip.write(os.path.join(path, 'Mashup.mp3'))

        with open("mashup.zip", "rb") as f:
            file_data = f.read()

        if send_email(sender_email, sender_password, email, subject, message, "mashup.zip", file_data):
            st.success("Email Sent Successfully!")
    else:
        st.error("Please ensure that the number of videos is greater than or equal to 10 and the duration is greater than or equal to 20 seconds.")import streamlit as st
from email.message import EmailMessage
import os
from pytube import YouTube, Search
import moviepy.editor as mp
from moviepy.editor import AudioFileClip, concatenate_audioclips
import zipfile
import smtplib

# Function to check constraints
def check_constraints(number_of_videos, audio_duration):
    if int(number_of_videos) >= 10 and int(audio_duration) >= 20:
        return True
    else:
        return False

# Function to send email
def send_email(sender_email, sender_password, recipient_email, subject, message, file_name, file_data):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg.set_content(message)
    msg.add_attachment(file_data, maintype="application", subtype="zip", filename=file_name)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
            return True
    except smtplib.SMTPAuthenticationError:
        st.error("Failed to authenticate. Please check your email and password.")
        return False
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return False

# Streamlit setup
st.set_page_config(layout='centered', page_title='Mashup')
st.header("MASHUP")

# Form input
with st.form("form1", clear_on_submit=True):
    singer_name = st.text_input("Singer Name")
    number_of_videos = st.text_input("Number of Videos")
    duration = st.text_input("Duration of each video (in sec)")
    email = st.text_input("Email ID", placeholder='example@gmail.com')
    submit = st.form_submit_button("Submit")

# Main functionality
if submit:
    if check_constraints(number_of_videos, duration):
        sender_email = "riya.mashupproject@gmail.com"  # Your Gmail address
        sender_password = "helloabcd"   # Your Gmail password
        subject = "Mashup Results"
        message = f"This is a mashup zip file of the audios of the singer {singer_name}.\n\nDone By -\nKhushi Prasad\n102183044\nCOE20"

        path = os.getcwd()
        search_results = []
        vid_files = []
        aud_files = []
        sub_files = []
        aud_clip = []

        s = Search(singer_name)
        for v in s.results:
            search_results.append(v.watch_url)

        for i in range(int(number_of_videos)):
            yt = YouTube(search_results[i])
            fin = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
            os.rename(fin, f'Video-{i}.mp4')
            vid_files.append(f'Video-{i}.mp4')

        for file in vid_files:
            clip = mp.VideoFileClip(os.path.join(path, file))
            clip.audio.write_audiofile(os.path.join(path, f'{os.path.splitext(file)[0]}.mp3'))
            aud_files.append(f'{os.path.splitext(file)[0]}.mp3')

        for file in aud_files:
            sub_file = AudioFileClip(os.path.join(path, file))
            final = sub_file.subclip(0, int(duration))
            final.write_audiofile(os.path.join(path, f'Sub{file}'))
            sub_files.append(f'Sub{file}')

        for file in sub_files:
            aud_clip.append(AudioFileClip(os.path.join(path, file)))

        final_audio = concatenate_audioclips(aud_clip)
        final_audio.write_audiofile(os.path.join(path, 'Mashup.mp3'))

        with zipfile.ZipFile("mashup.zip", "w", zipfile.ZIP_DEFLATED) as zip:
            zip.write(os.path.join(path, 'Mashup.mp3'))

        with open("mashup.zip", "rb") as f:
            file_data = f.read()

        if send_email(sender_email, sender_password, email, subject, message, "mashup.zip", file_data):
            st.success("Email Sent Successfully!")
    else:
        st.error("Please ensure that the number of videos is greater than or equal to 10 and the duration is greater than or equal to 20 seconds.")


# In[ ]:




