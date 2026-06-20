import streamlit as st
import yt_dlp
import os
import shutil

# Page Configuration
st.set_page_config(page_title="Universal Video Downloader", page_icon="🚀", layout="centered")

# --- SESSION STATE INITIALIZATION ---
if 'video_ready' not in st.session_state:
    st.session_state.video_ready = False

# Custom CSS for Professional Look
custom_css = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .main-title {
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #FF0000;
        font-weight: 900;
        font-size: 3rem;
        margin-bottom: 0px;
        padding-bottom: 0px;
    }
    .sub-title {
        text-align: center;
        color: #888888;
        font-size: 16px;
        margin-bottom: 30px;
        font-style: italic;
    }
    div[data-baseweb="input"] {
        border-radius: 12px !important;
        border: 1.5px solid #ccc !important;
        background-color: #f9f9f9 !important;
    }
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #FF416C, #FF4B2B);
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        border: none;
        padding: 12px 0px;
        transition: 0.3s all ease-in-out;
    }
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0px 5px 15px rgba(255, 75, 43, 0.4);
        color: white;
        border: none;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)
st.markdown('<h1 class="main-title">▶️ Pro Video Downloader</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Mac, iOS & Windows Compatible - Large Files Supported</p>', unsafe_allow_html=True)

# User Input
url = st.text_input("🔗 Paste YouTube Video Link Here:", placeholder="https://www.youtube.com/watch?v=...")

# Video download function
def download_yt_video(video_url, output_name="video_file.mp4"):
    if os.path.exists(output_name):
        os.remove(output_name)
        
    ydl_opts = {
        'format': 'bestvideo[ext=mp4][vcodec^=avc1]+bestaudio[ext=m4a]/best[ext=mp4][vcodec^=avc1]/best[ext=mp4]/best', 
        'outtmpl': output_name,
        'merge_output_format': 'mp4',
        'overwrites': True,
        'quiet': True,
        'n_check_sig': True,
        'socket_timeout': 600,         
        'retries': 50,                 
        'fragment_retries': 50,        
        'http_chunk_size': 10485760,
        
        # --- ULTIMATE ANTI-BAN TRICK FOR CLOUD ---
        'nocheckcertificate': True,
        # YouTube ko lagay ga ke request iPhone, Android aur Web se aa rahi hai
        'extractor_args': {'youtube': ['player_client=ios,android,web']},
        # Identity ko bilkul aam Google Chrome browser jaisa bana diya
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

# Start Process Button
if st.button("🚀 Fetch & Process Video"):
    if not url.strip():
        st.warning("⚠️ Please enter a YouTube video link first!")
    else:
        try:
            st.session_state.video_ready = False 
            
            with st.spinner("⏳ Downloading and merging the video. Please wait..."):
                download_yt_video(url)
            
            st.session_state.video_ready = True
            st.success("✅ Video is ready! Use the button below to save it.")
            
        except Exception as e:
            st.error(f"❌ Error: {e}")

# --- DIRECT MAC DOWNLOAD LOGIC ---
if st.session_state.video_ready and os.path.exists("video_file.mp4"):
    
    st.write("---")
    if st.button("⬇️ Save Video to 'Downloads' Folder"):
        try:
            with st.spinner("Saving to Downloads..."):
                mac_downloads_folder = os.path.expanduser("~/Downloads")
                final_file_path = os.path.join(mac_downloads_folder, "My_Downloaded_Video.mp4")
                
                shutil.copy("video_file.mp4", final_file_path)
                
            st.success(f"🎉 Success! The video has been saved to your local 'Downloads' folder.")
            st.info("Check your system's 'Downloads' directory to view the file!")
            
        except Exception as e:
            st.error(f"❌ Error saving the file: {e}")
