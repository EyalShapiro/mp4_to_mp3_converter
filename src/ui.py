import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from converter import VideoToAudioConverter

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def get_full_path(folder_path):
    """Returns the absolute path of a folder, even if relative."""
    return (
        os.path.abspath(folder_path)
        if os.path.isabs(folder_path)
        else os.path.join(SCRIPT_DIR, folder_path)
    )


FAVICON = "assets/audio-converting.ico"


class ConverterUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(get_full_path(FAVICON))
        self.config(bg="#d8d8d8")
        self.title("ממיר MP4 ל-MP3")
        self.geometry("400x250")
        self.resizable(False, False)

        self.input_folder = tk.StringVar()
        self.output_folder = tk.StringVar()

        tk.Label(self, text="תיקיית מקור (MP4):").pack(pady=5)
        tk.Entry(self, textvariable=self.input_folder, width=50).pack(pady=5)
        tk.Button(self, text="בחר תיקייה", command=self.browse_input).pack()

        tk.Label(self, text="תיקיית יעד (MP3):").pack(pady=10)
        tk.Entry(self, textvariable=self.output_folder, width=50).pack(pady=5)
        tk.Button(self, text="בחר תיקייה", command=self.browse_output).pack()

        tk.Button(
            self,
            text="המר",
            command=self.convert_files,
            bg="green",
            fg="white",
            width=15,
        ).pack(pady=20)

    def browse_input(self):
        folder = filedialog.askdirectory(title="בחר תיקיית מקור")
        if folder:
            self.input_folder.set(folder)

    def browse_output(self):
        folder = filedialog.askdirectory(title="בחר תיקיית יעד")
        if folder:
            self.output_folder.set(folder)

    def convert_files(self):
        input_folder = self.input_folder.get()
        output_folder = self.output_folder.get()

        if not input_folder or not output_folder:
            messagebox.showerror("שגיאה", "אנא בחר את שתי התיקיות")
            return

        VideoToAudioConverter.convert_folder(input_folder, output_folder)
        messagebox.showinfo("הצלחה", "הקבצים הומרו בהצלחה!")
