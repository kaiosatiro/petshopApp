import os

from PIL import Image
import customtkinter as ctk


class BreedsPanel(ctk.CTkToplevel):
    #button.configure(command=lambda: self.command(item))
    def __init__(self, master, racas:list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title("Raças")
        self.geometry("360x600+600+200")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.protocol("WM_DELETE_WINDOW", self._on_closing)
            
        self._frame = ctk.CTkScrollableFrame(self)
        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        
        self._breeds = racas
        self._label_list = []
        self._button_list = []
        self._del_button_list = []

        self._bt_img = ctk.CTkImage(Image.open(os.path.realpath("petApp/images/bt_img.png")), size=(28,28))
        self._del_img = ctk.CTkImage(Image.open(os.path.realpath("petApp/images/del_img.png")), size=(28,28))

        self._bt_add = ctk.CTkButton(
            self, text='Add',
            font=('Torus Notched Regular', 22, 'normal'),
            border_spacing=4,
            command=self._add_action
        )
        self._bt_add.grid(row=1, column=0, pady=(0, 10))

        self.update_list()
        self.grab_set()        
    
    def update_list(self):
        for i, j, k in zip(self._label_list, self._button_list, self._del_button_list):
            i.destroy()
            j.destroy()
            k.destroy()
        
        self._label_list.clear()
        self._button_list.clear()
        self._del_button_list.clear()

        for i, item in enumerate(self._breeds):
            label = ctk.CTkLabel(self._frame, text=item, font=('Torus Notched Regular', 20, 'normal'))
            button = ctk.CTkButton(
                self._frame, text='', width=28, image=self._bt_img, 
                command=lambda item=item: self._edit_action(item),
                fg_color='#A5D6A7', hover_color='#81C784',
                )
            del_button = ctk.CTkButton(
                self._frame, text='', width=28, image=self._del_img,
                fg_color='#EF9A9A', hover_color='#E57373',
                command=lambda item=item: self._del_action(item)
                )
            label.grid(row=len(self._label_list), column=0, pady=(0, 10), sticky="w")
            button.grid(row=len(self._button_list), column=1, pady=(0, 10), padx=5, sticky="e")
            del_button.grid(row=len(self._button_list), column=2, pady=(0, 10), padx=5, sticky="e")
            self._label_list.append(label)
            self._button_list.append(button)
            self._del_button_list.append(del_button)
    
    def _add_action(self):
        cx_dlg = ctk.CTkInputDialog(text="Digite a nova Raça:", title="Adicionar Raça")
        get = cx_dlg.get_input()
        if get and get != '':
            self.master.add_breed(get)
            self.update_list()
        self.focus_force()
    
    def _edit_action(self, breed):
        cx_dlg = ctk.CTkInputDialog(text="Edite o nome da Raça:", title="Editar Raça", placeholder_text=breed)
        get = cx_dlg.get_input()
        if get and get != '':
            self.master.edit_breed(breed, get)
            self.update_list()
        self.focus_force()

    def _del_action(self, breed):
        call = self.master.delete_breed(breed)
        if call:
            self.update_list()
        self.focus_force()

    def _on_closing(self):
        self.grab_release()
        self.destroy()


        