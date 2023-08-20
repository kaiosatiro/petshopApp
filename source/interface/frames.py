import customtkinter as ctk
from PIL import Image
from CTkTable import *
import os


class FramePet(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(4, weight=1)

        self.var_nome = ctk.StringVar(name='PY_NOME_PET', value='-')
        self.var_raca = ctk.StringVar(name='PY_RACA', value='-')
        self.var_porte = ctk.StringVar(name='PY_PORTE', value='-')
        self.var_observacoes = ctk.StringVar(name='PY_OBERVACOES', value='...')
        

        self.img_frame =  ctk.CTkFrame(self, fg_color='transparent')
        self.img_frame.grid(row=0, column=0, rowspan=3, sticky='nsew', padx=10, pady=10)
        # image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.foto = ctk.CTkImage(Image.open(os.path.realpath("images/image.png")), size=(500,300))#
        self.foto_label = ctk.CTkLabel(self.img_frame, text="", image=self.foto)
        self.foto_label.grid(row=0, column=0, sticky='nsew')

        self.nome = ctk.CTkEntry(
            self, textvariable=self.var_nome,
            fg_color='transparent', state='readonly',
            font=('', 32, 'normal'), justify='center'
        ).grid(row=0, column=2, padx=10, pady=10, sticky='nsew')
        self.label_nome = ctk.CTkLabel(self, text='Nome:', font=('', 32, 'bold')).grid(row=0, column=1)
        
        self.raca = ctk.CTkEntry(
            self, textvariable=self.var_raca,
            fg_color='transparent', state='readonly',
            font=('', 32, 'normal'), justify='center'
        ).grid(row=1, column=2, padx=10, pady=10, sticky='nsew')
        self.label_raca = ctk.CTkLabel(self, text='Raça:', font=('', 32, 'bold')).grid(row=1, column=1)

        self.porte = ctk.CTkEntry(
            self, textvariable=self.var_porte,
            fg_color='transparent', state='readonly',
            font=('', 32, 'normal'), justify='center'
        ).grid(row=2, column=2, padx=10, pady=10, sticky='nsew')
        self.label_porte = ctk.CTkLabel(self, text='Porte:', font=('', 32, 'bold')).grid(row=2, column=1)


        self.label_observacoes = ctk.CTkLabel(self, text='Observações:', font=('', 26, 'bold'))
        self.label_observacoes.grid(row=3, column=0, sticky='w', padx=10, pady=5)
        self.observacoes = ctk.CTkTextbox(
            self, corner_radius=6, font=('', 22, 'normal'),
            fg_color='transparent'
            )
        self.observacoes.grid(row=4, column=0, columnspan=3, sticky='nsew', padx=10, pady=(0, 10))
        self.observacoes.insert("0.0", self.var_observacoes.get())
        self.observacoes.configure(state='disable')


    def get(self):
        return {
            'nome': self.var_nome.get(),
            'raca': self.var_raca.get(),
            'porte': self.var_porte.get(),
            'obervacoes': self.var_observacoes.get()
        }
    

    def set(self, nome:str, raca:str, porte:str, observacoes:str):
        self.var_nome.set(nome)
        self.var_raca.set(raca)
        self.var_porte.set(porte)
        self.var_observacoes.set(observacoes)

        self.observacoes.delete("0.0", "end") 
        self.observacoes.insert("0.0", self.var_observacoes.get())
    

    def reset_observacao(self):
        self.observacoes.delete('0.0', 'end')
        self.observacoes.insert("0.0", self.var_observacoes.get())
        
    
class FrameTutor(ctk.CTkFrame):
    def __init__(self, master, titulo):
        super().__init__(master)
        
        self.grid_columnconfigure((1,3), weight=1)
        self.grid_rowconfigure(4, weight=1)

        self.var_nome = ctk.StringVar(name='PY_NOME_TUTOR', value='-')
        self.var_tel1 = ctk.StringVar(name='PY_TEL1_TUTOR', value='-')
        self.var_tel2 = ctk.StringVar(name='PY_TEL2_TUTOR', value='-')
        self.var_endereco = ctk.StringVar(name='PY_ENDERECO', value='...')

        self.titulo = ctk.CTkLabel(
            self, text=titulo, font=('', 28, 'bold'),
        ).grid(row=0, column=0, padx=10, pady=5, columnspan=4)
        

        self.label_nome = ctk.CTkLabel(
            self, text='Nome:', font=('', 22, 'bold'),          
        ).grid(row=1, column=0, padx=10, pady=5, sticky='w')

        self.nome = ctk.CTkEntry(
            self, textvariable=self.var_nome,
            fg_color='transparent', state='readonly',
            font=('', 22, 'normal')
        ).grid(row=1, column=1, columnspan=3, pady=5, sticky='we')
        

        self.label_tel1 = ctk.CTkLabel(self, text='Tel1:', font=('', 22, 'bold')).grid(
            row=2, column=0, sticky='w', padx=10, pady=5
        )

        self.tel1 = ctk.CTkEntry(
            self, textvariable=self.var_tel1,
            fg_color='transparent', state='readonly',
            font=('', 22, 'normal')
        ).grid(row=2, column=1, sticky='we')


        self.label_tel2 = ctk.CTkLabel(self, text='Tel2:', font=('', 22, 'bold')).grid(
            row=2, column=2, sticky='w', padx=10, pady=5
        )

        self.tel1 = ctk.CTkEntry(
            self, textvariable=self.var_tel2,
            fg_color='transparent', state='readonly',
            font=('', 22, 'normal'), justify='center'
        ).grid(row=2, column=3, sticky='we')


        self.label_endereco = ctk.CTkLabel(self, text='Endereço:', font=('', 22, 'bold')).grid(
            row=3, column=0, padx=10, pady=5, sticky='w', columnspan=2
        )
    
        self.endereco = ctk.CTkTextbox(
            self, corner_radius=6, font=('', 22, 'normal'),
            fg_color='transparent'
            )
        self.endereco.grid(row=4, column=0, columnspan=4, sticky='nsew')
        self.endereco.insert("0.0", self.var_endereco.get())  
    

    def get(self):
        return {
            'nome':self.var_nome.get(),
            'tel1': self.var_tel1.get(),
            'tel2': self.var_tel2.get(),
            'endereco':self.var_endereco.get()
        }
    

    def set(self, nome:str, tel1:str, tel2:str, endereco:str):
        self.var_nome.set(nome)
        self.var_tel1.set(tel1)       
        self.var_tel2.set(tel2)       
        self.var_endereco.set(endereco)

        self.endereco.delete("0.0", "end") 
        self.endereco.insert("0.0", self.var_endereco.get())  


class FramePesquisa(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(fg_color='transparent')

        self.head_pet = [['#', 'Nome', 'Raça', 'Tutor 1', 'Tutor 2']]
        self.head_tutor = [['#', 'Nome', 'Telefone 1', 'Telefone 2']]

        self.tabela = CTkTable(
            self, column=5, values=self.head_pet,
            hover=True, hover_color='grey', header_color='grey',
            font=('', 22, 'normal'), command=master.get_linha,
        )
        self.tabela.pack(expand=True, fill="both", padx=20, pady=20)
        self.tabela.edit_column(0, width=1)


    def set(self, head, dados):
        for i in range(1, self.tabela.rows+1):
            self.tabela.delete_row(i)
        if head == 'PET':
            ...
        elif head == 'TUTOR':
            dados_tabela = self.head_tutor.copy()
            for i in dados:
                dados_tabela.append(i)
            for n, i in enumerate(dados_tabela):
                self.tabela.add_row(i, n)
        

    def muda_header(self, tipo):
        if tipo == 'PET':
            self.tabela.configure(values=self.head_pet)
        elif tipo == 'TUTOR':
            self.tabela.configure(values=self.head_tutor)


# class FrameServicos(ctk.CTkFrame):
#     def __init__(self, master):
#         super().__init__(master)

#         head = [['#', 'Serviço', 'Data']]
#         self.tabela = CTkTable(self, column=3, values=head)
#         self.tabela.pack(expand=True, fill="both", padx=20, pady=20)
