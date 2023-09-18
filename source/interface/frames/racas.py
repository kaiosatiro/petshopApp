import customtkinter as ctk
from PIL import Image
import os


class FrameRacas(ctk.CTkToplevel):
    #button.configure(command=lambda: self.command(item))
    def __init__(self, master, racas:list, add_fn, edit_fn, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title("Raças")
        self.geometry("300x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.protocol("WM_DELETE_WINDOW", self._on_closing)
            
        self.frame = ctk.CTkScrollableFrame(self)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        
        self.add_fn = add_fn
        self.edit_fn = edit_fn

        self.lista = racas
        self.label_list = []
        self.button_list = []
        self.bt_img = ctk.CTkImage(Image.open(os.path.realpath("source/interface/images/bt_img.png")), size=(28,28))      

        self.BT_add = ctk.CTkButton(
            self, text='Add',
            font=('', 22, 'normal'),
            border_spacing=4,
            command=self._add_action
        )
        self.BT_add.grid(row=1, column=0, pady=(0, 10))

        self._listagem()
        self.grab_set()        
    
    
    def _listagem(self):
        for i, j in zip(self.label_list, self.button_list):
            i.destroy()
            j.destroy()
        
        self.label_list.clear()
        self.button_list.clear()

        for i, item in enumerate(self.lista):
            label = ctk.CTkLabel(self.frame, text=item, font=('', 20, 'normal'))
            button = ctk.CTkButton(self.frame, text='', width=28, image=self.bt_img, command=lambda item=item: self._edit_action(item))
            label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
            button.grid(row=len(self.button_list), column=1, pady=(0, 10), padx=5, sticky="e")
            self.label_list.append(label)
            self.button_list.append(button)
    

    def _add_action(self):
        cx_dlg = ctk.CTkInputDialog(text="Digite a nova Raça:", title="Adicionar Raça")
        get = cx_dlg.get_input()
        if get and get != '':
            self.add_fn(get)
            self._listagem()
        self.focus_force()
    

    def _edit_action(self, raca):
        cx_dlg = ctk.CTkInputDialog(text="Edite o nome da Raça:", title="Editar Raça", placeholder_text=raca)
        get = cx_dlg.get_input()
        if get and get != '':
            self.edit_fn(raca, get)
            self._listagem()
        self.focus_force()
    

    def _on_closing(self):
        self.grab_release()
        self.destroy()


        