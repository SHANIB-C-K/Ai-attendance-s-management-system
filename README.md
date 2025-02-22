# 🎯 Smart Attendance System

> _Revolutionizing attendance tracking with facial recognition_

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/OpenCV-4.x-green?style=for-the-badge&logo=opencv"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge"/>
</div>

## 🌟 Overview

This innovative project implements an attendance system using cutting-edge face recognition technology. It captures video from a webcam, detects faces in real-time, and records attendance in a CSV file. The system leverages the K-Nearest Neighbors (KNN) algorithm for accurate face recognition.

## ✨ Features

- 📸 **Real-time Face Detection** - Instant face capture and recognition
- ⚡ **Lightning Fast Processing** - Powered by KNN algorithm
- 📊 **Automated Logging** - Attendance with timestamps
- 🔊 **Voice Feedback** - Audio confirmations for better UX
- 🎯 **High Accuracy** - Reliable recognition system

## 🛠️ Requirements

- 🐍 Python 3.x
- 📷 OpenCV
- 🤖 scikit-learn
- 🔢 NumPy
- 🥒 Pickle
- 📝 CSV
- 🪟 Windows (for SAPI voice)

## 📦 Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/SHANIB-C-K/Ai-attendance-s-management-system.git
   cd Ai-attendance-s-management-system.git
   ```

2. **Install Dependencies:**

   ```bash
   pip install opencv-python scikit-learn numpy
   ```

3. **Setup Face Detection:**
   > Download the Haar Cascade file and place it in the project directory

## 🚀 Usage

1. **Register New User:**

   ```bash
   python main.py
   ```

2. **Launch Attendance System:**

   ```bash
   python attendance.py
   ```

3. **Controls:**
   - Press `O` - Mark attendance
   - Press `Q` - Quit application

## 💾 Data Storage

Attendance records are automatically stored in the `Attendance` directory as CSV files, organized by date.

## 🤝 Contributing

We welcome contributions! Feel free to:

- Submit issues
- Propose new features
- Send pull requests

## 📄 License

This project is protected under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenCV** - For powerful computer vision capabilities
- **scikit-learn** - For robust machine learning algorithms
- **SAPI** - For seamless voice feedback integration
