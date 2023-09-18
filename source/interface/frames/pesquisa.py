import customtkinter as ctk
from CTkTable import *


class FramePesquisa(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color='transparent')

        self.master_blaster = master
        
        self.head_pet = [['#', 'id', 'Nome', 'Raça', 'Porte', 'Sexo']]
        self.head_tutor = [['#', 'id', 'Nome', 'Telefone 1', 'Telefone 2', 'Frequência']]

        self.tabela = CTkTable(
            self, column=6, values=self.head_pet,
            hover=True, hover_color='grey', header_color='grey',
            font=('', 22, 'normal'), command=self._filtro_nao_buscar_cabecalho_Pet,
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
    

    def _get_id(self, linha):
        return int(self.tabela.get(linha, 1))
    

    def get_nome(self, linha):
        return self.tabela.get(linha, 2)

    
    def _filtro_nao_buscar_cabecalho_Pet(self, *args):
        if args[0]['row'] == 0:
            return
        else:
            linha = args[0]['row']
            id_ = int(self._get_id(linha))
            tipo = self.master_blaster.var_tipo_busca.get()
            if tipo == 1:
                self.master_blaster.busca_dados(id_)
            elif tipo == 2:
                self.master_blaster.busca_tutor_painel(id_)
            