import os
from tkinter import filedialog

from PIL import Image
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox


class PhotoHandler(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self._std_img = Image.open(os.path.relpath("petApp/images/w_plus.png"))

        self._id = 0
        self._new_photo_status = 0
        self._photo_path = None
        self._img = self._std_img
        self._img_bkp = None
        self._photo = ctk.CTkImage(self._img, size=(18,18))#aspect ratio is: 12 : 7
                
        self._bt_photo_display = ctk.CTkButton(
            self, text="", image=self._photo,
            corner_radius=10, fg_color='transparent',
            width=420,
            height=280,
            state='disabled',
            command=self._show_foto
        )
        self._bt_photo_display.pack(expand=True, fill="both")
        
    def _show_foto(self):
        self._img.show()
        return
    
    def _get_foto(self):
        CTkMessagebox(self.master, title="Aviso!", message="Dê preferência aos formatos Jpeg e PNG!", justify='center', option_focus=1)
        get = filedialog.askopenfile(
            mode ='r', 
            filetypes =[('Imagens', ['.jpeg', '.jpg', '.png', '.tiff', '.tif', '.bmp'])])
        if not get:
            return None
        self._img = Image.open(os.path.relpath(get.name))
        self._photo_path = os.path.relpath(get.name)
        self._set_foto()
        self._new_photo_status = 1

    def _set_foto(self):
         self._photo.configure(light_image=self._img, size=(420,280))

    def set_all(self, id_f:int|None, photo):
        if id_f:
            self._id = id_f
            img = Image.open(photo)
            self._img = img
            self._set_foto()
            self._bt_photo_display.configure(state='normal')
        else:
            self._id = 0
            self._img = self._std_img
            self._photo.configure(light_image=self._std_img, size=(18,18))
            self._bt_photo_display.configure(state='disabled')

    def get_dir(self):
        return self._photo_path

    def get_id(self):
        return self._id
    
    def new_photo(self):
        return bool(self._new_photo_status)

    def grid_adition(self):
        self._photo.configure(light_image=self._std_img, size=(18,18))
        self._bt_photo_display.configure(command=self._get_foto, state='normal')

    def grid_edition(self):
        if self.get_id():
            self._img_bkp = self._img
        self._bt_photo_display.configure(command=self._get_foto, state='normal')

    def grid_cancel_adition(self):
        self._new_photo_status = 0
        self._photo_path = None
        self._photo.configure(light_image=self._std_img, size=(18,18))
        self._bt_photo_display.configure(command=self._show_foto, state='disabled')

    def grid_cancel_edition(self):
        if self.new_photo():
            if self.get_id():
                self._img = self._img_bkp
                self._set_foto()
            else:
                self._photo.configure(light_image=self._std_img, size=(18,18))
            self._new_photo_status = 0
        self._photo_path = None
        self._bt_photo_display.configure(command=self._show_foto, state='disabled')  
