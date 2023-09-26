import backend.query_functions as qf
import backend.arquivo_functions as arqF
import backend.database as db
import interface.interface as it
import interface.frames.messages as msg


class main(it.App):
    def __init__(self, dBinterface):
        #DB Inicialization
        self.dBI = dBinterface
        super().__init__()
        self.set_racas_lista()
        self._seleciona_frame(1)


    def set_lista_tutores(self):
        self.lista_tutores.clear()
        for r in qf.consulta_tutores(self.dBI):
            self.lista_tutores.append(list(r))
    

    def set_racas_lista(self):
        self.racas.clear()
        for r in qf.consulta_racas(self.dBI):
            self.racas.append(r[0]) 
        self.pet.set_racas(self.racas)
            

    def adicionar_raca(self, raca):
        call = qf.add_raca(self.dBI, raca.strip())
        if call[0] == raca.title():
            self.set_racas_lista()
            self.racas_frame.update_list()            
        elif call[0] == 'error':
            msg.error_message_bd(self.racas_frame, call[1])
    

    def editar_raca(self, raca, raca_nova):
        call = qf.atualiza_raca(self.dBI, raca, raca_nova.strip())
        if call[0] == raca.title():
            self.set_racas_lista()
            self.racas_frame.update_list()            
        elif call[0] == 'error':
            msg.error_message_bd(self.racas_frame, call[1])
            

    def listagem(self, *args):
        dado = self.var_busca.get()
        if self.var_tipo_busca.get() == 1:
            self.label_titulo_tabela.configure(text='PETS')
            call = qf.consulta_pet(self.dBI, dado)
            if call[0] == 'error':
                msg.error_message_bd(self, call[1])
                return
            self.tabela_resultado.set(1, call)
        elif self.var_tipo_busca.get() == 2:
            self.label_titulo_tabela.configure(text='TUTORES')
            call = qf.consulta_tutor(self.dBI, dado)
            if call[0] == 'error':
                msg.error_message_bd(self, call[1])
                return
            self.tabela_resultado.set(2, call)
    

    def busca_tutor(self, i):
        call = qf.consulta_tutor_porId(self.dBI, i)
        if call[0] == 'error':
            msg.error_message_bd(self, call[1])
            return
        return call[0]
    

    def busca_tutor_painel(self, id_):
        call_tutor = qf.consulta_tutor_porId(self.dBI, id_)
        call_pets = qf.consulta_relacao_pets_tutor(self.dBI, id_)
        self._painel_tutor()
        if call_tutor[0] == 'error':
                msg.error_message_bd(self, call_tutor[1])
                return
        self.painel_tutor.set(
            call_tutor[0][0],
            call_tutor[0][1],
            call_tutor[0][2],
            call_tutor[0][3], 
            call_tutor[0][4],
            call_tutor[0][5],
        )
        if call_pets:
            if call_pets[0] == 'error':
                msg.error_message_bd(self, call_pets[1])
                return
            self.painel_tutor.set_tabela(call_pets)
    

    def busca_dados(self, pet_id):
        call_a = qf.consulta_pet_porId(self.dBI, pet_id)
        call_b = qf.consulta_relacao_tutores_pet(self.dBI, pet_id)
        call_Foto = qf.consulta_foto_por_pet(self.dBI, pet_id)
        
        if call_Foto:
            if call_Foto[0] == 'error':
                msg.error_message_bd(self, call_Foto[1])
                return
            id_foto = call_Foto[0][0]
            foto = arqF.blob_to_photo(call_Foto[0][1])
        else:
            id_foto = 0
            foto = None
 
        if call_a[0] == 'error':
            msg.error_message_bd(self, call_a[1])
            return
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

        if call_b:
            if call_b[0] == 'error':
                msg.error_message_bd(self, call_b[1])
                return
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
                self.tutor2.set(0, '-', '-', '-', '...',)
        
        self._seleciona_frame(1)
    

    def salvar_edicao_tutor(self):
        get = self.painel_tutor.get()
        id_ = get['id']
        nome = get['nome'].strip()
        tel1 = get['tel1'].strip()
        tel2 = get['tel2']
        freq = get['freq']
        endereco = get['endereco']
        if not nome or not tel1:
            msg.error_message(self.painel_tutor, title="CAMPOS EM BRANCO", message="Tutor precisa de um nome e ao menos um telefone!")
            return None
        call = qf.atualiza_tutor(self.dBI, id_, nome, tel1, tel2, freq, endereco)
        if call[0] == 'error':
            msg.error_message_bd(self, call[1])
            return
        return call


    def salvar_observacoes(self):
        pet = self.pet.get()
        _call_ = qf.atualiza_observacao(int(pet['id']), pet['observacoes'])
        if _call_[0] == 'error':
            msg.error_message_bd(self, _call_[1])
            return
        call = qf.consulta_pet_porId(self.dBI, int(pet['id']))
        if call[0] == 'error':
            msg.error_message_bd(self, call[1])
            return
        obs = call[0][5]
        self.pet.set_observacoes(obs)
        self._cancelar_observacoes()


    def salvar_edicao(self):
        pet = self.pet.get_novos()
        if not self.tutor1.exists() and not self.tutor2.exists():
            msg.error_message(self, title="SEM TUTOR", message=f"{pet['nome']} precisa de um tutor !!!")
            return
        
        nome = pet['nome'].strip()
        if not nome:
            msg.error_message(self, title="NOME EM BRANCO", message=f"{pet['nome']} precisa de um nome !!!")
            return
        else:
            # ATUALIZA TUTOR
            if self.tutor1.foi_trocado():
                _call_ = qf.remove_relacao(self.dBI, pet['id'], self.tutor1.get_old_id())
                if _call_[0] == 'error':
                    msg.error_message_bd(self, _call_[1])
                    return
                if self.tutor1.exists():
                    _call_ = qf.add_relacao(self.dBI, self.tutor1.get_new_id(), pet['id'])
                    if _call_[0] == 'error':
                        msg.error_message_bd(self, _call_[1])
                        return
                                        
            if self.tutor2.foi_trocado():
                _call_ = qf.remove_relacao(self.dBI, pet['id'], self.tutor2.get_old_id())
                if _call_[0] == 'error':
                    msg.error_message_bd(self, _call_[1])
                    return
                if self.tutor2.exists():
                    _call_ = qf.add_relacao(self.dBI, self.tutor2.get_new_id(), pet['id'])
                    if _call_[0] == 'error':
                        msg.error_message_bd(self, _call_[1])
                        return
                    
            # ATUALIZA PET
            _call_ = qf.atualiza_pet(self.dBI, int(pet['id']), pet['nome'], pet['raca'], pet['porte'], pet['sexo'])
            if _call_[0] == 'error':
                msg.error_message_bd(self, _call_[1])
                return
            
            # FOTO
            if pet['status_foto']:
                dir_ = pet['foto_dir']
                if not qf.consulta_foto_Id(self.dBI, pet['id']):
                    _call_ = qf.adiciona_foto(
                        self.dBI,
                        arqF.photo_to_blob(dir_),
                        pet['id']
                    )
                    if _call_[0] == 'error':
                        msg.error_message_bd(self, _call_[1])
                        return
                else:
                    _call_ = qf.atualiza_foto(
                        self.dBI,
                        arqF.photo_to_blob(dir_),
                        pet['foto_id']
                    )
                    if _call_[0] == 'error':
                        msg.error_message_bd(self, _call_[1])
                        return
            
            self._cancelar_edicao() 
            self.busca_dados(pet['id'])
    

    def salvar_novo_tutor(self):
        get = self.painel_tutor.get()
        nome = get['nome'].strip()
        tel1 = get['tel1'].strip()
        tel2 = get['tel2']
        freq = freq['freq']
        endereco = get['endereco']
        if not nome or not tel1:
            msg.error_message(self.painel_tutor, title="CAMPOS EM BRANCO", message="Tutor precisa de um nome e ao menos um telefone!")
            return None
        
        _call_ = qf.add_tutor(self.dBI, nome, tel1, tel2, freq, endereco)
        if _call_[0] == 'error':
            msg.error_message_bd(self, _call_[1])
            return
        elif _call_:
            msg.done_message(self.painel_tutor, "Tutor Criado!")
            return _call_
        

    def salvar_novo_pet(self):
        pet = self.pet.get_novos()
        if not self.tutor1.exists() and not self.tutor2.exists():
            msg.error_message(self, title="SEM TUTOR", message=f"{pet['nome']} precisa de um tutor !!!")
            return
        
        nome = pet['nome'].strip()
        raca = pet['nome'].strip()
        sexo = pet['nome'].strip()
        porte = pet['nome'].strip()
        if not nome or not raca or not sexo or not porte:
            msg.error_message(self, title="CAMPOS EM BRANCO", message="Preencha todos os campos !")
            return
        
        #ADICAO DO PET, FOTO, E DA RELACAO COM TUTOR
        call_pet = qf.add_pet(self.dBI, pet['nome'], pet['raca'], pet['porte'], pet['sexo'])
        if _call_[0] == 'error':
            msg.error_message_bd(self, _call_[1])
            return

        #PHOTO
        if pet['status_foto']:
            dir_ = pet['foto_dir']
            _call_ = qf.adiciona_foto(
                self.dBI,
                arqF.photo_to_blob(dir_),
                int(_call_[0])
            )
            if _call_[0] == 'error':
                msg.error_message_bd(self, _call_[1])
                return

        #TUTOR
        if self.tutor1.exists():
            tutor_id = self.tutor1.get_new_id()
            _call_ = qf.add_relacao(self.dBI, tutor_id, call_pet[0])
            if _call_[0] == 'error':
                msg.error_message_bd(self, _call_[1])
                return
            
        if self.tutor2.exists():
            tutor_id = self.tutor2.get_new_id()
            _call_ = qf.add_relacao(self.dBI, tutor_id, call_pet[0])
            if _call_[0] == 'error':
                msg.error_message_bd(self, _call_[1])
                return
        msg.done_message(self, message="Pet Criado!")

        #reset frame
        self.pet._cancela_adicao()
        self.tutor1.finaliza_adicao()
        self.tutor2.finaliza_adicao()
        self.BT_cancelar_editar.grid_forget()
        self.BT_editar.configure(text='Editar', command=self._editar)
        self.BT_pesquisar.configure(state='normal')
        self.busca_dados(int(call_pet[0]))


    def excluir_pet(self):
        pet = self.pet.get()
        get = msg.delete_message(self, f"Excluir {pet['nome']}.\nVocê tem certeza?")
        if get.get() == 'Sim':
            _call_ = qf.remove_pet(self.dBI, int(pet['id']))
            if _call_[0] == 'error':
                msg.error_message_bd(self, _call_[1])
                return
            elif _call_ == 1:
                msg.done_message(self, "Pet Excluído!")
            self._cancelar_edicao()
            self._pesquisa_button_event()


    def excluir_tutor(self, id_, nome):
        get = msg.delete_message(self, f"Excluir definitivamente {nome}?")
        
        if get.get() == 'Sim':            
            check = qf.consulta_pets_com_apenas_um_tutor_por_tutor_id(self.dBI, id_)
        else: #não /exit
            return
        
        if check or check != []:
            get = msg.delete_many_pets(self)

            if get.get() == 'Tenho':
                for i in check:
                    _call_ = qf.remove_pet(self.dBI, i[0])  
                    if _call_[0] == 'error':
                        msg.error_message_bd(self, _call_[1])
                        return
            else: #não /exit
                return
                    
        _call_ = qf.remove_tutor(self.dBI, id_)
        if _call_[0] == 'error':
            msg.error_message_bd(self, _call_[1])
            return
        elif _call_ == 1:
            msg.done_message(self, message="Excluído!")
            return 1
    
    
    def excluir_raca(self, raca):
        get = msg.delete_message(self.racas_frame, f"Excluir definitivamente {raca}?")
        if get.get() == 'Sim':
            _call_ = qf.remove_raca(self.dBI, raca)
            if _call_[0] == 'error':
                msg.error_message_bd(self, _call_[1])
                return
            self.set_racas_lista()
            return _call_
    

    def export_data(self, choice, path):
        _call_ = arqF.exporta_dados(self.dBI, choice, path)
        if _call_:
            if _call_[0] == 'error':
                msg.error_message_bd(self, _call_[1])
                return
            msg.done_message(self, message="Exportado!")
            return 1
    

    def import_data(self, choice, path):
        _call_ =arqF.importa_dados(self.dBI, choice, path)
        if _call_:
            if _call_[0] == 'error':
                msg.error_message_bd(self, _call_[1])
                return
            msg.done_message(self, message="Importado!")
            return 1


if __name__ == '__main__':
    dB = db.BD()
    app = main(dB)
    app.mainloop()

