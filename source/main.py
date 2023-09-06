# from backend.functions import *
# from interface.interface import *
import backend.functions as fn
import interface.interface as it

# PRAGMA foreign_keys = TRUE

class main(it.App):
    def __init__(self):
        super().__init__()
        # self.globalgetvar('PY_NOME_PET')
        # self.freq_lista = ['Semanal', 'Mensal', 'Esporático']
        
        self.set_racas_lista()
        self.pet.set_racas(self.racas)
        self._seleciona_frame(1)
    

    def set_racas_lista(self):
        self.racas.clear()
        self.racas = [r[0] for r in fn.consulta_racas()]
    

    def adicionar_raca(self, raca):
        fn.add_raca(raca)
        self.set_racas_lista()
    

    def editar_raca(self):
        ...
        

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
    

    def busca_dados(self, *args):
        if args[0]['row'] == 0:
            pass
        
        elif self.var_tipo_busca.get() == 1:
            linha = args[0]['row']
            pet_id = int(self.tabela_resultado.get_id(linha))
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
                    call_b[0][0],
                    call_b[1][1],
                    call_b[1][2],
                    call_b[1][3],
                    call_b[1][4],
                )
            else:
                self.tutor2.set(
                    None,
                    '-',
                    '-',
                    '-',
                    '...',
                )
            
            self._seleciona_frame(1)


        elif self.var_tipo_busca.get()  == 2:
            linha = args[0]['row']
            tutor_id = self.tabela_resultado.get_id(linha)
            tutor_nome = self.tabela_resultado.get_nome(linha)
            call = fn.consulta_relacao_pets_tutor(tutor_id)
            if call:
                self.label_titulo_tabela.configure(text=f'{tutor_nome} PETS')
                self.tabela_resultado.set(1, call)
            else:
                self.label_titulo_tabela.configure(text=f'{tutor_nome} não tem Pets cadastrados')
                self.tabela_resultado.set(1, call)
            self.var_tipo_busca.set(1)


    def salvar_observacoes(self):
        pet = self.pet.get()
        fn.atualiza_observacao(int(pet['id']), pet['observacoes'])
        call = fn.consulta_pet_porId(int(pet['id']))

        self.pet.set(
                call[0][0],
                call[0][1],
                call[0][2],
                call[0][3],
                call[0][4],
                call[0][5],                
            )
        
        self.BT_cancelar_editar.grid_forget()
        self.BT_editar_observacoes.configure(text='Editar', command=self._editar_observacao)
        self.pet.observacoes.configure(state='disabled', fg_color='transparent')
        self.BT_pesquisar.configure(state='normal')


if __name__ == '__main__':
    app = main()
    app.mainloop()

