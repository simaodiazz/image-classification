from button import Button
from PIL import Image, ImageTk
from tkinter import filedialog


class SelectImage(Button):

    '''
    TODO
    Carregar aqui o botão e blblablaabllablbalablab
    '''
    def __init__(self, widget):
        pass

    def action(self):
        # Abre janela para selecionar imagem
        file_path = filedialog.askopenfilename(title="Selecionar Imagem", filetypes=(("Imagens", "*.jpg;*.jpeg;*.png"),))
        # Carrega imagem na janela
        self.image = Image.open(file_path)
        self.image = self.image.resize((250, 250))
        self.image = ImageTk.PhotoImage(self.image)
        self.label_image.configure(image=self.image)
        self.label_image.image = self.image
