import tkinter as tk
from tkinter import filedialog

def select_video():
    """Kullanicinin bir video dosyasi seçmesini sağlar."""
    root = tk.Tk()
    root.withdraw()  # Ana pencereyi gizle
    video_path = filedialog.askopenfilename(title="Bir video dosyasi seç", filetypes=[("Video dosyalari", "*.mp4 *.avi *.mkv")])
    return video_path

def get_language_choice():
    """Dil seçimi için kullanicidan giriş alir."""
    root = tk.Tk()
    root.title("Dil Seçimi")
    
    choice = tk.StringVar(value="tr")
    
    def set_choice(value):
        choice.set(value)
        root.destroy()

    tk.Label(root, text="Altyazi dili seçin:").pack()
    tk.Button(root, text="Türkçe", command=lambda: set_choice("tr")).pack()
    tk.Button(root, text="İngilizce", command=lambda: set_choice("en")).pack()
    
    root.mainloop()
    
    return choice.get()
