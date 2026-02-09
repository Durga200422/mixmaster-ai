# 🎵 MixMaster AI: Automated YouTube Mixtape Studio


## 🎯 Overview
MixMaster AI is an end-to-end content automation tool designed to eliminate the manual grind of creating YouTube mixtapes. By combining a high-performance FastAPI backend with an intuitive Streamlit dashboard, it allows creators to transform raw audio tracks into a publish-ready video with seamless transitions and automated timestamps.


## 🔗 Live Demo
[https://durga200422-mixmaster-ai-srcmixmasteruiapp-aebeqc.streamlit.app/) (See how raw audio tracks turn into a YouTube-ready mixtape in seconds.)


## 🌟 Why I Built This
As a graduate specializing in CSE-AIML from Manav Rachna University, I recognized a significant bottleneck in digital content workflows. Creators often spend hours in heavy video editors performing repetitive tasks: merging audio, adding crossfades, and manually calculating timestamps for YouTube chapters. I developed MixMaster AI to automate these technical hurdles, allowing creators to focus entirely on artistic curation.

## 🚀 Key Features
- **Smart Audio Merging:** Automatically normalizes track volumes and applies custom crossfades (0ms to 5000ms) for professional-grade transitions using Pydub.
- **Dynamic Video Rendering:** Overlays the audio mix onto a high-quality static background to generate an MP4 file via MoviePy and FFmpeg.
- **Automated Tracklists:** Generates perfect YouTube-ready descriptions with HH:MM:SS timestamps automatically calculated from the mix logic.
- **Modular API Architecture:** Uses a decoupled FastAPI backend, making the core logic scalable and ready for integration with other frontends.
- **Session Management:** Uses unique UUIDs to handle multiple user requests simultaneously without file collisions.

## 🛠️ The Tech Stack
- **Backend:** Python, FastAPI (Asynchronous request handling)
- **Frontend:** Streamlit (Custom CSS-styled Studio UI)
- **Audio/Video Engines:** Pydub, MoviePy, FFmpeg
- **Environment:** uv (Next-generation Python package manager)
- **Data Validation:** Pydantic Settings & BaseModels

## 📂 Project Structure
```
mixmaster-ai/                      
├── main.py               # FastAPI Entry Point
├── run.bat               # One-click Studio Launcher
├── src/
│   └── mixmaster/
│        ├── api/          # Endpoints & Pydantic Schemas
│        ├── core/         # The "Brain" (Audio & Video Processing)
│        ├── ui/           # Streamlit Dashboard Code
│        └── utils/        # Cleanup, Logging, & Global Settings
├── data/                 # Local Storage (Uploads/Exports)
└── tests/                # Pytest Suite for Logic Validation

```

## ⚙️ How to Run Locally
### Prerequisites

- **Python 3.10+**
- **FFmpeg:** Ensure FFmpeg is installed and added to your system path.
- **uv:** Recommended for high-performance dependency management.

### Installation

#### 1. Clone the Repo:

```
git clone https://github.com/your-username/mixmaster-ai.git
cd mixmaster-ai
```
#### 2. Setup Environment:

```
uv venv
.venv\Scripts\activate  # Windows
uv sync

```
#### 3. Launch the Studio: Simply double-click the run.bat file or run:

```
.\run.bat

```

## 🧪 Testing
Quality assurance is integrated into the development cycle. Run the following to verify the timestamp logic and API health:

```
pytest
```

## 📈 Future Roadmap
- **🎨 AI Visuals:** Integrate Stable Diffusion to generate background art based on audio mood.
- **☁️ Cloud Storage:** Transition from local filesystem to AWS S3 for enterprise scalability.
- **🥁 Audio Analysis:** Utilize Librosa to detect BPM and automate beat-matched transitions.

## 👨‍💻 Author
Narapureddy Durga Prasad Reddy
Graduate in CSE-AIML | Manav Rachna University

## ⭐ If you like this project
Give it a star on GitHub and share it with creators who hate editing mixtapes manually!
