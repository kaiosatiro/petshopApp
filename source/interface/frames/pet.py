import customtkinter as ctk
from PIL import Image
import os
from .fotos import FrameFotos


class FramePet(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(9, weight=1)

        self.racas_lista = []
        self.porte_lista = ['Pequeno', 'Médio', 'Grande']
        self.sexo_lista = ['Macho', 'Fêmea']
        
        #VARIAVEIS DOS VALORES MOSTRADOS
        self.var_id = ctk.IntVar(value=None)
        self.var_nome = ctk.StringVar(value='- -')
        self.var_raca = ctk.StringVar(value='- -')
        self.var_porte = ctk.StringVar(value='- -')  
        self.var_sexo = ctk.StringVar(value='- -')
        self.var_obs = ctk.StringVar()
        
        #VARIAVEIS DOS VALORES QUE RECEBEM A EDICAO
        self.var_nome_ed = ctk.StringVar()
        self.var_raca_ed = ctk.StringVar()
        self.var_porte_ed = ctk.StringVar()
        self.var_sexo_ed = ctk.StringVar()

        #WIDGETS DOS VALORES DO PET
        #________ IMAGEM _________
        self.frame_foto = FrameFotos(self)
        self.frame_foto.grid(row=0, column=0, rowspan=8, sticky='nsew', padx=10, pady=(10, 0))
        
        #__________ NOME _________
        self.nome = ctk.CTkLabel(self, textvariable=self.var_nome, font=('', 28, 'normal'))
        self.nome.grid(row=1, column=1, padx=10, pady=10, sticky='ew', columnspan=3)

        self.label_nome = ctk.CTkLabel(self, text='Nome:', font=('', 22, 'bold')).grid(row=0, column=1, pady=(10, 0))
        
        self.nome_ed = ctk.CTkEntry(
            self, textvariable=self.var_nome_ed,
            font=('', 28, 'normal'), justify='left'
        )

        #__________ RACA _________
        self.raca = ctk.CTkLabel(self, textvariable=self.var_raca, font=('', 28, 'normal'))
        self.raca.grid(row=3, column=1, padx=10, pady=10, sticky='ew', columnspan=3)

        self.label_raca = ctk.CTkLabel(self, text='Raça:', font=('', 22, 'bold')).grid(row=2, column=1)
        
        self.raca_ed = ctk.CTkOptionMenu( 
            self, variable=self.var_raca_ed,
            state='normal', values=self.racas_lista,
            font=('', 28, 'normal'), dropdown_font=('', 26, 'normal'),
        )

        # _________ SEXO __________
        self.sexo = ctk.CTkLabel(self, textvariable=self.var_sexo, font=('', 28, 'normal'))
        self.sexo.grid(row=5, column=1, padx=10, pady=10, sticky='ew')

        self.label_sexo = ctk.CTkLabel(self, text='Sexo:', font=('', 22, 'bold')).grid(row=4, column=1)

        self.sexo_ed = ctk.CTkOptionMenu(
            self, variable=self.var_sexo_ed,
            state='normal', values=self.sexo_lista,
            font=('', 28, 'normal'), dropdown_font=('', 26, 'normal'),
        )

        # _________ PORTE __________        

        self.porte = ctk.CTkLabel(self, textvariable=self.var_porte, font=('', 28, 'normal'))
        self.porte.grid(row=7, column=1, padx=10, pady=10, sticky='ew')

        self.label_porte = ctk.CTkLabel(self, text='Porte:', font=('', 22, 'bold')).grid(row=6, column=1)
        
        self.porte_ed = ctk.CTkOptionMenu(
            self, variable=self.var_porte_ed,
            state='normal', values=self.porte_lista,
            font=('', 28, 'normal'), dropdown_font=('', 26, 'normal'),
        )

        # _________ OBSERVACOES __________        
        self.label_observacoes = ctk.CTkLabel(self, text='Observações', font=('', 26, 'bold'))
        self.label_observacoes.grid(row=8, column=0, sticky='w', padx=10, pady=(0, 5)) #pack(expand=True, fill="both") ??????
        self.observacoes = ctk.CTkTextbox(
            self, corner_radius=6, font=('', 22, 'normal'),
            fg_color='transparent'
            )
        self.observacoes.grid(row=9, column=0, columnspan=5, sticky='nsew', padx=10, pady=(0, 10))
        self.observacoes.insert("0.0", '...')
        self.observacoes.configure(state='disable')

        bt_img = ctk.CTkImage(Image.open(os.path.realpath("source/interface/images/bt_img.png")), size=(28,28))#
        self.BT_editar_obs = ctk.CTkButton(
            self, text='', width=28, image=bt_img,
            command=master._editar_observacao,
            state='disabled'
        )
        self.BT_editar_obs.grid(row=8, column=0, sticky='w', padx=180, pady=5)
    

    def reset(self):
        self.var_id.set(0)
        self.var_nome.set('')
        self.var_raca.set('')
        self.var_porte.set('')
        self.var_sexo.set('')
        self.var_obs.set('')
        self.reset_observacao()


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
            'observacoes': self.get_observacoes(),
            'foto_id': self.frame_foto.get_id()
        }
    
    def get_novos(self):
        return {
            'id': self.var_id.get(),
            #_____NOVOS______
            'nome': self.var_nome_ed.get(),
            'raca': self.var_raca_ed.get(),
            'sexo': self.var_sexo_ed.get(),
            'porte': self.var_porte_ed.get(),
            'status_foto': self.frame_foto.new_foto(),
            'foto_dir': self.frame_foto.get_dir(),
            #_________________
            'foto_id': self.frame_foto.get_id()
        }
    

    def set(self, id:int, nome:str, raca:str, porte:str, sexo:str, observacoes:str=None, id_foto:int=0, foto=None):
        self.var_id.set(id)
        self.var_nome.set(nome)
        self.var_raca.set(raca)
        self.var_porte.set(porte)
        self.var_sexo.set(sexo)
        if observacoes:
            self.set_observacoes(observacoes)
        self.frame_foto.set_all(id_foto, foto)


    def get_observacoes(self):
        return self.observacoes.get('0.0', 'end')
    

    def set_observacoes(self, txt):
        self.var_obs.set(txt)
        self.observacoes.configure(state='normal')
        self.observacoes.delete("0.0", "end")
        self.observacoes.insert("0.0", txt)
        self.observacoes.configure(state='disable')


    def reset_observacao(self):
        self.observacoes.delete('0.0', 'end')
        self.observacoes.insert("0.0", self.var_obs.get())
    

    def ativa_edicao(self):
        self.var_nome_ed.set(self.var_nome.get())
        self.var_raca_ed.set(self.var_raca.get())
        self.var_porte_ed.set(self.var_porte.get())
        self.var_sexo_ed.set(self.var_sexo.get())
        
        self.nome.grid_forget()
        self.raca.grid_forget()
        self.sexo.grid_forget()
        self.porte.grid_forget()

        self.nome_ed.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
        self.raca_ed.grid(row=3, column=1, padx=10, pady=10, sticky='ew')
        self.sexo_ed.grid(row=5, column=1, padx=10, pady=10, sticky='ew')
        self.porte_ed.grid(row=7, column=1, padx=10, pady=10, sticky='ew')
        self.frame_foto.ativa_edicao()

        self.BT_editar_obs.configure(state='disabled')
    

    def ativa_adicao(self):
        self.var_nome_ed.set('')
        self.var_raca_ed.set('')
        self.var_porte_ed.set('')
        self.var_sexo_ed.set('')

        self.nome.grid_forget()
        self.raca.grid_forget()
        self.sexo.grid_forget()
        self.porte.grid_forget()

        self.nome_ed.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
        self.raca_ed.grid(row=3, column=1, padx=10, pady=10, sticky='ew')
        self.sexo_ed.grid(row=5, column=1, padx=10, pady=10, sticky='ew')
        self.porte_ed.grid(row=7, column=1, padx=10, pady=10, sticky='ew')
        self.frame_foto.ativa_adicao()

        self.BT_editar_obs.configure(state='disabled')

    
    def cancela_edicao(self):
        self.nome_ed.grid_forget()
        self.raca_ed.grid_forget()
        self.sexo_ed.grid_forget()
        self.porte_ed.grid_forget()

        self.nome.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
        self.raca.grid(row=3, column=1, padx=10, pady=10, sticky='ew')
        self.sexo.grid(row=5, column=1, padx=10, pady=10, sticky='ew')
        self.porte.grid(row=7, column=1, padx=10, pady=10, sticky='ew')
        self.frame_foto.cancela_edicao()

        self.BT_editar_obs.configure(state='normal')
    

    def _cancela_adicao(self):
        self.nome_ed.grid_forget()
        self.raca_ed.grid_forget()
        self.sexo_ed.grid_forget()
        self.porte_ed.grid_forget()

        self.nome.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
        self.raca.grid(row=3, column=1, padx=10, pady=10, sticky='ew')
        self.sexo.grid(row=5, column=1, padx=10, pady=10, sticky='ew')
        self.porte.grid(row=7, column=1, padx=10, pady=10, sticky='ew')
        self.frame_foto.cancela_adicao()

        self.BT_editar_obs.configure(state='normal')
        