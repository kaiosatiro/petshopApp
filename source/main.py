# from backend.functions import *
# from interface.interface import *
import backend.functions as fn
import interface.interface as it

class main(it.App):
    def __init__(self):
        super().__init__()
        # self.globalgetvar('PY_NOME_PET')
        self.racas_lista = [r[0] for r in fn.consulta_racas()]
        self.porte_lista = ['P', 'M', 'G']
        self.sexo_lista = ['Macho', 'Fêmea']

        self._seleciona_frame('pesquisa')
    

    def listagem(self, *args):
        dado = self.var_busca.get()
        print(dado)
        if self.var_tipo_busca.get() == 1:
            call = fn.consulta_pet(dado)
            self.tabela_resultado.set(1, call)
        elif self.var_tipo_busca.get() == 2:
            call = fn.consulta_tutor(dado)
            print(call)
            self.tabela_resultado.set(2, call)
    

    def salvar_observacoes(self):
        ...


    def busca(self, data):
        ...


if __name__ == '__main__':
    app = main()
    app.mainloop()
    # print(app.racas_lista)

