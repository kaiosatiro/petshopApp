import customtkinter as ctk
from  CTkMessagebox import CTkMessagebox
from .tutores_lista import *
from PIL import Image
import os


class FrameTutor(ctk.CTkFrame):
    def __init__(self, master, titulo):
        super().__init__(master)
        
        self.grid_columnconfigure((1,3), weight=1)
        self.grid_rowconfigure(4, weight=1)

        self._var_id = ctk.IntVar(value=0)
        self._var_nome = ctk.StringVar(value='-')
        self._var_tel1 = ctk.StringVar(value='-')
        self._var_tel2 = ctk.StringVar(value='-')
        self._var_endereco = ctk.StringVar(value='...')

        self._id_ed = 0
        self._nome_ed = '-'
        self._tel1_ed = '-'
        self._tel2_ed = '-'
        self._endereco_ed = '-'

        self.titulo = ctk.CTkLabel(
            self, text=titulo, font=('', 28, 'bold'),
        ).grid(row=0, column=0, padx=10, pady=5, columnspan=4)
        
        # ____________ NOME ______________
        self.label_nome = ctk.CTkLabel(
            self, text='Nome:', font=('', 22, 'bold'),          
        ).grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.nome = ctk.CTkEntry(
            self, textvariable=self._var_nome,
            fg_color='transparent', state='readonly',
            font=('', 22, 'normal')
        )
        self.nome.grid(row=1, column=1, columnspan=3, pady=5, sticky='we')

        #____________ TELEFONES ________________
        self.label_tel1 = ctk.CTkLabel(self, text='Tel1:', font=('', 22, 'bold')).grid(
            row=2, column=0, sticky='w', padx=10, pady=5
        )
        self.tel1 = ctk.CTkEntry(
            self, textvariable=self._var_tel1,
            fg_color='transparent', state='readonly',
            font=('', 22, 'normal')
        ).grid(row=2, column=1, sticky='we')
        
        self.label_tel2 = ctk.CTkLabel(self, text='Tel2:', font=('', 22, 'bold')).grid(
            row=2, column=2, sticky='w', padx=10, pady=5
        )
        self.tel2 = ctk.CTkEntry(
            self, textvariable=self._var_tel2,
            fg_color='transparent', state='readonly',
            font=('', 22, 'normal'), justify='center'
        ).grid(row=2, column=3, sticky='we')
        
        #____________ ENDERECO ______________
        self.label_endereco = ctk.CTkLabel(self, text='Endereço:', font=('', 22, 'bold')).grid(
            row=3, column=0, padx=10, pady=5, sticky='w', columnspan=2
        )
        self.endereco = ctk.CTkTextbox(
            self, corner_radius=6, font=('', 22, 'normal'),
            fg_color='transparent'
            )
        self.endereco.grid(row=4, column=0, columnspan=4, sticky='nsew')
        self.endereco.insert("0.0", self._var_endereco.get())

        #_____________ BOTES EDICAO _____________
        add_img = ctk.CTkImage(Image.open(os.path.realpath("source/interface/images/add_img.png")), size=(28,28))
        del_img = ctk.CTkImage(Image.open(os.path.realpath("source/interface/images/del_img.png")), size=(28,28))
        self.BT_del = ctk.CTkButton(self, text='', width=28, image=del_img, command=self.del_fn, state='disabled')
        self.BT_add = ctk.CTkButton(self, text='', width=28, image=add_img, command=self.add_fn, state='disabled')
    

    def exists(self):
        return bool(self._var_id.get())

    
    def foi_trocado(self):
        return not (self._var_id.get() == self._id_ed)
    
    
    def get_old_id(self):
        return self._id_ed


    def get_new_id(self):
        return self._var_id.get()
    

    def get(self):
        return {
            'id': self._var_id.get(),
            'nome':self._var_nome.get(),
            'tel1': self._var_tel1.get(),
            'tel2': self._var_tel2.get(),
            'endereco':self._var_endereco.get()
        }
    

    def set(self, id:int, nome:str, tel1:str, tel2:str, endereco:str):
        self._var_id.set(id)
        self._var_nome.set(nome)
        self._var_tel1.set(tel1)       
        self._var_tel2.set(tel2)
        self._var_endereco.set(endereco)

        self.endereco.delete("0.0", "end")
        self.endereco.insert("0.0", self._var_endereco.get())
    

    def reset(self):
        self._var_id.set(0)
        self._var_nome.set('')
        self._var_tel1.set('')
        self._var_tel2.set('')
        self._var_endereco.set('')
        self.endereco.delete("0.0", "end")
        self.endereco.insert("0.0", self._var_endereco.get())


    def ativa_edicao(self):
        self.BT_add.grid(row=5, column=3, pady=5, stick='w')
        self.BT_del.grid(row=5, column=3, pady=5, sticky='e')
        
        if self.exists():
            self._id_ed = self._var_id.get()
            self._nome_ed = self._var_nome.get()
            self._tel1_ed = self._var_tel1.get()
            self._tel2_ed = self._var_tel2.get()
            self._endereco_ed = self._var_endereco.get()
            self.BT_del.configure(state='normal')
        else:
            self.BT_add.configure(state='normal')
    

    def cancela_edicao(self):
        self.BT_add.grid_forget()
        self.BT_del.grid_forget()
        self.set(self._id_ed, self._nome_ed, self._tel1_ed, self._tel2_ed, self._endereco_ed)
    

    def finaliza_adicao(self):
        self.BT_add.grid_forget()
        self.BT_del.grid_forget()

    
    def del_fn(self):
        msg = CTkMessagebox(
            title="Remover relação com Tutor?", justify='center',
            message=f"{self._var_nome.get()} deixará de ser o Tutor do Pet {self.master.pet.var_nome.get()}?", 
            icon="question", font=('', 18, 'normal'),
            option_1='Sim', option_2='Não',
            option_focus=1
        )
        if msg.get() == 'Sim':
            self._var_id.set(0)
            self._var_nome.set('-')
            self._var_tel1.set('-')       
            self._var_tel2.set('-')
            self._var_endereco.set('...')
            self.endereco.delete("0.0", "end")
            self.endereco.insert("0.0", self._var_endereco.get())
            self.BT_del.configure(state='disabled')
            self.BT_add.configure(state='normal')


    def add_fn(self):
        get_id = self.master._frame_tutores()
        if get_id:
            values = self.master.busca_tutor(get_id)
            self.set(values[0], values[1], values[2], values[3], values[4])
            self.BT_del.configure(state='normal')
            self.BT_add.configure(state='disabled')
