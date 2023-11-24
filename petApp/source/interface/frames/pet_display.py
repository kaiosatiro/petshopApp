import os
from importlib import resources

from PIL import Image
import customtkinter as ctk

from .photo_handler import PhotoHandler


class PetDisplay(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(9, weight=1)

        self._breeds = []
        self._sizes = ['Pequeno', 'Médio', 'Grande']
        self._sexs = ['Macho', 'Fêmea']
        
        #VARIAVEIS DOS VALORES MOSTRADOS
        self._id = ctk.IntVar(value=None)
        self._name_pet = ctk.StringVar()
        self._breed = ctk.StringVar()
        self._size = ctk.StringVar()  
        self._sex = ctk.StringVar()
        self._obs = ctk.StringVar()
        
        #VARIAVEIS DOS VALORES QUE RECEBEM A EDICAO
        self._name_bkp = ctk.StringVar()
        self._breed_bkp = ctk.StringVar()
        self._size_bkp = ctk.StringVar()
        self._sex_bkp = ctk.StringVar()

        #WIDGETS DOS VALORES DO PET
        #________ IMAGEM _________
        self._photo_display = PhotoHandler(self)
        self._photo_display.grid(row=0, column=0, rowspan=8, sticky='nsew', padx=10, pady=(10, 0))
        
        #__________ NOME _________
        self._name_display = ctk.CTkLabel(
            self, textvariable=self._name_pet,
            font=('Torus Notched Regular', 28, 'normal'),
            fg_color='gray83', corner_radius=8
        )
        self._name_display.grid(row=1, column=1, padx=10, pady=10, sticky='ew', columnspan=3)

        self._label_name = ctk.CTkLabel(self, text='Nome:', font=('Torus Notched Regular', 24, 'bold')).grid(row=0, column=1, pady=(10, 0))
        
        self._name_edition = ctk.CTkEntry(
            self, textvariable=self._name_bkp,
            font=('Torus Notched Regular', 28, 'normal'), justify='left'
        )

        #__________ RACA _________
        self._breed_display = ctk.CTkLabel(
            self, textvariable=self._breed,
            font=('Torus Notched Regular', 28, 'normal'),
            fg_color='gray83', corner_radius=8
            )
        self._breed_display.grid(row=3, column=1, padx=10, pady=10, sticky='ew', columnspan=3)

        self._label_breed = ctk.CTkLabel(self, text='Raça:', font=('Torus Notched Regular', 24, 'bold')).grid(row=2, column=1)
        
        self._breed_options_box = ctk.CTkOptionMenu( 
            self, variable=self._breed_bkp,
            state='normal', values=self._breeds,
            font=('Torus Notched Regular', 28, 'normal'), 
            dropdown_fg_color="#BBDEFB", dropdown_hover_color="#90CAF9",
            dropdown_font=('', 26, 'normal'),
        )

        # _________ SEXO __________
        self._sex_display = ctk.CTkLabel(
            self, textvariable=self._sex, 
            font=('Torus Notched Regular', 28, 'normal'),
            fg_color='gray83', corner_radius=8
            )
        self._sex_display.grid(row=5, column=1, padx=10, pady=10, sticky='ew')

        self._label_sex = ctk.CTkLabel(self, text='Sexo:', font=('Torus Notched Regular', 24, 'bold')).grid(row=4, column=1)

        self._sex_edition = ctk.CTkOptionMenu(
            self, variable=self._sex_bkp,
            state='normal', values=self._sexs,
            font=('Torus Notched Regular', 28, 'normal'),
            dropdown_fg_color="#BBDEFB", dropdown_hover_color="#90CAF9",
            dropdown_font=('', 26, 'normal'),
        )

        # _________ PORTE __________        

        self._size_display = ctk.CTkLabel(
            self, textvariable=self._size, 
            font=('Torus Notched Regular', 28, 'normal'),
            fg_color='gray83', corner_radius=8
            )
        self._size_display.grid(row=7, column=1, padx=10, pady=10, sticky='ew')

        self._label_size = ctk.CTkLabel(self, text='Porte:', font=('Torus Notched Regular', 24, 'bold')).grid(row=6, column=1)
        
        self._size_edition = ctk.CTkOptionMenu(
            self, variable=self._size_bkp,
            state='normal', values=self._sizes,
            font=('Torus Notched Regular', 28, 'normal'),
            dropdown_font=('', 26, 'normal'),
            dropdown_fg_color="#BBDEFB", dropdown_hover_color="#90CAF9",
        )

        # _________ OBSERVACOES __________        
        self._label_obs = ctk.CTkLabel(self, text='Observações', font=('Torus Notched Regular', 28, 'bold'))
        self._label_obs.grid(row=8, column=0, sticky='w', padx=10, pady=(0, 5)) #pack(expand=True, fill="both") ??????
        self._obs_display = ctk.CTkTextbox(
            self, corner_radius=8, font=('Torus Notched Regular', 22, 'normal'),
            fg_color='transparent'
            )
        self._obs_display.grid(row=9, column=0, columnspan=5, sticky='nsew', padx=10, pady=(0, 10))
        self._obs_display.insert("0.0", '...')
        self._obs_display.configure(state='disabled')
        
        self._bt_img = ctk.CTkImage(Image.open(os.path.relpath("petApp/images/bt_img.png")), size=(28,28))

        self._bt_edit_obs = ctk.CTkButton(
            self, text='', width=28, image=self._bt_img,
            command=master._grid_observations_edition,
            fg_color='#66BB6A', hover_color='#4CAF50',
            state='disabled'
        )
        self._bt_edit_obs.grid(row=8, column=0, sticky='w', padx=200, pady=5)
    

    def reset(self):
        self._id.set(0)
        self._name_pet.set('')
        self._breed.set('')
        self._size.set('')
        self._sex.set('')
        self._obs.set('')
        self.reset_observations()


    def set_breeds(self, breeds:list):
        self._breeds = breeds
        self._breed_options_box.configure(values=breeds)
    

    def get(self):
        return {
            'id': self._id.get(),
            'name': self._name_pet.get(),
            'breed': self._breed.get(),
            'sex': self._sex.get(),
            'size': self._size.get(),
            'observations': self.get_observations(),
            'photo_id': self._photo_display.get_id()
        }
    
    def get_new_ones(self):
        return {
            'id': self._id.get(),
            #_____NOVOS______
            'name': self._name_bkp.get(),
            'breed': self._breed_bkp.get(),
            'sex': self._sex_bkp.get(),
            'size': self._size_bkp.get(),
            'status_foto': self._photo_display.new_photo(),
            'photo_dir': self._photo_display.get_dir(),
            #_________________
            'photo_id': self._photo_display.get_id()
        }
    

    def set(self, id:int, name:str, breed:str, size:str, sex:str, observations:str=None, photo_id:int=0, photo=None):
        self._id.set(id)
        self._name_pet.set(name)
        self._breed.set(breed)
        self._size.set(size)
        self._sex.set(sex)
        if observations:
            self.set_observations(observations)
        else:
            self.set_observations('...')
        self._photo_display.set_all(photo_id, photo)


    def get_observations(self):
        return self._obs_display.get('0.0', 'end')
    

    def set_observations(self, txt):
        self._obs.set(txt)
        self._obs_display.configure(state='normal')
        self._obs_display.delete("0.0", "end")
        self._obs_display.insert("0.0", txt)
        self._obs_display.configure(state='disable')


    def reset_observations(self):
        self._obs_display.delete('0.0', 'end')
        self._obs_display.insert("0.0", self._obs.get())
    

    def grid_edition(self):
        self._name_bkp.set(self._name_pet.get())
        self._breed_bkp.set(self._breed.get())
        self._size_bkp.set(self._size.get())
        self._sex_bkp.set(self._sex.get())
        
        self._name_display.grid_forget()
        self._breed_display.grid_forget()
        self._sex_display.grid_forget()
        self._size_display.grid_forget()

        self._name_edition.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
        self._breed_options_box.grid(row=3, column=1, padx=10, pady=10, sticky='ew')
        self._sex_edition.grid(row=5, column=1, padx=10, pady=10, sticky='ew')
        self._size_edition.grid(row=7, column=1, padx=10, pady=10, sticky='ew')
        self._photo_display.grid_edition()

        self._bt_edit_obs.configure(state='disabled')
    

    def grid_adition(self):
        self._name_bkp.set('')
        self._breed_bkp.set('')
        self._size_bkp.set('')
        self._sex_bkp.set('')

        self._name_display.grid_forget()
        self._breed_display.grid_forget()
        self._sex_display.grid_forget()
        self._size_display.grid_forget()

        self._name_edition.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
        self._breed_options_box.grid(row=3, column=1, padx=10, pady=10, sticky='ew')
        self._sex_edition.grid(row=5, column=1, padx=10, pady=10, sticky='ew')
        self._size_edition.grid(row=7, column=1, padx=10, pady=10, sticky='ew')
        self._photo_display.grid_adition()

        self._bt_edit_obs.configure(state='disabled')

    
    def grid_cancel_edition(self):
        self._name_edition.grid_forget()
        self._breed_options_box.grid_forget()
        self._sex_edition.grid_forget()
        self._size_edition.grid_forget()

        self._name_display.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
        self._breed_display.grid(row=3, column=1, padx=10, pady=10, sticky='ew')
        self._sex_display.grid(row=5, column=1, padx=10, pady=10, sticky='ew')
        self._size_display.grid(row=7, column=1, padx=10, pady=10, sticky='ew')
        self._photo_display.grid_cancel_edition()

        self._bt_edit_obs.configure(state='normal')
    

    def grid_cancel_adition(self):
        self._name_edition.grid_forget()
        self._breed_options_box.grid_forget()
        self._sex_edition.grid_forget()
        self._size_edition.grid_forget()

        self._name_display.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
        self._breed_display.grid(row=3, column=1, padx=10, pady=10, sticky='ew')
        self._sex_display.grid(row=5, column=1, padx=10, pady=10, sticky='ew')
        self._size_display.grid(row=7, column=1, padx=10, pady=10, sticky='ew')
        self._photo_display.grid_cancel_adition()

        self._bt_edit_obs.configure(state='normal')
        