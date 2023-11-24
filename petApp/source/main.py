from .backend import statements_functions as sf
from .backend import file_handler_functions as fhf
from .interface import App
from .interface.frames import messages as msg


class Main(App):
    def __init__(self, dBinterface):
        #DB Inicialization
        self.dBI = dBinterface
        super().__init__()
        self.set_breed_list()
        self.set_recent_lists()
        self._recents()
        self._section_select(2)      


    def set_tutor_list(self):
        self._tutors.clear()
        for r in sf.query_many_tutors(self.dBI):
            self._tutors.append(list(r))
    

    def set_breed_list(self):
        self._breeds.clear()
        for r in sf.query_breeds(self.dBI):
            self._breeds.append(r[0]) 
        self._pet_display.set_breeds(self._breeds)
    

    def set_recent_lists(self):
        for pet in sf.query_recent_pet(self.dBI):
            self._recent_pets.append(list(pet))
        for tutor in sf.query_recent_tutor(self.dBI):
            self._recent_tutors.append(list(tutor))
    

    def update_recent_lists(self):
        sf.remove_recent_pet(self.dBI)
        sf.remove_recent_tutor(self.dBI)
      
        ids_p = []
        for pet in self._recent_pets:
            ids_p.append(pet[0])
        sf.insert_recent_pet(self.dBI, ids_p)
        ids_t = []
        for tutor in self._recent_tutors:
            ids_t.append(tutor[0])
        sf.insert_recent_tutor(self.dBI, ids_t)
    

    def refresh_recent(self, wich:int, tuple_, delete:bool):
        if wich == 1:
            for index, pet in enumerate(self._recent_pets):
                if int(tuple_[0]) == int(pet[0]):
                    self._recent_pets.pop(index)
                    if delete:
                        return
                    break
            pet = list(tuple_)
            if len(pet) > 5:
                pet.pop(-1) # REMOVES OBS            
            self._recent_pets.insert(0, pet)
            if len(self._recent_pets) > 10:
                self._recent_pets.pop(-1)

        elif wich == 2:
            for index, tutor in enumerate(self._recent_tutors):
                if int(tuple_[0]) == int(tutor[0]):
                    self._recent_tutors.pop(index)
                    if delete:
                        return
                    break
            tutor = list(tuple_)
            if len(tutor) > 5:
                tutor.pop(-1) # REMOVES ADDRESS
            self._recent_tutors.insert(0, tutor)
            if len(self._recent_tutors) > 10:
                self._recent_tutors.pop(-1)
    

    def add_breed(self, breed):
        call = sf.add_breed(self.dBI, breed.strip())
        if call[0] == breed.title():
            self.set_breed_list()
            self._breed_panel.update_list()            
        elif call[0] == 'error':
            msg.error_message_bd(self._breed_panel, call[1])
    

    def edit_breed(self, breed, raca_nova):
        call = sf.update_breed(self.dBI, breed, raca_nova.strip())
        if call[0] == raca_nova.title():
            self.set_breed_list()
            self._breed_panel.update_list()            
        elif call[0] == 'error':
            msg.error_message_bd(self._breed_panel, call[1])
            

    def search(self, *args):
        dado = self._search_data.get()
        if self._search_type.get() == 1:
            self._table_title_label.configure(text='PETS')
            call = sf.pet_query(self.dBI, dado)
            try:
                if call[0] == 'error':
                    msg.error_message_bd(self, call[1])
                    return
            except IndexError:
                pass
            self._search_table.set(1, call)
        elif self._search_type.get() == 2:
            self._table_title_label.configure(text='TUTORES')
            call = sf.query_tutor(self.dBI, dado)
            try:
                if call[0] == 'error':
                    msg.error_message_bd(self, call[1])
                    return
            except IndexError:
                pass
            self._search_table.set(2, call)
    

    def get_tutor(self, i):
        call = sf.query_tutor_by_id(self.dBI, i)
        if call[0] == 'error':
            msg.error_message_bd(self, call[1])
            return
        return call[0]
    

    def set_tutor_panel(self, id_):
        call_tutor = sf.query_tutor_by_id(self.dBI, id_)
        call_pets = sf.query_pet_tutor_relation(self.dBI, id_)
        
        self._call_tutor_panel()
        if call_tutor:
            if call_tutor[0] == 'error':
                msg.error_message_bd(self, call_tutor[1])
                return
            self._tutor_panel.set(
            call_tutor[0][0],
            call_tutor[0][1],
            call_tutor[0][2],
            call_tutor[0][3], 
            call_tutor[0][4],
            call_tutor[0][5],
        )
        else:
            msg.error_message(self, 'Não encontrado', 'Tutor não encontrado')
            self._tutor_panel.destroy()
            return
        
        
        if call_pets:
            if call_pets[0] == 'error':
                msg.error_message_bd(self, call_pets[1])
                return
            self._tutor_panel.set_table(call_pets)
        self.refresh_recent(2, call_tutor[0], False)
    

    def show_pet(self, pet_id):
        call_pet = sf.pet_query_by_id(self.dBI, pet_id)
        call_tutor = sf.query_tutor_pet_relation(self.dBI, pet_id)
        call_photo = sf.query_photo_by_pet_id(self.dBI, pet_id)
        
        if call_photo:
            if call_photo[0] == 'error':
                msg.error_message_bd(self, call_photo[1])
                return
            photo_id = call_photo[0][0]
            foto = fhf.blob_to_photo(call_photo[0][1])
        else:
            photo_id = 0
            foto = None
        if call_pet:
            if call_pet[0] == 'error':
                msg.error_message_bd(self, call_pet[1])
                return
            self._pet_display.set(
                call_pet[0][0],
                call_pet[0][1],
                call_pet[0][2],
                call_pet[0][3],
                call_pet[0][4],
                call_pet[0][5],
                photo_id,
                foto
                )
        else:
            msg.error_message(self, 'Não encontrado', 'Pet não encontrado')
            return

        if call_tutor:
            if call_tutor[0] == 'error':
                msg.error_message_bd(self, call_tutor[1])
                return
            self._tutorA_display.set(
            call_tutor[0][0],
            call_tutor[0][1],
            call_tutor[0][2],
            call_tutor[0][3],
            call_tutor[0][4],
        )   
            if len(call_tutor) == 2:    
                self._tutorB_display.set(
                    call_tutor[1][0],
                    call_tutor[1][1],
                    call_tutor[1][2],
                    call_tutor[1][3],
                    call_tutor[1][4],
                )
            else:
                self._tutorB_display.set(0, '-', '-', '-', '...',)
        else:
            self._tutorA_display.set(0, '-', '-', '-', '...',)
            self._tutorB_display.set(0, '-', '-', '-', '...',)

        self._section_select(1)
        self.refresh_recent(1, call_pet[0], False)

    def save_edit_tutor(self):
        get = self._tutor_panel.get()
        id_ = get['id']
        name = get['name'].strip()
        tel1 = get['tel1'].strip()
        tel2 = get['tel2']
        freq = get['freq']
        address = get['address']
        if not name or not tel1:
            msg.error_message(self._tutor_panel, title="CAMPOS EM BRANCO", message="Tutor precisa de um nome e ao menos um telefone!")
            return None
        call = sf.update_tutor(self.dBI, id_, name, tel1, tel2, freq, address)
        if call[0] == 'error':
            msg.error_message_bd(self, call[1])
            return
        return call


    def save_observations(self):
        pet = self._pet_display.get()
        _call_ = sf.update_observation(self.dBI, int(pet['id']), pet['observations'])
        if _call_[0] == 'error':
            msg.error_message_bd(self, _call_[1])
            return
        call = sf.pet_query_by_id(self.dBI, int(pet['id']))
        if call[0] == 'error':
            msg.error_message_bd(self, call[1])
            return
        obs = call[0][5]
        self._pet_display.set_observations(obs)
        self._grid_cancel_edit_obs()


    def save_edit_pet(self):
        pet = self._pet_display.get_new_ones()
        if not self._tutorA_display.exists() and not self._tutorB_display.exists():
            msg.error_message(self, title="SEM TUTOR", message=f"{pet['name']} precisa de um tutor !!!")
            return
        
        name = pet['name'].strip()
        if not name:
            msg.error_message(self, title="NOME EM BRANCO", message=f"{pet['name']} precisa de um nome !!!")
            return
        else:
            # ATUALIZA TUTOR
            if self._tutorA_display.foi_trocado():
                _call_ = sf.remove_relation(self.dBI, pet['id'], self._tutorA_display.get_old_id())
                if _call_[0] == 'error':
                    msg.error_message_bd(self, _call_[1])
                    return
                if self._tutorA_display.exists():
                    _call_ = sf.add_relation(self.dBI, self._tutorA_display.get_new_id(), pet['id'])
                    if _call_[0] == 'error':
                        msg.error_message_bd(self, _call_[1])
                        return
                                        
            if self._tutorB_display.foi_trocado():
                _call_ = sf.remove_relation(self.dBI, pet['id'], self._tutorB_display.get_old_id())
                if _call_[0] == 'error':
                    msg.error_message_bd(self, _call_[1])
                    return
                if self._tutorB_display.exists():
                    _call_ = sf.add_relation(self.dBI, self._tutorB_display.get_new_id(), pet['id'])
                    if _call_[0] == 'error':
                        msg.error_message_bd(self, _call_[1])
                        return
                    
            # ATUALIZA PET
            _call_ = sf.pet_update(self.dBI, int(pet['id']), pet['name'], pet['breed'], pet['size'], pet['sex'])
            if _call_[0] == 'error':
                msg.error_message_bd(self, _call_[1])
                return
            
            # FOTO
            if pet['status_foto']:
                dir_ = pet['photo_dir']
                if not sf.quey_photo_by_id(self.dBI, pet['id']):
                    _call_ = sf.add_photo(
                        self.dBI,
                        fhf.photo_to_blob(dir_),
                        pet['id']
                    )
                    if _call_[0] == 'error':
                        msg.error_message_bd(self, _call_[1])
                        return
                else:
                    _call_ = sf.photo_update(
                        self.dBI,
                        fhf.photo_to_blob(dir_),
                        pet['photo_id']
                    )
                    if _call_[0] == 'error':
                        msg.error_message_bd(self, _call_[1])
                        return
            
            self._grid_cancel_edit() 
            self.show_pet(pet['id'])
    

    def save_new_tutor(self):
        get = self._tutor_panel.get()
        name = get['name'].strip()
        tel1 = get['tel1'].strip()
        tel2 = get['tel2']
        freq = get['freq']
        address = get['address']
        if not name or not tel1:
            msg.error_message(self._tutor_panel, title="CAMPOS EM BRANCO", message="Tutor precisa de um nome e ao menos um telefone!")
            return None
        
        call_tutor = sf.add_tutor(self.dBI, name, tel1, tel2, freq, address)
        if call_tutor[0] == 'error':
            msg.error_message_bd(self, call_tutor[1])
            return
        else:
            msg.done_message(self._tutor_panel, "Tutor Criado!")
            self.refresh_recent(2, call_tutor, False)
            return call_tutor
        

    def save_new_pet(self):
        pet = self._pet_display.get_new_ones()
        if not self._tutorA_display.exists() and not self._tutorB_display.exists():
            msg.error_message(self, title="SEM TUTOR", message=f"{pet['name']} precisa de um tutor !!!")
            return
        
        name = pet['name'].strip()
        breed = pet['breed']
        sex = pet['sex']
        size = pet['size']
        if not name or not breed or not sex or not size:
            msg.error_message(self, title="CAMPOS EM BRANCO", message="Preencha todos os campos !")
            return
        
        # ADICAO DO PET, FOTO, E DA RELACAO COM TUTOR
        call_pet = sf.add_pet(self.dBI, pet['name'], pet['breed'], pet['size'], pet['sex'])
        if call_pet[0] == 'error':
            msg.error_message_bd(self, _call_[1])
            return

        # PHOTO
        if pet['status_foto']:
            dir_ = pet['photo_dir']
            _call_ = sf.add_photo(
                self.dBI,
                fhf.photo_to_blob(dir_),
                int(call_pet[0])
            )
            if _call_[0] == 'error':
                msg.error_message_bd(self, _call_[1])
                return

        # TUTOR
        if self._tutorA_display.exists():
            tutor_id = self._tutorA_display.get_new_id()
            _call_ = sf.add_relation(self.dBI, tutor_id, call_pet[0])
            if _call_[0] == 'error':
                msg.error_message_bd(self, _call_[1])
                return
        if self._tutorB_display.exists():
            tutor_id = self._tutorB_display.get_new_id()
            _call_ = sf.add_relation(self.dBI, tutor_id, call_pet[0])
            if _call_[0] == 'error':
                msg.error_message_bd(self, _call_[1])
                return
            
        msg.done_message(self, message="Pet Criado!")
        self.refresh_recent(1, call_pet, False)

        # reset frame
        self._pet_display.grid_cancel_adition()
        self._tutorA_display.grid_adition_complete()
        self._tutorB_display.grid_adition_complete()
        self._bt_cancel_edit.grid_forget()
        self._bt_edit.configure(text='Editar', command=self._grid_pet_edition)
        self._bt_search_display.configure(state='normal')
        self.show_pet(int(call_pet[0]))


    def delete_pet(self):
        pet = self._pet_display.get()
        get = msg.delete_message(self, f"Excluir {pet['name']}.\nVocê tem certeza?")
        if get.get() == 'Sim':
            _call_ = sf.remove_pet(self.dBI, int(pet['id']))
            if _call_[0] == 'error':
                msg.error_message_bd(self, _call_[1])
                return
            elif _call_[0] == 1:
                msg.done_message(self, "Pet Excluído!")
                pet = (pet['id'], pet['name'], pet['breed'], pet['sex'], pet['size'])
                self.refresh_recent(1, pet, True)
            self._grid_cancel_edit()
            self._search_display_button_event()


    def delete_tutor(self, tutor):
        get = msg.delete_message(self, f"Excluir definitivamente {tutor['name']}?")
        
        if get.get() == 'Sim':            
            check = sf.query_pets_with_only_one_tutor(self.dBI, tutor['id'])
        else: #não /exit
            return
        
        if check or check != []:
            get = msg.delete_many_pets(self)

            if get.get() == 'Tenho':
                for i in check:
                    _call_ = sf.remove_pet(self.dBI, i[0])  
                    if _call_[0] == 'error':
                        msg.error_message_bd(self, _call_[1])
                        return
            else: #não /exit
                return
                    
        _call_ = sf.remove_tutor(self.dBI, tutor['id'])
        if _call_[0] == 'error':
            msg.error_message_bd(self, _call_[1])
            return
        elif _call_[0] == 1:
            msg.done_message(self, message="Excluído!")
            tutor = (tutor['id'], tutor['name'], tutor['tel1'], tutor['tel2'], tutor['freq'])
            self.refresh_recent(2, tutor, True)
            self._search_display_button_event()
            return 1


    def delete_breed(self, breed):
        get = msg.delete_message(self._breed_panel, f"Excluir definitivamente {breed}?")
        if get.get() == 'Sim':
            _call_ = sf.remove_breed(self.dBI, breed)
            if _call_[0] == 'error':
                msg.error_message_bd(self, _call_[1])
                return
            self.set_breed_list()
            return _call_


    def export_data(self, choice, path):
        _call_ = fhf.export_data(self.dBI, choice, path)
        if _call_:
            if _call_[0] == 'error':
                msg.error_message_bd(self, _call_[1])
                return
            msg.done_message(self, message="Exportado!")
            return 1


    def import_data(self, choice, path):
        _call_ =fhf.import_data(self.dBI, choice, path)
        if _call_:
            if _call_[0] == 'error':
                msg.error_message_bd(self, _call_[1])
                return
            elif _call_[0] == 'errorS':
                msg.error_message(self, 'Erro ao importar!',_call_[1])
                return
            msg.done_message(self, message="Importado!")
            return 1


