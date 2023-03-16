import tkinter as tk
from tkinter import ttk, filedialog
from PIL import ImageTk, Image

from buttons.select_image import SelectImage


class View:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Classificador de Imagens")
        self.root.geometry("400x400")
        self.root.configure(background="#353434")

        # Define o estilo do tema
        self.style = ttk.Style(self.root)
        self.style.theme_use("clam")
        self.style.configure("TButton",
                             padding=6,
                             relief="flat",
                             background="#1b1f23",
                             foreground="#ffffff",
                             font=("Segoe UI", 10, "bold"))
        self.style.map("TButton",
                       background=[("active", "#2ea44f")],
                       foreground=[("active", "#ffffff")])

        # Define a imagem inicial
        self.image = Image.open("C:/Users/simao/PycharmProjects/image-classification/resources/images/frog.jpg")
        self.image = self.image.resize((250, 250))
        self.image = ImageTk.PhotoImage(self.image)

        # Define a label para a imagem
        self.label_image = tk.Label(self.root, image=self.image)

        # Define os botões
        self.create_model_button = ttk.Button(self.root, text="Criar Modelo")
        self.load_model_button = ttk.Button(self.root, text="Carregar Modelo")
        self.select_image_button = ttk.Button(self.root, text="Selecionar Imagem", command=SelectImage.action())
        self.classify_image_button = ttk.Button(self.root, text="Classificar Imagem")

        # Define a zona de texto
        self.result_text = tk.Text(self.root, height=2, bg="#f6f8fa", borderwidth=0)

        # Posiciona os componentes na janela
        self.label_image.pack(pady=10)
        self.create_model_button.pack(pady=10)
        self.load_model_button.pack(pady=10)
        self.select_image_button.pack(pady=10)
        self.classify_image_button.pack(pady=10)
        self.result_text.pack(pady=10)

    def run(self):
        self.root.mainloop()
