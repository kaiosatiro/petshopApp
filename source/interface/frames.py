import customtkinter as ctk
from PIL import Image
from CTkTable import *
import os


class FramePet(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure((1, 2), weight=1)
        self.grid_rowconfigure(4, weight=1)

        self.racas_lista = []
        self.porte_lista = ['Pequeno', 'Médio', 'Grande']
        self.sexo_lista = ['Macho', 'Fêmea']
        
        #VARIAVEIS DOS VALORES MOSTRADOS
        self.var_id = ctk.IntVar(value=None)
        self.var_nome = ctk.StringVar(value='- -')
        self.var_raca = ctk.StringVar(value='- -')
        self.var_porte = ctk.StringVar(value='- -')  
        self.var_sexo = ctk.StringVar(value='- -')
        
        #VARIAVEIS DOS VALORES QUE RECEBEM A EDICAO
        self.var_nome_ed = ctk.StringVar()
        self.var_raca_ed = ctk.StringVar()
        self.var_porte_ed = ctk.StringVar()  
        self.var_sexo_ed = ctk.StringVar()

        #WIDGETS DOS VALORES DO PET
        #________ IMAGEM _________
        self.img_frame =  ctk.CTkFrame(self, fg_color='transparent')
        self.img_frame.grid(row=0, column=0, rowspan=4, sticky='nsew', padx=10, pady=(10, 0))
        # image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.foto = ctk.CTkImage(Image.open(os.path.realpath("source/interface/images/image.png")), size=(440,300))#
        self.foto_label = ctk.CTkLabel(self.img_frame, text="", image=self.foto)
        self.foto_label.grid(row=0, column=0, sticky='nsew')
        
        #__________ NOME _________
        self.nome = ctk.CTkLabel(self, textvariable=self.var_nome, font=('', 28, 'normal'))
        self.nome.grid(row=0, column=2, padx=10, pady=10, sticky='ew', columnspan=3)

        self.label_nome = ctk.CTkLabel(self, text='Nome:', font=('', 28, 'bold')).grid(row=0, column=1)
        
        self.nome_ed = ctk.CTkEntry(
            self, textvariable=self.var_nome_ed,
            font=('', 28, 'normal'), justify='left'
        )

        #__________ RACA _________
        self.raca = ctk.CTkLabel(self, textvariable=self.var_raca, font=('', 28, 'normal'))
        self.raca.grid(row=1, column=2, padx=10, pady=10, sticky='ew', columnspan=3)

        self.label_raca = ctk.CTkLabel(self, text='Raça:', font=('', 28, 'bold')).grid(row=1, column=1)
        
        self.raca_ed = ctk.CTkComboBox(
            self, variable=self.var_raca_ed,
            state='normal', values=self.racas_lista,
            font=('', 28, 'normal'), dropdown_font=('', 26, 'normal'),
            justify='left'
        )

        # _________ SEXO __________
        self.sexo = ctk.CTkLabel(self, textvariable=self.var_sexo, font=('', 28, 'normal'))
        self.sexo.grid(row=2, column=2, padx=10, pady=10, sticky='ew')

        self.label_sexo = ctk.CTkLabel(self, text='Sexo:', font=('', 28, 'bold')).grid(row=2, column=1)

        self.sexo_ed = ctk.CTkComboBox(
            self, variable=self.var_sexo_ed,
            state='normal', values=self.sexo_lista,
            font=('', 28, 'normal'), dropdown_font=('', 26, 'normal'),
            justify='left'
        )

        # _________ PORTE __________        

        self.porte = ctk.CTkLabel(self, textvariable=self.var_porte, font=('', 28, 'normal'))
        self.porte.grid(row=3, column=2, padx=10, pady=10, sticky='ew')

        self.label_porte = ctk.CTkLabel(self, text='Porte:', font=('', 28, 'bold')).grid(row=3, column=1)
        
        self.porte_ed = ctk.CTkComboBox(
            self, variable=self.var_porte_ed,
            state='normal', values=self.porte_lista,
            font=('', 28, 'normal'), dropdown_font=('', 26, 'normal'),
            justify='left'
        )

        # _________ OBSERVACOES __________        
        self.label_observacoes = ctk.CTkLabel(self, text='Observações', font=('', 26, 'bold'))
        self.label_observacoes.grid(row=4, column=0, sticky='w', padx=10, pady=(0, 5))
        self.observacoes = ctk.CTkTextbox(
            self, corner_radius=6, font=('', 22, 'normal'),
            fg_color='transparent'
            )
        self.observacoes.grid(row=5, column=0, columnspan=5, sticky='nsew', padx=10, pady=(0, 10))
        self.observacoes.insert("0.0", '...')
        self.observacoes.configure(state='disable')

        bt_img = ctk.CTkImage(Image.open(os.path.realpath("source/interface/images/bt_img.png")), size=(28,28))#
        self.BT_editar_obs = ctk.CTkButton(
            self, text='', width=28, image=bt_img,
            command=master._editar_observacao,
            state='disabled'
        )
        self.BT_editar_obs.grid(row=4, column=0, sticky='w', padx=180, pady=5)
    

    def set_racas(self, racas:list):
        self.racas_lista = racas
        self.raca_ed.configure(values=racas)


    def get(self):
        return {
            'id': self.var_id.get(),
            'nome': self.var_nome.get(),
            'raca': self.var_raca.get(),
            'sexo': self.var_sexo.get(),
            'porte': self.var_porte.get(),
            'observacoes': self.get_observacoes()
        }
    

    def set(self, id:int, nome:str, raca:str, porte:str, sexo:str, observacoes:str):
        self.var_id.set(id)
        self.var_nome.set(nome)
        self.var_raca.set(raca)
        self.var_porte.set(porte)
        self.var_sexo.set(sexo)
        self.set_observacoes(observacoes)


    def get_observacoes(self):
        return self.observacoes.get('0.0', 'end')
    

    def set_observacoes(self, txt):
        self.observacoes.configure(state='normal')
        self.observacoes.delete("0.0", "end")
        self.observacoes.insert("0.0", txt)
        self.observacoes.configure(state='disable')


    def reset_observacao(self):
        self.observacoes.delete('0.0', 'end')
        self.observacoes.insert("0.0", '...')
    

    def ativa_edicao(self):
        self.var_nome_ed.set(self.var_nome.get())
        self.var_raca_ed.set(self.var_raca.get())
        self.var_porte_ed.set(self.var_porte.get())
        self.var_sexo_ed.set(self.var_sexo.get())
        
        self.nome.grid_forget()
        self.raca.grid_forget()
        self.sexo.grid_forget()
        self.porte.grid_forget()

        self.nome_ed.grid(row=0, column=2, padx=10, pady=10, sticky='ew')
        self.raca_ed.grid(row=1, column=2, padx=10, pady=10, sticky='ew')
        self.sexo_ed.grid(row=2, column=2, padx=10, pady=10, sticky='ew')
        self.porte_ed.grid(row=3, column=2, padx=10, pady=10, sticky='ew')

    
    def cancela_edicao(self):
        self.nome_ed.grid_forget()
        self.raca_ed.grid_forget()
        self.sexo_ed.grid_forget()
        self.porte_ed.grid_forget()

        self.nome.grid(row=0, column=2, padx=10, pady=10, sticky='ew')
        self.raca.grid(row=1, column=2, padx=10, pady=10, sticky='ew')
        self.sexo.grid(row=2, column=2, padx=10, pady=10, sticky='ew')
        self.porte.grid(row=3, column=2, padx=10, pady=10, sticky='ew')

        
    
class FrameTutor(ctk.CTkFrame):
    def __init__(self, master, titulo):
        super().__init__(master)
        
        self.grid_columnconfigure((1,3), weight=1)
        self.grid_rowconfigure(4, weight=1)

        self.var_id = ctk.IntVar(value=None)
        self.var_nome = ctk.StringVar(value='-')
        self.var_tel1 = ctk.StringVar(value='-')
        self.var_tel2 = ctk.StringVar(value='-')
        self.var_endereco = ctk.StringVar(value='...')

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

        add_img = ctk.CTkImage(Image.open(os.path.realpath("source/interface/images/add_img.png")), size=(28,28))
        del_img = ctk.CTkImage(Image.open(os.path.realpath("source/interface/images/del_img.png")), size=(28,28))
        self.BT_add = ctk.CTkButton(self, text='', width=28, image=add_img)
        self.BT_del = ctk.CTkButton(self, text='', width=28, image=del_img)
    

    def get(self):
        return {
            'id': self.var_id.get(),
            'nome':self.var_nome.get(),
            'tel1': self.var_tel1.get(),
            'tel2': self.var_tel2.get(),
            'endereco':self.var_endereco.get()
        }
    

    def set(self, id:int, nome:str, tel1:str, tel2:str, endereco:str):
        self.var_id.set(id)
        self.var_nome.set(nome)
        self.var_tel1.set(tel1)       
        self.var_tel2.set(tel2)
        self.var_endereco.set(endereco)

        self.endereco.delete("0.0", "end")
        self.endereco.insert("0.0", self.var_endereco.get())
    

    def ativa_edicao(self):
        self.BT_add.grid(row=5, column=3, pady=5, stick='w')
        self.BT_del.grid(row=5, column=3, pady=5, sticky='e')
    

    def cancela_edicao(self):
        self.BT_add.grid_forget()
        self.BT_del.grid_forget()


class FramePesquisa(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(fg_color='transparent')

        self.head_pet = [['#', 'id', 'Nome', 'Raça', 'Porte', 'Sexo']]
        self.head_tutor = [['#', 'id', 'Nome', 'Telefone 1', 'Telefone 2', 'Frequência']]

        self.tabela = CTkTable(
            self, column=6, values=self.head_pet,
            hover=True, hover_color='grey', header_color='grey',
            font=('', 22, 'normal'), command=master.busca_dados,
        )
        self.tabela.pack(expand=True, fill="both", padx=20, pady=20)


    def set(self, head, dados):
        for i in range(1, self.tabela.rows+1):
            self.tabela.delete_row(i)
        if head == 1:
            dados_tabela = self.head_pet.copy()
            for i in dados:
                dados_tabela.append(i)
            for i, lista in enumerate(dados_tabela):
                if i == 0:
                    self.tabela.add_row(lista, i)
                else:
                    lista = list(lista )
                    lista.insert(0, i)
                    self.tabela.add_row(lista, i)
        elif head == 2:
            dados_tabela = self.head_tutor.copy()
            for i in dados:
                dados_tabela.append(i)
            for i, lista in enumerate(dados_tabela):
                if i == 0:
                    self.tabela.add_row(lista, i)
                else:
                    lista = list(lista)
                    lista.insert(0, i)
                    self.tabela.add_row(lista, i)
                    
        self.tabela.edit_column(0, width=10)
        self.tabela.edit_column(1, width=100)
        self.tabela.edit_column(2, width=400)
        self.tabela.edit_column(3, width=150)
        self.tabela.edit_column(4, width=150)
        self.tabela.edit_column(4, width=150)
        

    def muda_header(self, tipo):
        if tipo == 1:
            self.tabela.configure(values=self.head_pet)
        elif tipo == 2:
            self.tabela.configure(values=self.head_tutor)
    

    def get_id(self, linha):
        return int(self.tabela.get(linha, 1))
    

    def get_nome(self, linha):
        return self.tabela.get(linha, 2)
