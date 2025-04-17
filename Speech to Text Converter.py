import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
import threading

class SpeechToText:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Speech to Text Converter")
        self.root.geometry("600x450")
        self.root.configure(bg='#000000')

        # Header
        self.header_frame = tk.Frame(self.root, bg='#ffffff')
        self.header_frame.pack(fill='x', padx=10, pady=10)
        self.header_label = tk.Label(self.header_frame, text="🎤 Speech to Text", font=('Arial', 18, 'bold'), bg='#ffffff', fg='#000000')
        self.header_label.pack(pady=10)

        # Status Label
        self.status_label = tk.Label(self.root, text="Status: Idle", font=('Arial', 12), bg='#000000', fg='#ffffff')
        self.status_label.pack(pady=10)

        # Text Box
        self.text_box = scrolledtext.ScrolledText(self.root, width=60, height=12, font=('Arial', 12), bg='#1c1c1c', fg='#ffffff', insertbackground='white', wrap=tk.WORD, relief=tk.FLAT, borderwidth=2)
        self.text_box.pack(padx=10, pady=10, fill='both', expand=True)

        # Buttons Frame
        self.button_frame = tk.Frame(self.root, bg='#000000')
        self.button_frame.pack(fill='x', padx=10, pady=10)

        button_style = {'font': ('Arial', 12, 'bold'), 'bg': '#ffffff', 'fg': '#000000', 'relief': 'flat', 'bd': 0, 'padx': 10, 'pady': 5}

        self.start_button = tk.Button(self.button_frame, text="🎙 Start", command=self.start_listening, **button_style, activebackground='#d9d9d9', highlightthickness=0, borderwidth=0)
        self.start_button.pack(side=tk.LEFT, fill='x', expand=True, padx=5, pady=5)
        self.start_button.config(highlightbackground="#ffffff", highlightcolor="#ffffff", borderwidth=2, relief="ridge", cursor="hand2")

        self.stop_button = tk.Button(self.button_frame, text="🛑 Stop", command=self.stop_listening, **button_style, activebackground='#d9d9d9', state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, fill='x', expand=True, padx=5, pady=5)
        self.stop_button.config(highlightbackground="#ffffff", highlightcolor="#ffffff", borderwidth=2, relief="ridge", cursor="hand2")

        self.clear_button = tk.Button(self.button_frame, text="🗑 Clear", command=self.clear_text, **button_style, activebackground='#d9d9d9')
        self.clear_button.pack(side=tk.LEFT, fill='x', expand=True, padx=5, pady=5)
        self.clear_button.config(highlightbackground="#ffffff", highlightcolor="#ffffff", borderwidth=2, relief="ridge", cursor="hand2")

        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.listening = False

    def start_listening(self):
        self.listening = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.status_label.config(text="Status: 🎙 Listening...", fg='#ffffff')
        threading.Thread(target=self.listen).start()

    def stop_listening(self):
        self.listening = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_label.config(text="Status: 🛑 Idle", fg='#ffffff')

    def listen(self):
        with self.microphone as source:
            try:
                self.status_label.config(text="Status: 🎙 Listening...", fg='#ffffff')
                audio = self.recognizer.listen(source)
                self.status_label.config(text="Status: ⏳ Processing...", fg='#ffffff')
                text = self.recognizer.recognize_google(audio)
                self.text_box.insert(tk.END, text + "\n")
            except sr.UnknownValueError:
                self.text_box.insert(tk.END, "Could not understand audio\n")
            except sr.RequestError as e:
               self.text_box.insert(tk.END, "Could not understand audio\n")
            finally:
                self.stop_listening()

    def clear_text(self):
        self.text_box.delete('1.0', tk.END)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    speech_to_text = SpeechToText()
    speech_to_text.run()
