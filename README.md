# YoutubeVideo_Downloader

# 🎥 Universal Pro Video Downloader

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://youtubevideodownloader-9zm4pquuhtggyf4pq3dysp.streamlit.app/)

A sleek, professional, and high-performance YouTube video downloader built with **Python**, **Streamlit**, and **yt-dlp**. 

This application is engineered to handle video files and ensures that every downloaded video is strictly formatted with the **H.264 (AVC) codec**, making it universally compatible across Mac (QuickTime), iOS, Android, and Windows devices.

---

## 🌐 Live Demo
You can try the live version of the application here: 
**[Universal Pro Video Downloader - Live App](https://youtubevideodownloader-9zm4pquuhtggyf4pq3dysp.streamlit.app/)**

*(Note: The live cloud version is best for short to medium-length videos. For massive 1.5GB+ files, please run the app locally as described below).*

---

## ✨ Key Features

* 🚀 **Universal Compatibility:** Forces H.264 video encoding. No more "Unsupported Format" errors on Apple devices or QuickTime Player.
* 💾 **Smart Local Downloading:** When run locally, it uses Python's `shutil` module to instantly transfer multi-gigabyte files directly to your system's `Downloads` directory, bypassing browser limits.
* 🎨 **Premium UI/UX:** Features a modern, clean interface with custom CSS gradient buttons, hover animations, and a distraction-free layout.
* 🛡️ **Anti-Timeout Architecture:** Configured with extended socket timeouts (600s), 50x retry limits, and 10MB chunked downloading for maximum stability.
* 🎵 **Highest Quality:** Automatically fetches the best available video stream and the best audio stream, then seamlessly merges them.

---

## 🛠️ Prerequisites (For Local Execution)

Before you begin, ensure you have the following installed on your machine:

1. **Python 3.8** or higher.
2. **FFmpeg:** This is **mandatory**. `yt-dlp` requires FFmpeg to merge the high-quality video and audio streams. 
   * **Mac:** `brew install ffmpeg`
   * **Windows:** Download from the [official FFmpeg site](https://ffmpeg.org/download.html) and add it to your system PATH.
   * **Linux:** `sudo apt install ffmpeg`

---

