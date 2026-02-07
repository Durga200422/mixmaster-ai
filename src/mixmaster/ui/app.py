import streamlit as st
import requests
import os
from pathlib import Path
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="MixMaster AI | Studio",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM STYLING ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
    }
    .stDownloadButton>button {
        width: 100%;
        border-radius: 5px;
    }
    .status-box {
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #31333F;
        background-color: #1E1E1E;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR SETTINGS ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3659/3659744.png", width=80)
    st.title("Studio Settings")
    st.markdown("---")
    
    st.subheader("🎚️ Audio Mixing")
    crossfade = st.select_slider(
        "Crossfade Duration (ms)",
        options=[0, 500, 1000, 2000, 3000, 5000],
        value=2000,
        help="The overlap duration between two audio tracks."
    )
    
    st.subheader("🎬 Video Quality")
    fps_choice = st.radio("Frame Rate", [5, 12, 24], index=0, horizontal=True, help="Higher FPS increases render time.")
    
    st.markdown("---")
    st.info("💡 **Pro Tip:** Ensure your audio files have a consistent bitrate for the best quality mix.")

# --- MAIN INTERFACE ---
st.title("🎵 MixMaster AI")
st.caption("Automated YouTube Mixtape Studio | Powered by FastAPI & MoviePy")

tab1, tab2, tab3 = st.tabs(["🚀 Generator", "📋 Instructions", "🛠️ System Status"])

with tab1:
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.subheader("📤 Step 1: Upload Assets")
        
        with st.container(border=True):
            uploaded_audio = st.file_uploader(
                "Audio Tracks (Order matters)", 
                type=["mp3", "wav"], 
                accept_multiple_files=True,
                help="The mix will be generated in the order files are uploaded."
            )
            
            if uploaded_audio:
                with st.expander("🔍 View Selected Tracks", expanded=False):
                    for i, file in enumerate(uploaded_audio):
                        st.text(f"{i+1}. {file.name} ({(file.size/1024/1024):.2f} MB)")

            uploaded_image = st.file_uploader(
                "Background Image", 
                type=["jpg", "png", "jpeg"],
                help="This image will be the static visual for the entire video."
            )
            
            if uploaded_image:
                st.image(uploaded_image, caption="Background Preview", use_container_width=True)

    with col2:
        st.subheader("⚡ Step 2: Generation")
        
        # Action Button
        generate_btn = st.button("✨ Create Mixtape", use_container_width=True)
        
        if generate_btn:
            if not uploaded_audio or not uploaded_image:
                st.warning("⚠️ Please provide both audio tracks and a background image to proceed.")
            else:
                progress_text = "Step 1/2: Merging Audio Tracks..."
                my_bar = st.progress(0, text=progress_text)
                
                try:
                    files = []
                    for audio in uploaded_audio:
                        files.append(("audio_files", (audio.name, audio.getvalue(), audio.type)))
                    files.append(("image_file", (uploaded_image.name, uploaded_image.getvalue(), uploaded_image.type)))

                    # Backend Request
                    start_time = time.time()
                    response = requests.post("http://localhost:8000/api/v1/create-mixtape", files=files)
                    
                    if response.status_code == 200:
                        data = response.json()
                        my_bar.progress(100, text="Generation Complete!")
                        st.balloons()
                        
                        v_path = Path(data["video_path"])
                        a_path = Path(data["audio_path"])

                        if v_path.exists():
                            st.success(f"✅ Success! Rendered in {int(time.time() - start_time)}s")
                            
                            st.subheader("🎬 Final Preview")
                            st.video(str(v_path))
                            
                            with st.container(border=True):
                                st.subheader("📝 YouTube Description")
                                description = "\n".join(data["youtube_description"])
                                st.code(description, language="text")
                                st.button("📋 Copy to Clipboard", on_click=lambda: st.write("Copied! (Simulated)"))

                            st.subheader("📥 Downloads")
                            dl1, dl2 = st.columns(2)
                            with dl1:
                                with open(a_path, "rb") as f:
                                    st.download_button("🎵 Download MP3", f, f"mixtape_{data['session_id'][:8]}.mp3", "audio/mpeg")
                            with dl2:
                                with open(v_path, "rb") as f:
                                    st.download_button("📽️ Download MP4", f, f"mixtape_{data['session_id'][:8]}.mp4", "video/mp4")
                        else:
                            st.error("The file was processed but could not be located on the server disk.")
                    else:
                        st.error(f"Backend Processing Error: {response.text}")
                
                except Exception as e:
                    st.error(f"🚫 Connection Error: {str(e)}")
                    st.info("Check if your FastAPI server is running at http://localhost:8000")

with tab2:
    st.header("How to use MixMaster AI")
    st.markdown("""
    1. **Upload Tracks:** Add the songs you want in your mix. They will be played in the order you select them.
    2. **Choose an Image:** This is the visual element of your video. High-resolution 16:9 images work best for YouTube.
    3. **Adjust Crossfade:** Use the sidebar to set the transition time between songs.
    4. **Generate:** Hit the button and wait. The system merges the audio, calculates timestamps, and renders the video.
    5. **Publish:** Use the generated timestamps in your YouTube video description for chapters!
    """)

with tab3:
    st.header("System Health")
    c1, c2, c3 = st.columns(3)
    try:
        health = requests.get("http://localhost:8000/api/v1/health").json()
        c1.metric("API Status", health.get("status", "Unknown").upper())
    except:
        c1.metric("API Status", "OFFLINE", delta_color="inverse")
    
    c2.metric("Storage Mode", "Local Filesystem")
    c3.metric("Renderer", "MoviePy / FFmpeg")

# --- FOOTER ---
st.divider()
footer_col1, footer_col2 = st.columns(2)
with footer_col1:
    st.caption(f"© 2026 MixMaster AI Studio | Professional Edition")
with footer_col2:
    st.markdown("<div style='text-align: right;'><span style='font-size: 0.8em;'>Built by Durga Prasad Reddy</span></div>", unsafe_allow_html=True)