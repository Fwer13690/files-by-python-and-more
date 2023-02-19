import tkinter as tk
import time

class Cronometro:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cronómetro")
        self.root.configure(bg='#1B2631')
        self.label = tk.Label(self.root, text="00:00:00", font=("Arial", 50), fg='#F8F9F9', bg='#1B2631')
        self.label.pack(pady=20)
        self.inicio = 0
        self.contando = False

        btn_iniciar = tk.Button(self.root, text="Iniciar", command=self.iniciar)
        btn_iniciar.pack(side=tk.LEFT, padx=20)

        btn_detener = tk.Button(self.root, text="Detener", command=self.detener)
        btn_detener.pack(side=tk.RIGHT, padx=20)

        self.root.protocol("WM_DELETE_WINDOW", self.cerrar)

    def iniciar(self):
        if not self.contando:
            self.inicio = time.time()
            self.contando = True
            self.actualizar()

    def detener(self):
        self.contando = False

    def actualizar(self):
        if self.contando:
            duracion = time.time() - self.inicio
            minutos, segundos = divmod(duracion, 60)
            horas, minutos = divmod(minutos, 60)
            tiempo = "{:02d}:{:02d}:{:02d}".format(int(horas), int(minutos), int(segundos))
            self.label.configure(text=tiempo)
            self.label.after(1000, self.actualizar)

    def cerrar(self):
        self.root.destroy()

cronometro = Cronometro()
cronometro.root.mainloop()
