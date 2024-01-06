from tkinter import END, messagebox, ttk
from ttkthemes import ThemedTk
import pytube
from pytube import YouTube
from moviepy.editor import AudioFileClip
# Programa tkinter para descargat en .mp3 canciones de youtube
class App:
    def __init__(self):
        self.ventana = ThemedTk(theme="plastik")
        self.ventana.title("Tubepy echo por Jota")
        self.ventana.geometry("500x150")
        self.ventana.resizable(False, False)
        self.formulario()
        self.ventana.mainloop()
    def formulario(self):
        print("Programa Tubepy iniciado!\t")
        self.label2 = ttk.Label(self.ventana, text="Tubepy echo por Jota").pack()
        self.separador = ttk.Label(self.ventana, text="").pack()

        self.label = ttk.Label(self.ventana, text="Url de la cancion: ").pack()
        self.link = ttk.Entry(self.ventana, width=50)
        self.link.pack()
        self.boton = ttk.Button(self.ventana, text="Descargar", command=self.descargar).place(x=100, y=90)
        self.btnLimpiar = ttk.Button(self.ventana, text="Limpiar", command=self.limpiar).place(x=180, y=90)
    def descargar(self):
        url = self.link.get()
        # Proceso de validacion de la url
        if self.validarUrl(url) == True: 
            video = YouTube(url)
            audio = video.streams.filter(only_audio=True).first()
            download_path = audio.download(output_path="mp4")
            nombre = video.title.replace(" ", "_").replace("|", "")
            print("Descargando: "+nombre)
            # Convertir el archivo descargado a .mp3
            clip = AudioFileClip(download_path)
            clip.write_audiofile("mp3/"+nombre+".mp3")
            clip.close()
            messagebox.showinfo("Tubepy", "Descarga completada")
            self.limpiar()
            print("Recuerda que cada canción se descarga en .mp3/.mp4 en sus respectivas carpetas.\nPrograma Tubepy finalizado!\nEcho por Jota.")
        else:
            messagebox.showerror("Tubepy", "Url invalida")
    def validarUrl(self, url):
        import validators
        if validators.url(url) == True:
            print("Url valida")
            return True
        else:
            print("Url invalida")
            return False
    def limpiar(self):
        self.link.delete(0, END)