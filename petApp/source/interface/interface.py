import os

import customtkinter as ctk
from PIL import Image

from .frames import BreedsPanel, FileHandler, PetDisplay, SearchTable, TutorDisplay, TutorPanel, TutorSearchPanel


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('petApp')
        self.geometry('1380x720')
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("petApp/resources/theme.json")
        ctk.FontManager.load_font("petApp/resources/Torus Notched Regular.ttf")
        self.protocol("WM_DELETE_WINDOW", self._on_closing)

        self._add_img = ctk.CTkImage(Image.open(os.path.realpath("petApp/images/add_img.png")), size=(28,28))

        #VARS
        self._breeds = []
        self._tutors = [] #For quick search
        self._recent_pets = []
        self._recent_tutors = []
        self._search_data = ctk.StringVar(value='')
        self._search_type = ctk.IntVar(value=1)

        #FRAMES
        self._breed_panel = None
        self._tutors_search = None
        self._tutor_panel = None
        self._file_handler = None
        self._pet_display = PetDisplay(self)
        self._tutorA_display = TutorDisplay(self, 'Tutor 1')   
        self._tutorB_display = TutorDisplay(self, 'Tutor 2')
        self._search_table = SearchTable(self)

        #AREA DE PESQUISA
        self._search_label = ctk.CTkLabel(self, text='Busca:', font=('Torus Notched Regular', 32, 'bold'))
        self._search_entry = ctk.CTkEntry(
            self, textvariable=self._search_data,
            font=('Torus Notched Regular', 22, 'normal'))
        self._search_entry.bind('<Return>', self.search)

        self._bt_radio_pet = ctk.CTkRadioButton(
            self, text='PET', font=('Torus Notched Regular', 28, 'normal'), 
            value=1, variable=self._search_type, command=self._radio_callback
            )
        self._bt_radio_tutor = ctk.CTkRadioButton(
            self, text='TUTOR', font=('Torus Notched Regular', 28, 'normal'), 
            value=2, variable=self._search_type, command=self._radio_callback
            )
        self._table_title_label = ctk.CTkLabel(self, text='', font=('Torus Notched Regular', 36, 'normal'))

        #BUTTONS
        self._bt_back = ctk.CTkButton(
            self, text='Voltar', height=40,
            font=('Torus Notched Regular', 26, 'normal'),
            fg_color='#42A5F5', hover_color='#2196F3',
            border_spacing=8, 
            command=self._pet_display_button_event
        )

        self._bt_search = ctk.CTkButton(
            self, text='Pesquisar', height=40,
            font=('Torus Notched Regular', 24, 'normal'),
            fg_color='#42A5F5', hover_color='#2196F3',
            command=self.search
        )     

        self._bt_search_display = ctk.CTkButton(
            self, text='Pesquisa!',
            font=('Torus Notched Regular', 34, 'normal'),
            fg_color='#42A5F5', hover_color='#2196F3',
            border_spacing=8,
            command=self._search_display_button_event
        )
        
        self._bt_edit = ctk.CTkButton(
            self, text='Editar', width=160,
            font=('Torus Notched Regular', 34, 'normal'),
            border_spacing=8, state='disabled',
            fg_color='#66BB6A', hover_color='#4CAF50',
            command=self._grid_pet_edition,
        )

        self._bt_cancel_edit = ctk.CTkButton(
            self, text='Cancelar', width=160,
            font=('Torus Notched Regular', 34, 'normal'),
            fg_color='#E57373', hover_color='#EF5350',
            border_spacing=8,
        )

        self._bt_breed_panel = ctk.CTkButton(
            self, text='Raças',
            font=('Torus Notched Regular', 28, 'normal'),
            fg_color='#757575', hover_color='#616161',
            border_spacing=4, 
            command=self._call_breed_panel
        )

        self._bt_file_handler = ctk.CTkButton(
            self, text='Arquivo',
            font=('Torus Notched Regular', 28, 'normal'),
            border_spacing=4,
            fg_color='#757575', hover_color='#616161',
            command=self._call_file_handler
        )

        self._bt_add_pet = ctk.CTkButton(
            self, text='Pet',
            font=('Torus Notched Regular', 28, 'normal'),
            border_spacing=4,
            image=self._add_img,
            compound='left',
            fg_color='#66BB6A', hover_color='#4CAF50',
            width=130, height=50,
            command=self._grid_add_new_pet
        )

        self._bt_add_tutor = ctk.CTkButton(
            self, text='Tutor',
            font=('Torus Notched Regular', 28, 'normal'),
            border_spacing=4,
            image=self._add_img,
            compound='left',
            fg_color='#66BB6A', hover_color='#4CAF50',
            width=150, height=50,
            command=self._call_new_tutor_panel
        )

        self._bt_delete_pet = ctk.CTkButton(
            self, text='Excluir Pet',
            font=('Torus Notched Regular', 28, 'normal'),
            border_spacing=4, width=150,
            fg_color='#E57373', hover_color='#E53935',
            command=self.delete_pet    
        )
        
        self._radio_callback()
        # self._section_select(1)

    def search(self, *args):
        raise NotImplementedError("Please Implement this method")

    def set_tutor_list(self):
        raise NotImplementedError("Please Implement this method")   

    def set_breed_list(self):
        raise NotImplementedError("Please Implement this method")
    
    def set_recent_lists(sself):
        raise NotImplementedError("Please Implement this method")

    def update_recent_lists(self):
        raise NotImplementedError("Please Implement this method")
    
    def add_recent(self, wich, tuple_):
        raise NotImplementedError("Please Implement this method")
    
    def add_breed(self, breed):
        raise NotImplementedError("Please Implement this method")

    def edit_breed(self):
        raise NotImplementedError("Please Implement this method")
 
    def save_edit_pet(self):
        raise NotImplementedError("Please Implement this method")

    def save_observations(self):
        raise NotImplementedError("Please Implement this method")
    
    def save_edit_tutor(self):
        raise NotImplementedError("Please Implement this method")
    
    def save_new_pet(self):
        raise NotImplementedError("Please Implement this method")

    def save_new_tutor(self):
        raise NotImplementedError("Please Implement this method")

    def delete_pet(self):
        raise NotImplementedError("Please Implement this method")
    
    def delete_tutor(self):
        raise NotImplementedError("Please Implement this method")

    def delete_breed(self, breed):
        raise NotImplementedError("Please Implement this method")
        
    def show_pet(self, data):
        raise NotImplementedError("Please Implement this method")

    def get_tutor(self):
        raise NotImplementedError("Please Implement this method")
    
    def set_tutor_panel(self):
        raise NotImplementedError("Please Implement this method")

    def export_data(self, choice, path):
        raise NotImplementedError("Please Implement this method")
    
    def import_data(self, choice, path):
        raise NotImplementedError("Please Implement this method")

    def _call_file_handler(self):
        if self._file_handler is None or not self._file_handler.winfo_exists():
            self._file_handler = FileHandler(self)

    def _call_breed_panel(self):
        self.set_breed_list()
        if self._breed_panel is None or not self._breed_panel.winfo_exists():
            self._breed_panel = BreedsPanel(self, racas=self._breeds)

    def _call_tutor_quick_search_panel(self):
        self.set_tutor_list()
        if self._tutors_search is None or not self._tutors_search.winfo_exists():
            self._tutors_search = TutorSearchPanel(self, self._tutors)
        return self._tutors_search.get_choice()
    
    def _call_tutor_panel(self):
        if self._tutor_panel is None or not self._tutor_panel.winfo_exists():
            self._tutor_panel = TutorPanel(self)
        else:
            self._tutor_panel.destroy()
            self._tutor_panel = TutorPanel(self)

    def _call_new_tutor_panel(self):
        self._call_tutor_panel()
        self._tutor_panel.grid_adition()      

    def _radio_callback(self):
        if self._search_type.get() == 1:
            self._table_title_label.configure(text='PETS')
        elif self._search_type.get() == 2:
            self._table_title_label.configure(text='TUTORES')
        self._search_table._change_header(self._search_type.get())
        self._recents()
    
    def _recents(self):
        if self._search_type.get() == 1:
            self._search_table.set(1, self._recent_pets)
        elif self._search_type.get() == 2:
            self._search_table.set(2, self._recent_tutors)
    
    def _grid_pet_edition(self):
        self._bt_delete_pet.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='w')
        self._bt_cancel_edit.grid(row=3, column=1,  sticky='nsw', padx=10, pady=10)
        self._bt_cancel_edit.configure(command=self._grid_cancel_edit)
        self._bt_edit.configure(text='Salvar', command=self.save_edit_pet)
        self._bt_search_display.configure(state='disabled')
        self._pet_display.set_breeds(self._breeds)
        self._pet_display.grid_edition()
        self._tutorA_display.grid_edition()
        self._tutorB_display.grid_edition()

    def _grid_observations_edition(self):
        self._bt_cancel_edit.grid(row=3, column=1,  sticky='nsw', padx=10, pady=10)
        self._bt_cancel_edit.configure(command=self._grid_cancel_edit_obs)
        self._bt_edit.configure(text='Salvar', command=self.save_observations)
        self._pet_display._obs_display.configure(state='normal', fg_color='gray93')
        self._bt_search_display.configure(state='disabled')
    
    def _grid_add_new_pet(self):
        self._pet_display.reset()
        self._tutorA_display.reset()
        self._tutorB_display.reset()
        self._pet_display.grid_adition()
        self._pet_display.set_breeds(self._breeds)
        self._tutorA_display.grid_edition()
        self._tutorB_display.grid_edition()
        self._bt_cancel_edit.grid(row=3, column=1,  sticky='nsw', padx=10, pady=10)
        self._bt_cancel_edit.configure(command=self._grid_cancel_adition)
        self._bt_edit.configure(text='Salvar', state='normal', command=self.save_new_pet)
        self._bt_search_display.configure(state='disabled')
        self._section_select(1)

    def _grid_cancel_edit(self):
        self._bt_delete_pet.grid_forget()
        self._bt_cancel_edit.grid_forget()
        self._bt_edit.configure(text='Editar', command=self._grid_pet_edition)
        self._bt_search_display.configure(state='normal')
        self._pet_display.grid_cancel_edition()
        self._tutorA_display.grid_cancel_edition()
        self._tutorB_display.grid_cancel_edition()

    def _grid_cancel_edit_obs(self):
        self._bt_cancel_edit.grid_forget()
        self._bt_edit.configure(text='Editar', command=self._grid_pet_edition)
        self._pet_display.reset_observations()
        self._pet_display._obs_display.configure(state='disable', fg_color='transparent')
        self._bt_search_display.configure(state='normal')
    
    def _grid_cancel_adition(self):
        self._pet_display.reset()
        self._tutorA_display.reset()
        self._tutorB_display.reset()
        self._pet_display.grid_cancel_adition()
        self._tutorA_display.grid_cancel_edition()
        self._tutorB_display.grid_cancel_edition()
        self._bt_cancel_edit.grid_forget()
        self._bt_edit.configure(text='Editar', command=self._grid_pet_edition)
        self._bt_search_display.configure(state='normal')
        self._bt_back.configure(state='disabled')
        self._section_select(2)

    def _section_select(self, frame):
        if frame == 1:
            self.grid_columnconfigure(0, weight=2)
            self.grid_columnconfigure(1, weight=1)
            self.grid_rowconfigure((0,3), weight=0)
            self.grid_rowconfigure((1,2), weight=1)
            self._bt_breed_panel.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='e')
            self._bt_file_handler.grid(row=0, column=1, padx=10, pady=(10, 0), sticky='e')
            self._pet_display.grid(row=1, column=0, padx=10, pady=(5, 0), rowspan=2, sticky='ewsn')
            self._tutorA_display.grid(row=1, column=1, padx=10, pady=(5, 0), sticky='ewsn')
            self._tutorB_display.grid(row=2, column=1, padx=10, pady=(10, 0), sticky='ewsn')
            self._bt_search_display.grid(row=3, column=0, sticky='nsew', padx=10, pady=5)
            self._bt_edit.grid(row=3, column=1,  sticky='nse', padx=10, pady=5)
            if self._pet_display._id.get():
                self._bt_edit.configure(state='normal')
                self._pet_display._bt_edit_obs.configure(state='normal')
        else:
            self._bt_breed_panel.grid_forget()
            self._bt_file_handler.grid_forget()
            self._pet_display.grid_forget()
            self._tutorA_display.grid_forget()
            self._tutorB_display.grid_forget()
            self._bt_search_display.grid_forget()
            self._bt_edit.grid_forget()

        if frame == 2:
            self.grid_columnconfigure(0, weight=0)
            self.grid_columnconfigure(1, weight=1)
            self.grid_rowconfigure(1, weight=0)
            self.grid_rowconfigure(2, weight=1)
            self._search_label.grid(row=0, column=0, padx=(30, 10), pady=(20, 10))
            self._search_entry.grid(row=0, column=1, sticky='new', padx=30, pady=(30, 10))
            self._bt_radio_pet.grid(row=1, column=0, sticky='n', padx=(30, 10), pady=10)
            self._bt_radio_tutor.grid(row=1, column=1, sticky='nw', padx=(0, 10), pady=10)
            self._search_table.grid(row=2, column=0, columnspan=2, sticky='news', padx=10, pady=(0, 10))
            self._bt_back.configure(state='normal')
            self._bt_back.grid(row=3, column=0, padx=(30, 10), pady=(30, 10))
            self._bt_search.grid(row=1, column=1, sticky='ne', padx=30)
            self._bt_add_pet.grid(row=3, column=1, padx=(30, 240), pady=(30, 20), sticky='e')
            self._bt_add_tutor.grid(row=3, column=1, padx=(30, 40), pady=(30, 20), sticky='e')
            self._table_title_label.grid(row=1, column=1, sticky='s', padx=(0, 230), pady=(60, 0))
        else:
            self._search_table.grid_forget()
            self._search_entry.grid_forget()
            self._search_label.grid_forget()
            self._bt_radio_pet.grid_forget()
            self._bt_radio_tutor.grid_forget()
            self._bt_back.grid_forget()
            self._bt_search.grid_forget()
            self._table_title_label.grid_forget()
            self._bt_add_pet.grid_forget()
            self._bt_add_tutor.grid_forget()

        if frame == 3:
            ...
        else:
            ...
        
    def _pet_display_button_event(self):
        self._section_select(1)

    def _search_display_button_event(self):
        if self._search_data.get().strip():
            self.search()
        # self._bt_back.configure(state='normal')
        self._section_select(2)
    
    def _on_closing(self):
        self.update_recent_lists()
        self.grab_release()
        self.destroy()


if __name__ == '__main__':  
    app = App()
    app.mainloop()  
