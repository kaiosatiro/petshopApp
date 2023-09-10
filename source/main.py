# from backend.functions import *
# from interface.interface import *
import backend.functions as fn
import interface.interface as it
from  CTkMessagebox import CTkMessagebox
# PRAGMA foreign_keys = TRUE

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
    

    def busca_tutor(self, i):
        call = fn.consulta_tutor_porId(i)
        return call[0]


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
            CTkMessagebox(title="Erro", message="Raça já existe", icon="cancel", font=('', 18, 'normal'))
    

    def editar_raca(self, raca, raca_nova):
        call = fn.atualiza_raca(raca, raca_nova)
        if call == 1:
            self.set_racas_lista()
        if call == 2067:
            CTkMessagebox(title="Erro", message="Raça já existe", icon="cancel", font=('', 18, 'normal'))
            

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
    

    def busca_dados(self, pet_id):
        call_a = fn.consulta_pet_porId(pet_id)
        call_b = fn.consulta_relacao_tutores_pet(pet_id)

        self.pet.set(
            call_a[0][0],
            call_a[0][1],
            call_a[0][2],
            call_a[0][3],
            call_a[0][4],
            call_a[0][5],                
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
                title="SEM TUTOR", icon="cancel", 
                message=f"{pet['nome']} precisa de um tutor !!!",
                font=('', 16, 'normal')
            )
            return
        nome = pet['nome'].strip()
        if not nome:
            CTkMessagebox(
                title="NOME EM BRANCO", icon="cancel", 
                message="Preencha todos os campos !",
                font=('', 16, 'normal')
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
            self._cancelar_edicao()
            self.busca_dados(int(pet['id']))
        

    def salvar_novo_pet(self):
        pet = self.pet.get_novos()
        if not self.tutor1.exists() and not self.tutor2.exists():
            CTkMessagebox(
                title="SEM TUTOR", icon="cancel", 
                message=f"{pet['nome']} precisa de um tutor !!!",
                font=('', 16, 'normal')
            )
            return
        
        nome = pet['nome'].strip()
        raca = pet['nome'].strip()
        sexo = pet['nome'].strip()
        porte = pet['nome'].strip()
        if not nome or not raca or not sexo or not porte:
            CTkMessagebox(
                title="CAMPOS EM BRANCO", icon="cancel", 
                message="Preencha todos os campos !",
                font=('', 16, 'normal')
            )
            return
        #ADICAO DO PET E DA RELACAO COM TUTOR
        call = fn.add_pet(pet['nome'], pet['raca'], pet['porte'], pet['sexo'])
        if self.tutor1.exists():
            tid = self.tutor1.get_new_id()
            fn.add_relacao(tid, call[0])
        if self.tutor2.exists():
            tid = self.tutor2.get_new_id()
            fn.add_relacao(tid, call[0])
        CTkMessagebox(
                title="Aviso", icon="check", 
                message="Pet Criado!",
                font=('', 16, 'normal'),
                justify='center'
            )
        self.busca_dados(int(call[0]))
        self.pet.cancela_edicao()
        self.tutor1.finaliza_adicao()
        self.tutor2.finaliza_adicao()
        self.BT_cancelar_editar.grid_forget()
        self.BT_editar.configure(text='Editar', command=self._editar)
        self.BT_pesquisar.configure(state='normal')
        self._seleciona_frame(1)


    def excluir_pet(self):
        pet = self.pet.get()
        msg = CTkMessagebox(
                title="ATENÇÂO!", icon="warning", 
                message=f"Excluir {pet['nome']}.\nVocê tem certeza?",
                font=('', 16, 'normal'),
                sound=True,
                option_1='Sim',
                option_2='Não, cancelar',  
                justify='center'
            )
        if msg.get() == 'Sim':
            call = fn.remove_pet(int(pet['id']))
            if call:
                CTkMessagebox(
                title="Aviso", icon="check", 
                message="Pet Excluído!",
                font=('', 16, 'normal'),
                justify='center'
            )
            self._cancelar_edicao()
            self._seleciona_frame(2)

    


if __name__ == '__main__':
    app = main()
    app.mainloop()

