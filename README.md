# Speech-to-Text Converter

## Overview
This **Speech-to-Text Converter** application converts your speech into text in real-time. Built using Python's `Tkinter` for the graphical user interface (GUI) and `speech_recognition` library for audio processing, this tool enables users to easily transcribe spoken words.

## Features
- **Real-Time Speech Recognition**: Convert spoken words to text as you speak.
- **Clear Text**: Clear the displayed text with the "Clear" button for a fresh session.
- **Simple and User-Friendly Interface**: Minimalist dark theme with easy-to-navigate buttons.
- **Start and Stop Buttons**: Control speech recognition with Start and Stop buttons.
- **Status Updates**: Real-time status of the application ("Listening", "Idle").
- **Error Handling**: Displays messages when audio cannot be understood or there’s a request error.

## Requirements
- Python 3.x
- `Tkinter` (usually comes pre-installed with Python)
- `speech_recognition` library
- `PyAudio` library for microphone input

## Installation

1. **Install Dependencies**:
   Install the required libraries using pip:
   ```bash
   pip install SpeechRecognition
   pip install pyaudio
