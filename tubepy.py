from tkinter import *
import pytube
from pytube import YouTube
from moviepy.editor import AudioFileClip
# Programa tkinter para descargat en .mp3 canciones de youtube
class App:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Tubepy echo por Jota")
        self.ventana.geometry("500x300")
        self.ventana.resizable(False, False)
        self.formulario()
        self.ventana.mainloop()

    def formulario(self):
        self.label2 = Label(self.ventana, text="Tubepy echo por Jota").pack()
        self.label = Label(self.ventana, text="Url de la cancion: ").pack()
        self.link = Entry(self.ventana, width=50)
        self.link.pack()
        self.boton = Button(self.ventana, text="Descargar", command=self.descargar).pack()
        self.btnLimpiar = Button(self.ventana, text="Limpiar", command=self.limpiar).pack()
    def descargar(self):
        url = self.link.get()
        video = YouTube(url)
        audio = video.streams.filter(only_audio=True).first()
        download_path = audio.download(output_path="mp4")
        nombre = video.title.replace(" ", "_")

        # Convertir el archivo descargado a .mp3
        clip = AudioFileClip(download_path)
        clip.write_audiofile("mp3/"+nombre+".mp3")
        clip.close()
    
    def limpiar(self):
        self.link.delete(0, END)
        
if __name__ == '__main__':
    run = App()