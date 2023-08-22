from .frames import *


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title('petApp')
        self.geometry('1280x720')
        ctk.set_appearance_mode("light")

        #AREA PRINCIPAL
        self.pet = FramePet(self)
        self.tutor1 = FrameTutor(self, 'Tutor 1')   
        self.tutor2 = FrameTutor(self, 'Tutor 2')

        self.BT_pesquisar = ctk.CTkButton(
            self, text='Pesquisa!',
            font=('', 32, 'normal'),
            border_spacing=8,
            command=self._pesquisa_button_event
        )
        
        self.BT_editar_observacoes = ctk.CTkButton(
            self, text='Editar',
            font=('', 32, 'normal'),
            border_spacing=8,
            command=self._editar_observacao
        )

        self.BT_cancelar_editar = ctk.CTkButton(
            self, text='Cancelar',
            font=('', 32, 'normal'),
            border_spacing=8,
            command=self._cancelar_edicao
        )

        #AREA DE PESQUISA
        self.var_busca = ctk.StringVar(name='PY_BUSCA', value='')
        self.var_tipo_busca = ctk.IntVar(name='PY_TIPO_BUSCA')
        
        self.label_busca = ctk.CTkLabel(self, text='Busca:', font=('', 32, 'normal'))
        self.busca = ctk.CTkEntry(
            self, textvariable=self.var_busca,
            font=('', 22, 'normal')
        )
        self.busca.bind('<Return>', self.listagem)
        # self.busca.unbind
                
        self.radio_pet = ctk.CTkRadioButton(self, text='PET', font=('', 26, 'normal'), value=1, variable=self.var_tipo_busca, command=self._radio_callback)
        self.radio_tutor = ctk.CTkRadioButton(self, text='TUTOR', font=('', 26, 'normal'), value=2, variable=self.var_tipo_busca, command=self._radio_callback)
        self.var_tipo_busca.set(1)

        self.tabela_resultado = FramePesquisa(self)
        self._radio_callback()

        self.BT_buscar = ctk.CTkButton(
            self, text='Pesquisar',
            font=('', 20, 'normal'),
            border_spacing=8,
            command=self.listagem
        )

        self.BT_voltar = ctk.CTkButton(
            self, text='Voltar',
            font=('', 22, 'normal'),
            border_spacing=8,
            command=self._home_button_event
        )
        

        self._seleciona_frame("home")


    def listagem(self, *args):
        raise NotImplementedError("Please Implement this method")
    

    def salvar_observacoes(self):
        raise NotImplementedError("Please Implement this method")


    def busca(self, data):
        raise NotImplementedError("Please Implement this method")


    def _radio_callback(self):
        self.tabela_resultado.muda_header(self.var_tipo_busca.get())
        self.listagem()


    def _editar_observacao(self):
        self.BT_cancelar_editar.grid(row=3, column=1,  sticky='nsw', padx=10, pady=10)
        self.BT_editar_observacoes.configure(text='Salvar', command=self.salvar_observacoes)
        self.pet.observacoes.configure(state='normal', fg_color='white')
    

    def _cancelar_edicao(self):
        self.BT_cancelar_editar.grid_forget()
        self.BT_editar_observacoes.configure(text='Editar', command=self._editar_observacao)
        self.pet.reset_observacao()
        self.pet.observacoes.configure(state='disable', fg_color='transparent')
    

    def _seleciona_frame(self, frame):
        if frame == "home":
            self.grid_columnconfigure(0, weight=2)
            self.grid_columnconfigure(1, weight=1)
            self.grid_rowconfigure((0,3), weight=0)
            self.grid_rowconfigure((1,2), weight=1)
            self.pet.grid(row=1, column=0, padx=10, pady=(10, 0), rowspan=2, sticky='ewsn')
            self.tutor1.grid(row=1, column=1, padx=10, pady=(10, 0), sticky='ewsn')
            self.tutor2.grid(row=2, column=1, padx=10, pady=(10, 0), sticky='ewsn')
            self.BT_pesquisar.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)
            self.BT_editar_observacoes.grid(row=3, column=1,  sticky='nse', padx=10, pady=10)
            
            
        else:
            self.pet.grid_forget()
            self.tutor1.grid_forget()
            self.tutor2.grid_forget()
            self.BT_pesquisar.grid_forget()
            self.BT_editar_observacoes.grid_forget()

        if frame == "pesquisa":
            self.grid_columnconfigure(0, weight=0)
            self.grid_columnconfigure(1, weight=1)
            self.grid_rowconfigure(1, weight=0)
            self.grid_rowconfigure(2, weight=1)
            self.label_busca.grid(row=0, column=0, padx=(30, 10), pady=(30, 10))
            self.busca.grid(row=0, column=1, sticky='new', padx=30, pady=(30, 10))
            self.radio_pet.grid(row=1, column=0, sticky='n', padx=(30, 10), pady=10)
            self.radio_tutor.grid(row=1, column=1, sticky='nw', padx=(0, 10), pady=10)
            self.tabela_resultado.grid(row=2, column=0, columnspan=2, sticky='news', padx=10, pady=10)
            self.BT_voltar.grid(row=3, column=0, padx=(30, 10), pady=(30, 10))
            self.BT_buscar.grid(row=1, column=1, sticky='ne', padx=(0, 10), pady=10)

        else:
            self.tabela_resultado.grid_forget()
            self.busca.grid_forget()
            self.label_busca.grid_forget()
            self.radio_pet.grid_forget()
            self.radio_tutor.grid_forget()
            self.BT_voltar.grid_forget()
            self.BT_buscar.grid_forget()

        if frame == "cadastro":
            ...
        else:
            ...
        

    def _home_button_event(self):
        self._seleciona_frame("home")

    def _pesquisa_button_event(self):
        self._seleciona_frame("pesquisa")

    def _cadatro_button_event(self):
        self._seleciona_frame("cadastro")



if __name__ == '__main__':  
    app = App()
    app.mainloop()  
