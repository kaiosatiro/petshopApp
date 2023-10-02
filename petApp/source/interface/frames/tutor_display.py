import os
from importlib import resources

from PIL import Image
import customtkinter as ctk
from  CTkMessagebox import CTkMessagebox


class TutorDisplay(ctk.CTkFrame):
    def __init__(self, master, titulo):
        super().__init__(master)
        
        self.grid_columnconfigure((1,3), weight=1)
        self.grid_rowconfigure(4, weight=1)

        self._id = ctk.IntVar(value=0)
        self._name_tutor = ctk.StringVar()
        self._tel1 = ctk.StringVar()
        self._tel2 = ctk.StringVar()
        self._address = ctk.StringVar(value='...')

        self._id_bkp = 0
        self._name_bkp = '-'
        self._tel1_bkp = '-'
        self._tel2_bkp = '-'
        self._address_bkp = '-'

        self._title_label = ctk.CTkLabel(
            self, text=titulo, font=('Torus Notched Regular', 30, 'bold'),
        ).grid(row=0, column=0, padx=10, pady=5, columnspan=4)
        
        # ____________ NOME ______________
        self._label_name = ctk.CTkLabel(
            self, text='Nome:', font=('Cairo', 22, 'bold'),          
        ).grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self._name_display = ctk.CTkEntry(
            self, textvariable=self._name_tutor,
            state='readonly', border_color='gray83',
            fg_color='gray83', corner_radius=8,
            font=('Torus Notched Regular', 22, 'normal')
        )
        self._name_display.grid(row=1, column=1, columnspan=3, pady=5, sticky='we')

        #____________ TELEFONES ________________
        self._label_tel1 = ctk.CTkLabel(self, text='Tel1:', font=('Cairo', 22, 'bold')).grid(
            row=2, column=0, sticky='w', padx=10, pady=5
        )
        self._tel1_display = ctk.CTkEntry(
            self, textvariable=self._tel1,
            state='readonly', border_color='gray83',
            fg_color='gray83', corner_radius=8,
            font=('Torus Notched Regular', 22, 'normal')
        ).grid(row=2, column=1, sticky='we')
        
        self._label_tel2 = ctk.CTkLabel(self, text='Tel2:', font=('Cairo', 22, 'bold')).grid(
            row=2, column=2, sticky='w', padx=10, pady=5
        )
        self._tel2_display = ctk.CTkEntry(
            self, textvariable=self._tel2,
            state='readonly', border_color='gray83',
            fg_color='gray83', corner_radius=8,
            font=('Torus Notched Regular', 22, 'normal'), justify='center'
        ).grid(row=2, column=3, sticky='we')
        
        #____________ ENDERECO ______________
        self._label_address = ctk.CTkLabel(self, text='Endereço:', font=('Torus Notched Regular', 22, 'bold')).grid(
            row=3, column=0, padx=10, pady=5, sticky='w', columnspan=2
        )
        self._address_display = ctk.CTkTextbox(
            self, corner_radius=6, font=('Torus Notched Regular', 22, 'normal'),
            fg_color='transparent',
            )
        self._address_display.grid(row=4, column=0, columnspan=4, sticky='nsew')
        self._address_display.insert("0.0", self._address.get())
        self._address_display.configure('disabled')

        #_____________ BOTES EDICAO _____________
        self._add_img = ctk.CTkImage(Image.open(os.path.realpath("petApp/images/add_img.png")), size=(28,28))
        self._del_img = ctk.CTkImage(Image.open(os.path.realpath("petApp/images/del_img.png")), size=(28,28))
            
        self._bt_add = ctk.CTkButton(
            self, text='', image=self._add_img,
            fg_color='#A5D6A7', hover_color='#81C784',
            command=self.add_fn, state='disabled'
            )
        self._bt_del = ctk.CTkButton(
            self, text='', image=self._del_img,
            fg_color='#EF9A9A', hover_color='#E57373',
            command=self.del_fn, state='disabled'
            )
    
    def exists(self):
        return bool(self._id.get())
 
    def foi_trocado(self):
        return not (self._id.get() == self._id_bkp)
    
    def get_old_id(self):
        return self._id_bkp

    def get_new_id(self):
        return self._id.get()
   
    def get(self):
        return {
            'id': self._id.get(),
            'name':self._name_tutor.get(),
            'tel1': self._tel1.get(),
            'tel2': self._tel2.get(),
            'address':self._address.get()
        }
   
    def set(self, id:int, name:str, tel1:str, tel2:str, address:str):
        self._id.set(id)
        self._name_tutor.set(name)
        self._tel1.set(tel1)       
        self._tel2.set(tel2)
        self._address.set(address)

        self._address_display.delete("0.0", "end")
        self._address_display.insert("0.0", self._address.get())
        self._address_display.configure(state='disabled')
    
    def reset(self):
        self._id.set(0)
        self._name_tutor.set('')
        self._tel1.set('')
        self._tel2.set('')
        self._address.set('')
        self._address_display.delete("0.0", "end")
        self._address_display.insert("0.0", self._address.get())

    def grid_edition(self):
        self._bt_add.grid(row=5, column=0, columnspan=2, pady=5, padx=5, sticky='ew')
        self._bt_del.grid(row=5, column=2, columnspan=2, pady=5, padx=5, sticky='ew')
        
        if self.exists():
            self._id_bkp = self._id.get()
            self._name_bkp = self._name_tutor.get()
            self._tel1_bkp = self._tel1.get()
            self._tel2_bkp = self._tel2.get()
            self._address_bkp = self._address.get()
            self._bt_del.configure(state='normal')
        else:
            self._bt_add.configure(state='normal')
    
    def grid_cancel_edition(self):
        self._bt_add.grid_forget()
        self._bt_del.grid_forget()
        self.set(self._id_bkp, self._name_bkp, self._tel1_bkp, self._tel2_bkp, self._address_bkp)
    
    def grid_adition_complete(self):
        self._bt_add.grid_forget()
        self._bt_del.grid_forget()
    
    def del_fn(self):
        msg = CTkMessagebox(
            title="Remover relação com Tutor?", justify='center',
            message=f"{self._name_tutor.get()} deixará de ser o Tutor do Pet {self.master._pet_display._name_pet.get()}?", 
            icon="question", font=('Torus Notched Regular', 18, 'normal'),
            option_1='Sim', option_2='Não',
            option_focus=1
        )
        if msg.get() == 'Sim':
            self._id.set(0)
            self._name_tutor.set('-')
            self._tel1.set('-')       
            self._tel2.set('-')
            self._address.set('...')
            self._address_display.delete("0.0", "end")
            self._address_display.insert("0.0", self._address.get())
            self._bt_del.configure(state='disabled')
            self._bt_add.configure(state='normal')

    def add_fn(self):
        get_id = self.master._call_tutor_quick_search_panel()
        if get_id:
            values = self.master.get_tutor(get_id)
            self.set(values[0], values[1], values[2], values[3], values[4])
            self._bt_del.configure(state='normal')
            self._bt_add.configure(state='disabled')
