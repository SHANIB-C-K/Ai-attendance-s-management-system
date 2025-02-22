# Attendance System using Face Recognition

## Overview
This project implements an attendance system using face recognition technology. It captures video from a webcam, detects faces, and records attendance in a CSV file. The system utilizes the K-Nearest Neighbors (KNN) algorithm for face recognition.

## Features
- Real-time face detection and recognition.
- Attendance logging with timestamps.
- User-friendly interface with audio feedback.

## Requirements
- Python 3.x
- OpenCV
- scikit-learn
- NumPy
- Pickle
- CSV
- Windows (for SAPI voice)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/SHANIB-C-K/Ai-attendance-s-management-system.git
   cd Ai-attendance-s-management-system.git
   ```

2. Install the required packages:
   ```bash
   pip install opencv-python scikit-learn numpy
   ```

3. Download the Haar Cascade file for face detection and place it in the project directory.

## Usage
1. Run the `main.py` file to register a new user:
   ```bash
   python main.py
   ```

2. Start the attendance system by running `attendance.py`:
   ```bash
   python attendance.py
   ```

3. Press 'o' to mark attendance and 'q' to quit the application.

## Data Storage
Attendance records are stored in the `Attendance` directory as CSV files, named with the date of attendance.

## Contributing
Feel free to submit issues or pull requests to improve the project.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- OpenCV for computer vision capabilities.
- scikit-learn for machine learning algorithms.
- SAPI for voice feedback.
