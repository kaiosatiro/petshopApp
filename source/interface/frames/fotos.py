import os
import customtkinter as ctk
from tkinter import filedialog
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageShow
from io import BytesIO


class FrameFotos(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        # self.std_img = Image.open(os.path.realpath("source/interface/images/image.png"))
        self.std_img = Image.open(os.path.realpath("source/interface/images/w_plus.png"))

        self._id = 0
        self._new_foto_status = 0
        self._foto_dir = None
        self._img = self.std_img
        self._img_bkp = None
        self.foto = ctk.CTkImage(self._img, size=(18,18))#aspect ratio is: 12 : 7
                
        self.BT_label_foto = ctk.CTkButton(
            self, text="", image=self.foto,
            corner_radius=10, fg_color='transparent',
            width=420,
            height=280,
            state='disabled',
            command=self._show_foto
        )
        self.BT_label_foto.pack(expand=True, fill="both")
        

    def _show_foto(self):
        self._img.show()
        return
    

    def _get_foto(self):
        CTkMessagebox(title="Aviso!", message="Dê preferência aos formatos Jpeg e PNG!")
        get = filedialog.askopenfile(mode ='r', filetypes =[('Imagens', ['.jpeg', '.jpg', '.png',
                                                       '.tiff', '.tif', '.bmp'])])
        if not get:
            return None
        self._img = Image.open(os.path.realpath(get.name))
        self._foto_dir = os.path.realpath(get.name)
        self._set_foto()
        self._new_foto_status = 1
    

    def _set_foto(self):
         self.foto.configure(light_image=self._img, size=(420,280))


    def set_all(self, id_f:int|None, foto):
        if id_f:
            self._id = id_f
            img = Image.open(foto)
            self._img = img
            self._set_foto()
            self.BT_label_foto.configure(state='normal')
        else:
            self._id = 0
            self._img = self.std_img
            self.foto.configure(light_image=self.std_img, size=(18,18))
            self.BT_label_foto.configure(state='disabled')


    def get_dir(self):
        return self._foto_dir


    def get_id(self):
        return self._id
    

    def new_foto(self):
        return bool(self._new_foto_status)
   

    def ativa_adicao(self):
        self.foto.configure(light_image=self.std_img, size=(18,18))
        self.BT_label_foto.configure(command=self._get_foto, state='normal')
    

    def ativa_edicao(self):
        if self.get_id():
            self._img_bkp = self._img
        self.BT_label_foto.configure(command=self._get_foto, state='normal')
    

    def cancela_adicao(self):
        self._foto_nova_status = 0
        self.foto_dir = None
        self.foto.configure(light_image=self.std_img, size=(18,18))
        self.BT_label_foto.configure(command=self._show_foto, state='disabled')


    def cancela_edicao(self):
        if self.new_foto():
            if self.get_id():
                self._img = self._img_bkp
                self._set_foto()
            else:
                self.foto.configure(light_image=self.std_img, size=(18,18))
            self._foto_nova_status = 0
        self.foto_dir = None
        self.BT_label_foto.configure(command=self._show_foto, state='disabled')  


if __name__ == '__main__':    
    app = ctk.CTk()
    app.geometry("800x600")
    f = FrameFotos(app)
    f.grid(row=0, column=0)

    import sys
    sys.path.insert(0, r'C:\Users\ADM\Desktop\petshop\source\backend')

    # def convertToBinaryData(filename):
    #     with open(filename, 'rb') as file:
    #         blobData = file.read()
    #     return blobData

    # from database import *
    # bd = BD()
    # foto = r"C:\Users\ADM\Desktop\img.jpeg"
    # blob = convertToBinaryData(foto)
    # tupla = (2, blob)
    # query = f"""INSERT INTO foto(pet_id, foto) VALUES (?, ?)"""
    # call = bd.executa_query(query, tupla)
    # print(call)

    query = "select foto from foto where pet_id = 2"
    call = bd.consulta_query(query)
    img = call[0][0]

    img = Image.open(BytesIO(img))
    # img = ImageTk.PhotoImage(data=img)

    # f.set_foto(img)

    app.mainloop()
