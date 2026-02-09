# 🎵 MixMaster AI: Automated YouTube Mixtape Studio

MixMaster AI is an **end-to-end content automation tool** designed to eliminate the manual grind of creating YouTube mixtapes. By combining a high-performance **FastAPI backend** with an intuitive **Streamlit dashboard**, it allows creators to transform raw audio tracks into a publish-ready video with seamless transitions and automated timestamps.

---

## 🔗 Live Demo
👉 **[Try MixMaster AI Here](#https://durga200422-mixmaster-ai-srcmixmasteruiapp-aebeqc.streamlit.app/)**

---

## 🌟 Why I Built This

As a graduate specializing in **CSE-AIML from Manav Rachna University**, I recognized a significant bottleneck in digital content workflows. Creators often spend hours in heavy video editors performing repetitive tasks: merging audio, adding crossfades, and manually calculating timestamps for YouTube chapters.

**MixMaster AI automates these technical hurdles, allowing creators to focus entirely on artistic curation.**

---

## 🚀 Key Features

- 🎚️ **Smart Audio Merging**  
  Automatically normalizes track volumes and applies custom crossfades *(0ms to 5000ms)* for professional-grade transitions using **Pydub**.

- 🎥 **Dynamic Video Rendering**  
  Overlays the audio mix onto a high-quality static background to generate an MP4 file via **MoviePy** and **FFmpeg**.

- 🕒 **Automated Tracklists**  
  Generates perfect YouTube-ready descriptions with **HH:MM:SS timestamps** automatically calculated from the mix logic.

- 🧩 **Modular API Architecture**  
  Uses a decoupled **FastAPI backend**, making the core logic scalable and ready for integration with other frontends.

- 🧵 **Session Management**  
  Uses unique **UUIDs** to handle multiple user requests simultaneously without file collisions.

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|------------|
| **Backend** | Python, FastAPI (Async) |
| **Frontend** | Streamlit (Custom CSS Studio UI) |
| **Audio Engine** | Pydub |
| **Video Engine** | MoviePy, FFmpeg |
| **Environment** | uv (next-gen Python package manager) |
| **Validation** | Pydantic BaseModels & Settings |

---

## 📂 Project Structure

mixmaster-ai/
│
├── main.py # FastAPI Entry Point
├── run.bat # One-click Studio Launcher
│
├── src/
│ └── mixmaster/
│ ├── api/ # Endpoints & Pydantic Schemas
│ ├── core/ # Audio & Video Processing Logic
│ ├── ui/ # Streamlit Dashboard
│ └── utils/ # Cleanup, Logging, Settings
│
├── data/ # Uploads & Exports
└── tests/ # Pytest Suite


---

## ⚙️ How to Run Locally

### ✅ Prerequisites

- Python **3.10+**
- **FFmpeg** installed and added to system PATH
- **uv** package manager (recommended)

---

### 📦 Installation

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/mixmaster-ai.git
cd mixmaster-ai
2️⃣ Setup Environment
uv venv
.venv\Scripts\activate   # Windows
uv sync
3️⃣ Launch the Studio
Double-click run.bat or run:

.\run.bat
🧪 Testing
Run the test suite to verify timestamp logic and API health:

pytest
📈 Future Roadmap
🎨 AI Visuals — Generate background art using Stable Diffusion based on audio mood

☁️ Cloud Storage — Move from local filesystem to AWS S3

🥁 Audio Analysis — Use Librosa for BPM detection and beat-matched transitions

👨‍💻 Author
Narapureddy Durga Prasad Reddy
Graduate in CSE-AIML | Manav Rachna University

⭐ If you like this project
Give it a star on GitHub and share it with creators who hate editing mixtapes manually!
