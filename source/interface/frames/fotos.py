import os
import customtkinter as ctk
from tkinter import filedialog
from CTkMessagebox import CTkMessagebox
from PIL import Image
from io import BytesIO


class FrameFotos(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        # self.std_img = Image.open(os.path.realpath("source/interface/images/image.png"))
        self.add_img = Image.open(os.path.realpath("source/interface/images/w_plus.png"))

        self.foto = ctk.CTkImage(self.add_img, size=(18,18))#aspect ratio is: 12 : 7
        self._id = 0
        
        self.BT_label_foto = ctk.CTkButton(
            self, text="", image=self.foto,
            corner_radius=10, fg_color='transparent',
            width=420,
            height=280,
            state='disabled',
            command=self._get_foto
        )
        self.BT_label_foto.pack(expand=True, fill="both")
               
        self.set_adicao()


    def _show_foto(self):
        self.std_img.show()
    

    def _get_foto(self):
        CTkMessagebox(title="Aviso!", message="Dê preferência aos formatos Jpeg e PNG!")
        get = filedialog.askopenfile(mode ='r', filetypes =[('Imagens', ['.jpeg', '.jpg', '.png',
                                                       '.tiff', '.tif', '.bmp'])])
        if not get:
            return None
        img = Image.open(os.path.realpath(get.name))
        self.set_foto(img)


    def set_foto(self, foto):
         self.foto.configure(light_image=foto, size=(420,280))
         self._id = 1


    def set_adicao(self):
        self.BT_label_foto.configure(state='normal')
    
         
    def add_foto(self):
        ...

    
    def exists(self):
        return self._id



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

    from database import *
    bd = BD()
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
