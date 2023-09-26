from .frames.pesquisa import *
from .frames.pet import *
from .frames.racas import *
from .frames.tutor import *
from .frames.tutores_lista import *
from .frames.tutor_painel import *
from .frames.arquivo import *


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # self.maxsize(600, 700)
        self.title('petApp')
        self.geometry('1380x720')
        ctk.set_appearance_mode("light")

        add_img = ctk.CTkImage(Image.open(os.path.realpath("source/interface/images/add_img.png")), size=(28,28))
        
        #VARS
        self.racas = []
        self.lista_tutores = []
        self.var_busca = ctk.StringVar(name='PY_BUSCA', value='')
        self.var_tipo_busca = ctk.IntVar(name='PY_TIPO_BUSCA', value=1)

        #FRAMES
        self.racas_frame = None
        self.tutores_listagem = None
        self.painel_tutor = None
        self.arquivo = None
        self.pet = FramePet(self)
        self.tutor1 = FrameTutor(self, 'Tutor 1')   
        self.tutor2 = FrameTutor(self, 'Tutor 2')
        self.tabela_resultado = FramePesquisa(self)
        
        #AREA DE PESQUISA
        self.label_busca = ctk.CTkLabel(self, text='Busca:', font=('', 32, 'normal'))
        self.entrada_busca = ctk.CTkEntry(
            self, textvariable=self.var_busca,
            font=('', 22, 'normal'))
        self.entrada_busca.bind('<Return>', self.listagem)

        self.radio_pet = ctk.CTkRadioButton(self, text='PET', font=('', 26, 'normal'), value=1, variable=self.var_tipo_busca, command=self._radio_callback)
        self.radio_tutor = ctk.CTkRadioButton(self, text='TUTOR', font=('', 26, 'normal'), value=2, variable=self.var_tipo_busca, command=self._radio_callback)
        self.label_titulo_tabela = ctk.CTkLabel(self, text='', font=('', 32, 'normal'))

        #BUTTONS
        self.BT_voltar = ctk.CTkButton(
            self, text='Voltar',
            font=('', 22, 'normal'),
            border_spacing=8,
            command=self._home_button_event
        )

        self.BT_buscar = ctk.CTkButton(
            self, text='Pesquisar',
            font=('', 20, 'normal'),
            border_spacing=8,
            command=self.listagem
        )     

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
            border_spacing=8
        )

        self.BT_racas = ctk.CTkButton(
            self, text='Raças',
            font=('', 26, 'normal'),
            border_spacing=4,
            command=self._frame_racas
        )

        self.BT_arquivo = ctk.CTkButton(
            self, text='Arquivo',
            font=('', 26, 'normal'),
            border_spacing=4,
            command=self._arquivo
        )

        self.BT_add_pet = ctk.CTkButton(
            self, text='Pet',
            font=('', 26, 'normal'),
            border_spacing=4,
            image=add_img,
            compound='left',
            width=130,
            height=50,
            command=self._adicionar_pet
        )

        self.BT_add_tutor = ctk.CTkButton(
            self, text='Tutor',
            font=('', 26, 'normal'),
            border_spacing=4,
            image=add_img,
            compound='left',
            width=150,
            height=50,
            command=self._adicionar_tutor
        )

        self.BT_remover_pet = ctk.CTkButton(
            self, text='Excluir Pet',
            font=('', 26, 'normal'),
            border_spacing=4,
            width=150,
            hover_color='red',
            command=self.excluir_pet    
        )
        
        self._radio_callback()
        self._seleciona_frame(1)


    def listagem(self, *args):
        raise NotImplementedError("Please Implement this method")

    def set_lista_tutores(self):
        raise NotImplementedError("Please Implement this method")   

    def set_racas_lista(self):
        raise NotImplementedError("Please Implement this method")
    
    def adicionar_raca(self, raca):
        raise NotImplementedError("Please Implement this method")

    def editar_raca(self):
        raise NotImplementedError("Please Implement this method")
 
    def salvar_edicao(self):
        raise NotImplementedError("Please Implement this method")

    def salvar_observacoes(self):
        raise NotImplementedError("Please Implement this method")
    
    def salvar_edicao_tutor(self):
        raise NotImplementedError("Please Implement this method")
    
    def salvar_novo_pet(self):
        raise NotImplementedError("Please Implement this method")

    def salvar_novo_tutor(self):
        raise NotImplementedError("Please Implement this method")

    def excluir_pet(self):
        raise NotImplementedError("Please Implement this method")
    
    def excluir_tutor(self):
        raise NotImplementedError("Please Implement this method")

    def excluir_raca(self, raca):
        raise NotImplementedError("Please Implement this method")
        
    def busca_dados(self, data):
        raise NotImplementedError("Please Implement this method")

    def busca_tutor(self):
        raise NotImplementedError("Please Implement this method")
    
    def busca_tutor_painel(self):
        raise NotImplementedError("Please Implement this method")

    def export_data(self, choice, path):
        raise NotImplementedError("Please Implement this method")
    
    def import_data(self, choice, path):
        raise NotImplementedError("Please Implement this method")
     

    def _arquivo(self):
        if self.arquivo is None or not self.arquivo.winfo_exists():
            self.arquivo = FrameArquivo(self)


    def _frame_racas(self):
        self.set_racas_lista()
        if self.racas_frame is None or not self.racas_frame.winfo_exists():
            self.racas_frame = FrameRacas(self, racas=self.racas, add_fn=self.adicionar_raca, edit_fn=self.editar_raca, del_fn=self.excluir_raca)
        

    def _frame_tutores(self):
        self.set_lista_tutores()
        if self.tutores_listagem is None or not self.tutores_listagem.winfo_exists():
            self.tutores_listagem = FrameListaTutores(self, self.lista_tutores)
        return self.tutores_listagem.get_choice()
    

    def _painel_tutor(self):
        if self.painel_tutor is None or not self.painel_tutor.winfo_exists():
            self.painel_tutor = TutorPainel(self)
            # self.wait_window(self.painel_tutor)
            # self.listagem()          


    def _radio_callback(self):
        if self.var_tipo_busca.get() == 1:
            self.label_titulo_tabela.configure(text='PETS')
        elif self.var_tipo_busca.get() == 2:
            self.label_titulo_tabela.configure(text='TUTORES')
        self.tabela_resultado.muda_header(self.var_tipo_busca.get())
        self.listagem()
    

    def _editar(self):
        self.BT_remover_pet.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='w')
        self.BT_cancelar_editar.grid(row=3, column=1,  sticky='nsw', padx=10, pady=10)
        self.BT_cancelar_editar.configure(command=self._cancelar_edicao)
        self.BT_editar.configure(text='Salvar', command=self.salvar_edicao)
        self.BT_pesquisar.configure(state='disabled')
        self.pet.set_racas(self.racas)
        self.pet.ativa_edicao()
        self.tutor1.ativa_edicao()
        self.tutor2.ativa_edicao()        


    def _editar_observacao(self):
        self.BT_cancelar_editar.grid(row=3, column=1,  sticky='nsw', padx=10, pady=10)
        self.BT_cancelar_editar.configure(command=self._cancelar_observacoes)
        self.BT_editar.configure(text='Salvar', command=self.salvar_observacoes)
        self.pet.observacoes.configure(state='normal', fg_color='white')
        self.BT_pesquisar.configure(state='disabled')
    

    def _adicionar_pet(self):
        self.pet.reset()
        self.tutor1.reset()
        self.tutor2.reset()
        self.pet.ativa_adicao()
        self.pet.set_racas(self.racas)
        self.tutor1.ativa_edicao()
        self.tutor2.ativa_edicao()
        self.BT_cancelar_editar.grid(row=3, column=1,  sticky='nsw', padx=10, pady=10)
        self.BT_cancelar_editar.configure(command=self._cancelar_adicao_pet)
        self.BT_editar.configure(text='Salvar', state='normal', command=self.salvar_novo_pet)
        self.BT_pesquisar.configure(state='disabled')
        self._seleciona_frame(1)
    

    def _adicionar_tutor(self):
        self._painel_tutor()
        self.painel_tutor.ativa_Adicao()


    def _cancelar_edicao(self):
        self.BT_remover_pet.grid_forget()
        self.BT_cancelar_editar.grid_forget()
        self.BT_editar.configure(text='Editar', command=self._editar)
        self.BT_pesquisar.configure(state='normal')
        self.pet.cancela_edicao()
        self.tutor1.cancela_edicao()
        self.tutor2.cancela_edicao()


    def _cancelar_observacoes(self):
        self.BT_cancelar_editar.grid_forget()
        self.BT_editar.configure(text='Editar', command=self._editar)
        self.pet.reset_observacao()
        self.pet.observacoes.configure(state='disable', fg_color='transparent')
        self.BT_pesquisar.configure(state='normal')
    

    def _cancelar_adicao_pet(self):
        self.pet.reset()
        self.tutor1.reset()
        self.tutor2.reset()
        self.pet._cancela_adicao()
        self.tutor1.cancela_edicao()
        self.tutor2.cancela_edicao()
        self.BT_cancelar_editar.grid_forget()
        self.BT_editar.configure(text='Editar', command=self._editar)
        self.BT_pesquisar.configure(state='normal')
        self.BT_voltar.configure(state='disabled')
        self._seleciona_frame(2)


    def _seleciona_frame(self, frame):
        if frame == 1:
            self.grid_columnconfigure(0, weight=2)
            self.grid_columnconfigure(1, weight=1)
            self.grid_rowconfigure((0,3), weight=0)
            self.grid_rowconfigure((1,2), weight=1)
            self.BT_racas.grid(row=0, column=1, padx=10, pady=(10, 0), sticky='e')
            self.BT_arquivo.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='w')
            self.pet.grid(row=1, column=0, padx=10, pady=(5, 0), rowspan=2, sticky='ewsn')
            self.tutor1.grid(row=1, column=1, padx=10, pady=(5, 0), sticky='ewsn')
            self.tutor2.grid(row=2, column=1, padx=10, pady=(10, 0), sticky='ewsn')
            self.BT_pesquisar.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)
            self.BT_editar.grid(row=3, column=1,  sticky='nse', padx=10, pady=10)
            if self.pet.var_id.get():
                self.BT_editar.configure(state='normal')
                self.pet.BT_editar_obs.configure(state='normal')
        else:
            self.BT_racas.grid_forget()
            self.BT_arquivo.grid_forget()
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
            self.BT_add_pet.grid(row=3, column=1, padx=(30, 240), pady=(30, 20), sticky='e')
            self.BT_add_tutor.grid(row=3, column=1, padx=(30, 40), pady=(30, 20), sticky='e')
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
            self.BT_add_pet.grid_forget()
            self.BT_add_tutor.grid_forget()

        if frame == 3:
            ...
        else:
            ...
        
    def _home_button_event(self):
        self._seleciona_frame(1)

    def _pesquisa_button_event(self):
        self.BT_voltar.configure(state='normal')
        self._radio_callback()
        self._seleciona_frame(2)

    def _cadatro_button_event(self):
        self._seleciona_frame(3)


if __name__ == '__main__':  
    app = App()
    app.mainloop()  
