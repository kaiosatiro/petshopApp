from io import BytesIO
import backend.functions as fn
import interface.interface as it
from  CTkMessagebox import CTkMessagebox

class main(it.App):
    def __init__(self):
        super().__init__()
        # self.globalgetvar('PY_NOME_PET')
        # self.freq_lista = ['Semanal', 'Mensal', 'Esporático']
        
        self.set_racas_lista()
        self.pet.set_racas(self.racas)
        self.set_lista_tutores()
        self._seleciona_frame(2)
    

    def set_lista_tutores(self):
        self.lista_tutores.clear()
        for r in fn.consulta_tutores():
            self.lista_tutores.append(list(r))
    

    def set_racas_lista(self):
        self.racas.clear()
        for r in fn.consulta_racas():
            self.racas.append(r[0]) 
        self.pet.set_racas(self.racas)
            

    def adicionar_raca(self, raca):
        call = fn.add_raca(raca)
        if call == 1:
            self.set_racas_lista()
        elif call == 2067:
            CTkMessagebox(
                self.racas_frame,
                title="Erro", message="Raça já existe", 
                icon="cancel", font=('', 18, 'normal'),
                justify='center', option_focus=1
            )
    

    def editar_raca(self, raca, raca_nova):
        call = fn.atualiza_raca(raca, raca_nova)
        if call == 1:
            self.set_racas_lista()
        if call == 2067:
            CTkMessagebox(
                self.racas_frame,
                title="Erro", message="Raça já existe", 
                icon="cancel", font=('', 18, 'normal'),
                justify='center', option_focus=1
            )
            

    def listagem(self, *args):
        dado = self.var_busca.get()
        if self.var_tipo_busca.get() == 1:
            self.label_titulo_tabela.configure(text='PETS')
            call = fn.consulta_pet(dado)
            self.tabela_resultado.set(1, call)
        elif self.var_tipo_busca.get() == 2:
            self.label_titulo_tabela.configure(text='TUTORES')
            call = fn.consulta_tutor(dado)
            self.tabela_resultado.set(2, call)
    

    def busca_tutor(self, i):
        call = fn.consulta_tutor_porId(i)
        return call[0]
    

    def busca_tutor_painel(self, i):
        call = fn.consulta_tutor_porId(i)
        id_ = call[0][0]
        nome = call[0][1]
        tel1 = call[0][2]
        tel2 = call[0][3]
        endereco = call[0][4]
        self._painel_tutor()
        self.painel_tutor.set(id_, nome, tel1, tel2, endereco)
    

    def busca_dados(self, pet_id):
        call_a = fn.consulta_pet_porId(pet_id)
        call_b = fn.consulta_relacao_tutores_pet(pet_id)
        call_Foto = fn.consulta_foto_por_pet(pet_id)
        
        if call_Foto:
            id_foto = call_Foto[0][0]
            foto = BytesIO(call_Foto[0][1])
        else:
            id_foto = 0
            foto = None


        self.pet.set(
            call_a[0][0],
            call_a[0][1],
            call_a[0][2],
            call_a[0][3],
            call_a[0][4],
            call_a[0][5],
            id_foto,
            foto
        )

        self.tutor1.set(
            call_b[0][0],
            call_b[0][1],
            call_b[0][2],
            call_b[0][3],
            call_b[0][4],
        )   

        if len(call_b) == 2:    
            self.tutor2.set(
                call_b[1][0],
                call_b[1][1],
                call_b[1][2],
                call_b[1][3],
                call_b[1][4],
            )
        else:
            self.tutor2.set(
                0,
                '-',
                '-',
                '-',
                '...',
            )
        
        self._seleciona_frame(1)
    

    def salvar_edicao_tutor(self):
        get = self.painel_tutor.get()
        id_ = get['id']
        nome = get['nome'].strip()
        tel1 = get['tel1'].strip()
        tel2 = get['tel2']
        endereco = get['endereco']
        if not nome or not tel1:
            CTkMessagebox(
                self.painel_tutor,
                title="CAMPOS EM BRANCO", icon="cancel", 
                message="Tutor precisa de um nome e ao menos um telefone!",
                font=('', 16, 'normal'),
                justify='center',
                option_focus=1
            )
            return None
        call = fn.atualiza_tutor(id_, nome, tel1, tel2, endereco)
        return call


    def salvar_observacoes(self):
        pet = self.pet.get()
        fn.atualiza_observacao(int(pet['id']), pet['observacoes'])
        call = fn.consulta_pet_porId(int(pet['id']))
        self.pet.set_observacoes(call[0][5])
        self._cancelar_observacoes()


    def salvar_edicao(self):
        pet = self.pet.get_novos()
        if not self.tutor1.exists() and not self.tutor2.exists():
            CTkMessagebox(
                self,
                title="SEM TUTOR", icon="cancel", 
                message=f"{pet['nome']} precisa de um tutor !!!",
                font=('', 16, 'normal'),
                sound=True,
                justify='center',
                option_focus=1
            )
            return
        nome = pet['nome'].strip()
        if not nome:
            CTkMessagebox(
                self,
                title="NOME EM BRANCO", icon="cancel", 
                message="Preencha todos os campos !",
                font=('', 16, 'normal'),
                sound=True,
                justify='center',
                option_focus=1
            )
            return
        else:
            # ATUALIZA TUTOR
            if self.tutor1.foi_trocado():
                fn.remove_relacao(
                    pet['id'], 
                    self.tutor1.get_old_id()
                )
                if self.tutor1.exists():
                    fn.add_relacao(
                        self.tutor1.get_new_id(),
                        pet['id']
                    )
            if self.tutor2.foi_trocado():
                fn.remove_relacao(
                    pet['id'], 
                    self.tutor2.get_old_id()
                )
                if self.tutor2.exists():
                    fn.add_relacao(
                        self.tutor2.get_new_id(),
                        pet['id']
                    )
            # ATUALIZA PET
            fn.atualiza_pet(int(pet['id']), pet['nome'], pet['raca'], pet['porte'], pet['sexo'])
            # FOTO
            if pet['status_foto']:
                dir_ = pet['foto_dir']
                with open(dir_, 'rb') as file:
                    blob = file.read()
                    if not fn.consulta_foto_Id(pet['id']):
                        tupla = (blob, pet['id'])
                        fn.adiciona_foto(tupla)
                    else:
                        tupla = (blob, pet['foto_id'])
                        fn.atualiza_foto(tupla)#(bytes, int)
            self._cancelar_edicao() 
            self.busca_dados(int(pet['id']))
    

    def salvar_novo_tutor(self):
        get = self.painel_tutor.get()
        nome = get['nome'].strip()
        tel1 = get['tel1'].strip()
        tel2 = get['tel2']
        endereco = get['endereco']
        if not nome or not tel1:
            CTkMessagebox(
                self.painel_tutor,
                title="CAMPOS EM BRANCO", icon="cancel", 
                message="Tutor precisa de um nome e ao menos um telefone!",
                font=('', 16, 'normal'),
                justify='center',
                option_focus=1
            )
            return None
        
        call = fn.add_tutor(nome, tel1, tel2, endereco)
        if call:
            CTkMessagebox(
                title="Aviso", icon="check", 
                message="Tutor Criado!",
                font=('', 16, 'normal'),
                justify='center'
            )
            return call
        

    def salvar_novo_pet(self):
        pet = self.pet.get_novos()
        if not self.tutor1.exists() and not self.tutor2.exists():
            CTkMessagebox(
                self,
                title="SEM TUTOR", icon="cancel", 
                message=f"{pet['nome']} precisa de um tutor !!!",
                font=('', 16, 'normal'),
                justify='center',                
                option_focus=1, 
                sound=True  
            )
            return
        
        nome = pet['nome'].strip()
        raca = pet['nome'].strip()
        sexo = pet['nome'].strip()
        porte = pet['nome'].strip()
        if not nome or not raca or not sexo or not porte:
            CTkMessagebox(
                self,
                title="CAMPOS EM BRANCO", icon="cancel", 
                message="Preencha todos os campos !",
                font=('', 16, 'normal'),
                justify='center',                
                option_focus=1,   
                sound=True      
            )
            return
        #ADICAO DO PET, FOTO, E DA RELACAO COM TUTOR
        call = fn.add_pet(pet['nome'], pet['raca'], pet['porte'], pet['sexo'])
        #------
        if pet['status_foto']:
            dir_ = pet['foto_dir']
            with open(dir_, 'rb') as file:
                blob = file.read()
                tupla = (blob, int(call[0]))
                fn.adiciona_foto(tupla)#(bytes, int)
        #------
        if self.tutor1.exists():
            tid = self.tutor1.get_new_id()
            fn.add_relacao(tid, call[0])
        if self.tutor2.exists():
            tid = self.tutor2.get_new_id()
            fn.add_relacao(tid, call[0])
        CTkMessagebox(
                self,
                title="Aviso", icon="check", 
                message="Pet Criado!",
                font=('', 16, 'normal'),
                justify='center',
                option_focus=1
            )
        self.pet._cancela_adicao()
        self.tutor1.finaliza_adicao()
        self.tutor2.finaliza_adicao()
        self.BT_cancelar_editar.grid_forget()
        self.BT_editar.configure(text='Editar', command=self._editar)
        self.BT_pesquisar.configure(state='normal')
        self.busca_dados(int(call[0]))


    def excluir_pet(self):
        pet = self.pet.get()
        msg = CTkMessagebox(
                self,
                title="ATENÇÂO!", icon="warning", 
                message=f"Excluir {pet['nome']}.\nVocê tem certeza?",
                font=('', 16, 'normal'),
                sound=True,
                option_1='Sim',
                option_2='Não, cancelar',  
                justify='center',
                option_focus=1                
            )
        if msg.get() == 'Sim':
            call = fn.remove_pet(int(pet['id']))
            if call:
                CTkMessagebox(
                self,
                title="Aviso", icon="check", 
                message="Pet Excluído!",
                font=('', 16, 'normal'),
                justify='center',
                option_focus=1
            )
            self._cancelar_edicao()
            self._pesquisa_button_event()


    def excluir_tutor(self, id_, nome):
        msg = CTkMessagebox(
            self.painel_tutor,
            justify='center',
            title="Excluir Tutor?", message=f"Excluir definitivamente {nome} ?", 
            icon="question", font=('', 18, 'normal'),
            option_1='Sim', option_2='Não',
            option_focus=1,
        )
        if msg.get() == 'Sim':            
            check = fn.consulta_pets_com_apenas_um_tutor_por_tutor_id(id_)
            if check or check != []:
                msg = CTkMessagebox(
            self.painel_tutor,
            title="Excluir PETS?",
            width=500, justify='center',
            message=f"Pets que não possuem outro tutor tambem serão excluídos.\nTem certeza? (Pets com outro tutor permanecem)", 
            icon="warning", font=('', 18, 'normal'),
            sound=True, option_focus=1,
            option_1='Tenho', option_2='Não'
                )
                if msg.get() == 'Tenho':
                    for i in check:
                        fn.remove_pet(i[0])  
                else:
                    return
            call = fn.remove_tutor(id_)
            if call:
                CTkMessagebox(
                self,
                title="Aviso", icon="check", 
                message="Excluído!",
                font=('', 16, 'normal'),
                justify='center',
                option_focus=1
            )
                return 1


if __name__ == '__main__':
    app = main()
    app.mainloop()

