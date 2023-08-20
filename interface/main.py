from frames import *


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title('petApp')
        self.geometry('1280x720')
        # self.attributes('-fullscreen', True)        
        # self.globalgetvar('PY_NOME_PET')

        #AREA PRINCIPAL
        self.pet = FramePet(self)
        self.tutor1 = FrameTutor(self, 'Tutor 1')   
        self.tutor2 = FrameTutor(self, 'Tutor 2')

        self.BT_pesquisar = ctk.CTkButton(
            self, text='Pesquisar',
            font=('', 32, 'normal'),
            border_spacing=8,
            command=self.pesquisa_button_event
        )

        #AREA DE PESQUISA
        self.var_busca = ctk.StringVar(name='PY_BUSCA', value='')
        self.var_tipo_busca = ctk.StringVar(name='PY_TIPO_BUSCA')
        
        self.label_busca = ctk.CTkLabel(self, text='Busca:', font=('', 32, 'normal'))
        self.busca = ctk.CTkEntry(
            self, textvariable=self.var_busca,
            font=('', 22, 'normal')
        )
        self.busca.bind('<Return>', self.query)
        # self.busca.unbind
                
        self.radio_pet = ctk.CTkRadioButton(self, text='PET', font=('', 26, 'normal'), value='PET', variable=self.var_tipo_busca, command=self._radio_callback)
        self.radio_tutor = ctk.CTkRadioButton(self, text='TUTOR', font=('', 26, 'normal'), value='TUTOR', variable=self.var_tipo_busca, command=self._radio_callback)
        self.var_tipo_busca.set('PET')

        self.tabela_resultado = FramePesquisa(self)
        self._radio_callback()

        self.BT_buscar = ctk.CTkButton(
            self, text='Buscar',
            font=('', 20, 'normal'),
            border_spacing=8,
            command=self.query
        )

        self.BT_voltar = ctk.CTkButton(
            self, text='Voltar',
            font=('', 22, 'normal'),
            border_spacing=8,
            command=self.home_button_event
        )
        # self.servicos = FrameServicos(self).grid(row=3, column=0, padx=10, pady=(10, 10), sticky='ewsn', columnspan=2)

        self.seleciona_frame("pesquisa")
        


    def _radio_callback(self):
        self.tabela_resultado.muda_header(self.var_tipo_busca.get())
    

    def query(self, *args):
        ####ABSTRATA??
        a = self.var_busca.get()
        query = [['...']]
        tipo = self.var_tipo_busca.get()
        self.tabela_resultado.set(tipo, query)


    def get_linha(self, data):
        print(data)


    def seleciona_frame(self, frame):
        if frame == "home":
            self.grid_columnconfigure(0, weight=2)
            self.grid_columnconfigure(1, weight=1)
            self.grid_rowconfigure((0,3), weight=0)
            self.grid_rowconfigure((1,2), weight=1)
            self.pet.grid(row=1, column=0, padx=10, pady=(10, 0), rowspan=2, sticky='ewsn')
            self.tutor1.grid(row=1, column=1, padx=10, pady=(10, 0), sticky='ewsn')
            self.tutor2.grid(row=2, column=1, padx=10, pady=(10, 0), sticky='ewsn')
            self.BT_pesquisar.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)
        else:
            self.pet.grid_forget()
            self.tutor1.grid_forget()
            self.tutor2.grid_forget()
            self.BT_pesquisar.grid_forget()

        if frame == "pesquisa":
            self.grid_columnconfigure(0, weight=0)
            self.grid_columnconfigure(1, weight=1)
            self.grid_rowconfigure(1, weight=0)
            self.grid_rowconfigure(2, weight=1)
            self.label_busca.grid(row=0, column=0, padx=(30, 10), pady=(30, 10))
            self.busca.grid(row=0, column=1, sticky='new', padx=30, pady=(30, 10))
            self.radio_pet.grid(row=1, column=0, sticky='n', padx=(30, 10), pady=10)
            self.radio_tutor.grid(row=1, column=1, sticky='nw', padx=(0, 10), pady=10)
            self.tabela_resultado.grid(row=2, column=0, columnspan=2, sticky='new', padx=10, pady=10)
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
        

    def home_button_event(self):
        self.seleciona_frame("home")

    def pesquisa_button_event(self):
        self.seleciona_frame("pesquisa")

    def cadatro_button_event(self):
        self.seleciona_frame("cadastro")




if __name__ == '__main__':
    ctk.set_appearance_mode("light")
    app = App()
    app.mainloop()  
