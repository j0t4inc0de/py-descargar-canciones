import tkinter as tk
from tkinter import ttk, messagebox
import threading
import os
from yt_dlp import YoutubeDL

class TubePyApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("TubePy MP3 Downloader")
        self.window.geometry("500x150")
        
        # Configurar interfaz
        self.create_widgets()
        self.check_directories()
        
    def check_directories(self):
        os.makedirs("mp3", exist_ok=True)
        
    def create_widgets(self):
        # Entrada de URL
        ttk.Label(self.window, text="URL de YouTube:").pack(pady=5)
        self.url_entry = ttk.Entry(self.window, width=50)
        self.url_entry.pack(pady=5)
        
        # Botones
        btn_frame = ttk.Frame(self.window)
        btn_frame.pack(pady=10)
        
        ttk.Button(
            btn_frame, 
            text="Descargar", 
            command=self.start_download
        ).pack(side="left", padx=5)
        
        ttk.Button(
            btn_frame, 
            text="Limpiar", 
            command=self.clear_input
        ).pack(side="left", padx=5)
        
    def start_download(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("Error", "Ingresa una URL válida")
            return
            
        threading.Thread(
            target=self.download_audio, 
            args=(url,), 
            daemon=True
        ).start()
        
    def download_audio(self, url):
        try:
            ydl_opts = {
                'format': 'bestaudio[ext=m4a]',
                'outtmpl': os.path.join("mp3", '%(title)s.%(ext)s'),
                'noplaylist': True,
            }
            
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                
            messagebox.showinfo("Éxito", "Descarga completada")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")
            
    def clear_input(self):
        self.url_entry.delete(0, tk.END)

if __name__ == "__main__":
    app = TubePyApp()
    app.window.mainloop()