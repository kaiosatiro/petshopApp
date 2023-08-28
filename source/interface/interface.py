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

        self.status_edicao = 0

        self.BT_pesquisar = ctk.CTkButton(
            self, text='Pesquisa!',
            font=('', 32, 'normal'),
            border_spacing=8,
            command=self._pesquisa_button_event
        )
        
        self.BT_editar = ctk.CTkButton(
            self, text='Editar',
            font=('', 32, 'normal'),
            border_spacing=8,
            command=self._editar,
            state='disabled'
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
        self.entrada_busca = ctk.CTkEntry(
            self, textvariable=self.var_busca,
            font=('', 22, 'normal')
        )
        self.entrada_busca.bind('<Return>', self.listagem)
        # self.busca.unbind
                
        self.radio_pet = ctk.CTkRadioButton(self, text='PET', font=('', 26, 'normal'), value=1, variable=self.var_tipo_busca, command=self._radio_callback)
        self.radio_tutor = ctk.CTkRadioButton(self, text='TUTOR', font=('', 26, 'normal'), value=2, variable=self.var_tipo_busca, command=self._radio_callback)
        self.var_tipo_busca.set(1)
        
        self.label_titulo_tabela = ctk.CTkLabel(self, text='', font=('', 32, 'normal'))

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
        

        # self._seleciona_frame(1)


    def listagem(self, *args):
        raise NotImplementedError("Please Implement this method")
    

    def salvar_edicao(self):
        raise NotImplementedError("Please Implement this method")


    def salvar_observacoes(self):
        raise NotImplementedError("Please Implement this method")


    def busca_dados(self, data):
        raise NotImplementedError("Please Implement this method")
    
    
    def set_racas(self):
        return self.racas_lista
    

    def _radio_callback(self):
        if self.var_tipo_busca.get() == 1:
            self.label_titulo_tabela.configure(text='PETS')
        elif self.var_tipo_busca.get() == 2:
            self.label_titulo_tabela.configure(text='TUTORES')
        self.tabela_resultado.muda_header(self.var_tipo_busca.get())
        self.listagem()
    

    def _editar(self):
        self.BT_cancelar_editar.grid(row=3, column=1,  sticky='nsw', padx=10, pady=10)
        self.BT_editar.configure(text='Salvar', command=self.salvar_edicao)
        self.BT_pesquisar.configure(state='disabled')

        ###############----------------################
        self.status_edicao = 1
        self.pet.ativa_edicao()
        self.tutor1.ativa_edicao()
        self.tutor2.ativa_edicao()        


    def _editar_observacao(self):
        self.BT_cancelar_editar.grid(row=3, column=1,  sticky='nsw', padx=10, pady=10)
        self.BT_editar.configure(text='Salvar', command=self.salvar_observacoes)
        self.pet.observacoes.configure(state='normal', fg_color='white')
        self.BT_pesquisar.configure(state='disabled')
        

    def _cancelar_edicao(self):
        self.BT_cancelar_editar.grid_forget()
        self.BT_editar.configure(text='Editar', command=self._editar)
        self.pet.reset_observacao()
        self.pet.observacoes.configure(state='disable', fg_color='transparent')
        self.BT_pesquisar.configure(state='normal')

        if self.status_edicao:
            self.pet.cancela_edicao()
            self.tutor1.cancela_edicao()
            self.tutor2.cancela_edicao()


    def _seleciona_frame(self, frame):
        if frame == 1:
            self.grid_columnconfigure(0, weight=2)
            self.grid_columnconfigure(1, weight=1)
            self.grid_rowconfigure((0,3), weight=0)
            self.grid_rowconfigure((1,2), weight=1)
            self.pet.grid(row=1, column=0, padx=10, pady=(10, 0), rowspan=2, sticky='ewsn')
            self.tutor1.grid(row=1, column=1, padx=10, pady=(10, 0), sticky='ewsn')
            self.tutor2.grid(row=2, column=1, padx=10, pady=(10, 0), sticky='ewsn')
            self.BT_pesquisar.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)
            self.BT_editar.grid(row=3, column=1,  sticky='nse', padx=10, pady=10)

            if self.pet.var_id.get():
                self.BT_editar.configure(state='normal')
                self.pet.BT_editar_obs.configure(state='normal')
                
            
        else:
            self.pet.grid_forget()
            self.tutor1.grid_forget()
            self.tutor2.grid_forget()
            self.BT_pesquisar.grid_forget()
            self.BT_editar.grid_forget()

        if frame == 2:
            self.grid_columnconfigure(0, weight=0)
            self.grid_columnconfigure(1, weight=1)
            self.grid_rowconfigure(1, weight=0)
            self.grid_rowconfigure(2, weight=1)
            self.label_busca.grid(row=0, column=0, padx=(30, 10), pady=(30, 10))
            self.entrada_busca.grid(row=0, column=1, sticky='new', padx=30, pady=(30, 10))
            self.radio_pet.grid(row=1, column=0, sticky='n', padx=(30, 10), pady=10)
            self.radio_tutor.grid(row=1, column=1, sticky='nw', padx=(0, 10), pady=10)
            self.tabela_resultado.grid(row=2, column=0, columnspan=2, sticky='news', padx=10, pady=(0, 10))
            self.BT_voltar.grid(row=3, column=0, padx=(30, 10), pady=(30, 10))
            self.BT_buscar.grid(row=1, column=1, sticky='ne', padx=(0, 10), pady=10)
            self.label_titulo_tabela.grid(row=1, column=1, sticky='s', padx=(0, 230), pady=(60, 0))
            
        else:
            self.tabela_resultado.grid_forget()
            self.entrada_busca.grid_forget()
            self.label_busca.grid_forget()
            self.radio_pet.grid_forget()
            self.radio_tutor.grid_forget()
            self.BT_voltar.grid_forget()
            self.BT_buscar.grid_forget()
            self.label_titulo_tabela.grid_forget()

        if frame == 3:
            ...
        else:
            ...
        

    def _home_button_event(self):
        self._seleciona_frame(1)


    def _pesquisa_button_event(self):
        self._seleciona_frame(2)


    def _cadatro_button_event(self):
        self._seleciona_frame(3)



if __name__ == '__main__':  
    app = App()
    app.mainloop()  
