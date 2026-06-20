# File Name: downloader.py
import yt_dlp
import os

def download_video_from_youtube(url, filename="video_file.mp4"):
    """
    YouTube URL se video download karne ka function.
    Return karega: (Success_Boolean, Message_String)
    """
    # Pehle se mojood file ko delete karein
    if os.path.exists(filename):
        os.remove(filename)

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best', 
        'outtmpl': filename,
        # Note: Agar aap isko Streamlit Cloud par deploy karein ge to 'cookiesfrombrowser' error dega
        # is liye agar error aaye to is line ko comment kar dijiye ga. Local PC par theek chalega.
        'cookiesfrombrowser': ('chrome',), 
        'merge_output_format': 'mp4',
        'overwrites': True,
        'quiet': True, # Streamlit mein background clean rakhne ke liye True kiya hai
        'n_check_sig': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return True, f"Video successfully downloaded as '{filename}'"
    except Exception as e:
        return False, str(e)