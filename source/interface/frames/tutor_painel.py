import customtkinter as ctk
from CTkTable import *


class TutorPainel(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Tutor Painel")
        self.geometry("700x600+500+200")
        # self.maxsize(600, 700)
        self.protocol("WM_DELETE_WINDOW", self._on_closing)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.frameT = ctk.CTkFrame(self)
        self.frameL = ctk.CTkScrollableFrame(self)

        self.frameT.grid(row=0, padx=10, pady=(40,0), sticky='nsew')
        self.frameT.grid_columnconfigure((1,3), weight=1)
        self.frameL.grid(row=1, column=0, padx=10, pady=(45,0), sticky='nsew')
        # self.frameL.grid_columnconfigure((1,3), weight=1)
        
        self._var_id = ctk.IntVar(value=0)
        self._var_nome = ctk.StringVar(value='')
        self._var_tel1 = ctk.StringVar(value='')
        self._var_tel2 = ctk.StringVar(value='')
        self._var_endereco = ctk.StringVar(value='')

        self._id_ed = 0
        self._nome_ed = ''
        self._tel1_ed = ''
        self._tel2_ed = ''
        self._endereco_ed = ''

        # ____________ NOME ______________
        self.label_nome = ctk.CTkLabel(
            self.frameT, text='Nome:', font=('', 22, 'bold'),          
        ).grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.nome = ctk.CTkEntry(
            self.frameT, textvariable=self._var_nome,
            state='readonly',
            font=('', 22, 'normal')
        )
        self.nome.grid(row=1, column=1, columnspan=3, pady=5, sticky='we')

        #____________ TELEFONES ________________
        self.label_tel1 = ctk.CTkLabel(self.frameT, text='Tel1:', font=('', 22, 'bold')).grid(
            row=2, column=0, sticky='w', padx=10, pady=5
        )
        self.tel1 = ctk.CTkEntry(
            self.frameT, textvariable=self._var_tel1,
             state='readonly',
            font=('', 22, 'normal')
        )
        self.tel1.grid(row=2, column=1, sticky='we')
        
        self.label_tel2 = ctk.CTkLabel(self.frameT, text='Tel2:', font=('', 22, 'bold')).grid(
            row=2, column=2, sticky='w', padx=10, pady=5
        )
        self.tel2 = ctk.CTkEntry(
            self.frameT, textvariable=self._var_tel2,
             state='readonly',
            font=('', 22, 'normal'),
        )
        self.tel2.grid(row=2, column=3, sticky='we')
        
        #____________ ENDERECO ______________
        self.label_endereco = ctk.CTkLabel(self.frameT, text='Endereço:', font=('', 22, 'bold')).grid(
            row=3, column=0, padx=10, pady=5, sticky='w', columnspan=2
        )
        self.endereco = ctk.CTkEntry(
            self.frameT, corner_radius=6, font=('', 22, 'normal'),
            textvariable=self._var_endereco,
            state='readonly',
            
            )
        self.endereco.grid(row=4, column=0, padx=10, pady=(0, 10), columnspan=4, sticky='nsew')
        #_____________ PETS __________________
        self.label_endereco = ctk.CTkLabel(
            self, text='Pets', font=('', 28, 'bold'),
            bg_color='transparent'
            ).grid(row=1, column=0, pady=(10,0), sticky='n')
        
        self.head_tabela = [['#', 'Nome', 'Raca']]
        self.tabela = CTkTable(
            self.frameL, column=3, values=self.head_tabela,
            hover=True, hover_color='grey', header_color='grey',
            font=('', 18, 'normal'),
            command=self._vizualiza_pet
        )
        self.tabela.pack(expand=True, fill="both", padx=10, pady=10)
        self.tabela.edit_column(0, width=1)
        self.tabela.edit_column(1, width=300)

        #_____________ BOTES _____________
        # del_img = ctk.CTkImage(Image.open(os.path.realpath("source/interface/images/del_img.png")), size=(28,28))
        # self.BT_del = ctk.CTkButton(self, text='', width=28, image=del_img, command=self.del_fn, state='disabled')

        self.bt_excluir = ctk.CTkButton(
            self, text='Excluir',
            font=('', 20, 'normal'),
            hover_color='red',
            width=100,
            command=self._excluir_tutor
        )

        self.bt_editar = ctk.CTkButton(
            self, text='Editar',
            font=('', 22, 'normal'),
            border_spacing=4, height=20,
            command=self._ativa_edicao
        )

        self.bt_voltar = ctk.CTkButton(
            self, text='Voltar',
            font=('', 22, 'normal'),
            border_spacing=4, height=20,
            command=self._on_closing
        )

        self.bt_editar.grid_configure(row=3, column=0, padx=200, pady=6, sticky='w')
        self.bt_voltar.grid_configure(row=3, column=0, padx=200, pady=6, sticky='e')

        self.focus_force()
        self.grab_set()
    

    def get(self):
        return {
            'id': self._var_id.get(),
            'nome':self._var_nome.get(),
            'tel1': self._var_tel1.get(),
            'tel2': self._var_tel2.get(),
            'endereco':self._var_endereco.get()
        }
    

    def set(self, id_:int, nome:str, tel1:str, tel2:str, endereco:str):
        self._var_id.set(id_)
        self._var_nome.set(nome)
        self._var_tel1.set(tel1)       
        self._var_tel2.set(tel2)
        self._var_endereco.set(endereco)
    

    def set_tabela(self, dados):
        for i, lista in enumerate(dados):
            lista = list(lista)
            self.tabela.add_row(lista, i+1)
    

    def _ativa_edicao(self):
        self._id_ed = self._var_id.get()
        self._nome_ed = self._var_nome.get()
        self._tel1_ed = self._var_tel1.get()
        self._tel2_ed = self._var_tel2.get()
        self._endereco_ed = self._var_endereco.get()

        self.nome.configure(state='normal')
        self.tel1.configure(state='normal')
        self.tel2.configure(state='normal')
        self.endereco.configure(state='normal')

        self.bt_excluir.grid_configure(row=0, column=0, padx=10, pady=5, sticky='en')
        self.bt_editar.configure(text='Salvar', command=self._salvar_edicao)
        self.bt_voltar.configure(text='Cancelar', command=self._cancelar_edicao)
    

    def _salvar_edicao(self):
        wait = self.master.salvar_edicao_tutor()
        if wait:
            self.set(wait[0], wait[1], wait[2], wait[3], wait[4])
            self.nome.configure(state='readonly')
            self.tel1.configure(state='readonly')
            self.tel2.configure(state='readonly')
            self.endereco.configure(state='readonly')

            self.bt_excluir.grid_forget()
            self.bt_editar.configure(text='Editar', command=self._ativa_edicao)
            self.bt_voltar.configure(text='Voltar', command=self._on_closing)


    def _cancelar_edicao(self):
        self.nome.configure(state='readonly')
        self.tel1.configure(state='readonly')
        self.tel2.configure(state='readonly')
        self.endereco.configure(state='readonly')

        self._var_id.set(self._id_ed)
        self._var_nome.set(self._nome_ed)
        self._var_tel1.set(self._tel1_ed)
        self._var_tel2.set(self._tel2_ed)
        self._var_endereco.set(self._endereco_ed)

        self.bt_excluir.grid_forget()
        self.bt_editar.configure(text='Editar', command=self._ativa_edicao)
        self.bt_voltar.configure(text='Voltar', command=self._on_closing)
    

    def ativa_Adicao(self):
        self.nome.configure(state='normal')
        self.tel1.configure(state='normal')
        self.tel2.configure(state='normal')
        self.endereco.configure(state='normal')

        self.bt_editar.configure(text='Salvar', command=self._salvar_Adicao)
        self.bt_voltar.configure(text='Cancelar', command=self._on_closing)
    

    def _salvar_Adicao(self):
        wait = self.master.salvar_novo_tutor()
        if wait:
            self.set(wait[0], wait[1], wait[2], wait[3], wait[4])
            self.nome.configure(state='readonly')
            self.tel1.configure(state='readonly')
            self.tel2.configure(state='readonly')
            self.endereco.configure(state='readonly')

            self.bt_editar.configure(text='Editar', command=self._ativa_edicao)
            self.bt_voltar.configure(text='Voltar', command=self._on_closing)
    

    def _excluir_tutor(self):
        call = self.master.excluir_tutor(self._var_id.get(), self._var_nome.get())
        if call:
            self._on_closing()
    

    def _vizualiza_pet(self, *args, **kargs):
        linha = self.tabela.get_row(args[0]['row'])
        id_ = linha[0]
        self.master.busca_dados(id_)
        self.grab_release()
        self.master.focus_force()
        # self.master.BT ?
    
    
    def _on_closing(self):
        self.master.listagem()
        self.grab_release()
        self.destroy()

    



if __name__ == '__main__':
    ctk.set_appearance_mode("light")
    app = ctk.CTk()
    t = TutorPainel(app)
    
    app.mainloop()