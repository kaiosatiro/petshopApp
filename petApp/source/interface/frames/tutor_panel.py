import customtkinter as ctk
from CTkTable import *


class TutorPanel(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Tutor Painel")
        self.geometry("700x600+500+200")
        self.maxsize(700, 600)
        self.minsize(700, 600)

        self.protocol("WM_DELETE_WINDOW", self._on_closing)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self._attendance = ['Diário', 'Semanal', 'Quinzenal', 'Mensal', 'Esporático']

        self._frameT = ctk.CTkFrame(self)
        self._frameL = ctk.CTkScrollableFrame(self)

        self._frameT.grid(row=0, padx=10, pady=(40,0), sticky='nsew')
        self._frameT.grid_columnconfigure((1,3), weight=1)
        self._frameL.grid(row=1, column=0, padx=10, pady=(45,0), sticky='nsew')
        # self._frameL.grid_columnconfigure((1,3), weight=1)
        
        self._id = ctk.IntVar(value=0)
        self._name_tutor = ctk.StringVar(value='')
        self._tel1 = ctk.StringVar(value='')
        self._tel2 = ctk.StringVar(value='')
        self._freq = ctk.StringVar(value='')
        self._address = ctk.StringVar(value='')

        self._id_bkp = 0
        self._name_bkp = ''
        self._tel1_bkp = ''
        self._tel2_bkp = ''
        self._freq_bkp = ''
        self._address_bkp = ''

        # ____________ NOME ______________
        self._label_name = ctk.CTkLabel(
            self._frameT, text='Nome:', font=('Torus Notched Regular', 22, 'bold'),          
        ).grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self._name_display = ctk.CTkEntry(
            self._frameT, textvariable=self._name_tutor,
            state='readonly',
            font=('Torus Notched Regular', 22, 'normal')
        )
        self._name_display.grid(row=1, column=1, columnspan=3, pady=5, sticky='we')

        #____________ TELEFONES ________________
        self._label_tel1 = ctk.CTkLabel(self._frameT, text='Tel1:', font=('Torus Notched Regular', 22, 'bold')).grid(
            row=2, column=0, sticky='w', padx=10, pady=5
        )
        self._tel1_display = ctk.CTkEntry(
            self._frameT, textvariable=self._tel1,
             state='readonly',
            font=('Torus Notched Regular', 22, 'normal')
        )
        self._tel1_display.grid(row=2, column=1, sticky='we')
        
        self._label_tel2 = ctk.CTkLabel(self._frameT, text='Tel2:', font=('Torus Notched Regular', 22, 'bold')).grid(
            row=2, column=2, sticky='w', padx=10, pady=5
        )
        self._tel2_display = ctk.CTkEntry(
            self._frameT, textvariable=self._tel2,
             state='readonly',
            font=('Torus Notched Regular', 22, 'normal'),
        )
        self._tel2_display.grid(row=2, column=3, sticky='we')

        #___________ FREQ __________
        self._label_freq = ctk.CTkLabel(self._frameT, text='Freq:', font=('Torus Notched Regular', 22, 'bold')).grid(
            row=3, column=2, sticky='w', padx=10, pady=5
        )
        self._freq_display = ctk.CTkOptionMenu( 
            self._frameT, variable=self._freq,
            state='disabled', values=self._attendance,
            font=('Torus Notched Regular', 22, 'normal'), 
            dropdown_fg_color="#BBDEFB", dropdown_hover_color="#90CAF9",
            dropdown_font=('', 22, 'normal'),
        )
        self._freq_display.grid(row=3, column=3, padx=10, sticky='we')
        
        #____________ ENDERECO ______________
        self._label_endereco = ctk.CTkLabel(self._frameT, text='Endereço:', font=('Torus Notched Regular', 22, 'bold')).grid(
            row=3, column=0, padx=10, pady=5, sticky='w', columnspan=2
        )
        self._address_display = ctk.CTkEntry(
            self._frameT, corner_radius=6, font=('Torus Notched Regular', 22, 'normal'),
            textvariable=self._address,
            state='readonly',
            
            )
        self._address_display.grid(row=4, column=0, padx=10, pady=(0, 10), columnspan=4, sticky='nsew')
        #_____________ PETS __________________
        self._label_pets = ctk.CTkLabel(
            self, text='Pets', font=('Torus Notched Regular', 28, 'bold'),
            bg_color='transparent'
            ).grid(row=1, column=0, pady=(10,0), sticky='n')
        
        self._head_table = [['#', 'Nome', 'Raça']]
        self._table = CTkTable(
            self._frameL, column=3, values=self._head_table,
            hover=True, hover_color='grey', header_color='grey',
            font=('Torus Notched Regular', 18, 'normal'),
            command=self._call_goto_pet
        )
        self._table.pack(expand=True, fill="both", padx=10, pady=10)
        self._table.edit_column(0, width=1)
        self._table.edit_column(1, width=300)

        #_____________ BOTES _____________

        self._bt_remove = ctk.CTkButton(
            self, text='Excluir', width=100,
            font=('Torus Notched Regular', 20, 'normal'),
            fg_color='#E57373', hover_color='#E53935',
            command=self._call_delete_tutor
        )

        self._bt_edit = ctk.CTkButton(
            self, text='Editar',
            font=('Torus Notched Regular', 22, 'normal'),
            border_spacing=4, height=20,
            fg_color='#66BB6A', hover_color='#4CAF50',
            command=self._grid_edition
        )

        self._bt_back = ctk.CTkButton(
            self, text='Voltar',
            font=('Torus Notched Regular', 22, 'normal'),
            border_spacing=4, height=20,
            command=self._on_closing
        )

        self._bt_edit.grid_configure(row=3, column=0, padx=200, pady=6, sticky='w')
        self._bt_back.grid_configure(row=3, column=0, padx=200, pady=6, sticky='e')

        self.focus_force()
        self.grab_set()
   
    def get(self):
        return {
            'id': self._id.get(),
            'name':self._name_tutor.get(),
            'tel1': self._tel1.get(),
            'tel2': self._tel2.get(),
            'freq': self._freq.get(), 
            'address':self._address.get()
        }
    
    def set(self, id_:int, name:str, tel1:str, tel2:str, frequencia:str, address:str):
        self._id.set(id_)
        self._name_tutor.set(name)
        self._tel1.set(tel1)       
        self._tel2.set(tel2)
        self._freq.set(frequencia)
        self._address.set(address)
    
    def set_table(self, dados):
        for i, list_ in enumerate(dados):
            list_ = list(list_)
            self._table.add_row(list_, i+1)
    
    def _grid_edition(self):
        self._id_bkp = self._id.get()
        self._name_bkp = self._name_tutor.get()
        self._tel1_bkp = self._tel1.get()
        self._tel2_bkp = self._tel2.get()
        self._freq_bkp = self._freq.get()
        self._address_bkp = self._address.get()

        self._name_display.configure(state='normal')
        self._tel1_display.configure(state='normal')
        self._tel2_display.configure(state='normal')
        self._freq_display.configure(state='normal')
        self._address_display.configure(state='normal')

        self._bt_remove.grid_configure(row=0, column=0, padx=10, pady=5, sticky='en')
        self._bt_edit.configure(text='Salvar', command=self._call_save_edition)
        self._bt_back.configure(
            text='Cancelar', command=self._grid_cancel_edit,
            fg_color='#E57373',hover_color='#EF5350'
            )
    
    def _call_save_edition(self):
        call = self.master.save_edit_tutor()
        if call:
            self.set(call[0], call[1], call[2], call[3], call[4], call[5])
            self._name_display.configure(state='readonly')
            self._tel1_display.configure(state='readonly')
            self._tel2_display.configure(state='readonly')
            self._freq_display.configure(state='disabled')
            self._address_display.configure(state='readonly')

            self._bt_remove.grid_forget()
            self._bt_edit.configure(text='Editar', command=self._grid_edition)
            self._bt_back.configure(text='Voltar', command=self._on_closing)

    def _grid_cancel_edit(self):
        self._name_display.configure(state='readonly')
        self._tel1_display.configure(state='readonly')
        self._tel2_display.configure(state='readonly')
        self._freq_display.configure(state='disabled')
        self._address_display.configure(state='readonly')

        self._id.set(self._id_bkp)
        self._name_tutor.set(self._name_bkp)
        self._tel1.set(self._tel1_bkp)
        self._tel2.set(self._tel2_bkp)
        self._freq.set(self._freq_bkp)
        self._address.set(self._address_bkp)

        self._bt_remove.grid_forget()
        self._bt_edit.configure(text='Editar', command=self._grid_edition)
        self._bt_back.configure(
            text='Voltar', command=self._on_closing,
            fg_color='#42A5F5',hover_color='#2196F3'
            )
    
    def grid_adition(self):
        self._name_display.configure(state='normal')
        self._tel1_display.configure(state='normal')
        self._tel2_display.configure(state='normal')
        self._freq_display.configure(state='normal')
        self._address_display.configure(state='normal')

        self._bt_edit.configure(text='Salvar', command=self._call_save_adition)
        self._bt_back.configure(
            text='Cancelar', command=self._on_closing,
            fg_color='#E57373',hover_color='#EF5350'
            )
    
    def _call_save_adition(self):
        call = self.master.save_new_tutor()
        if call:
            self.set(call[0], call[1], call[2], call[3], call[4], call[5])
            self._name_display.configure(state='readonly')
            self._tel1_display.configure(state='readonly')
            self._tel2_display.configure(state='readonly')
            self._freq_display.configure(state='disabled')
            self._address_display.configure(state='readonly')

            self._bt_edit.configure(text='Editar', command=self._grid_edition)
            self._bt_back.configure(text='Voltar', command=self._on_closing)
    
    def _call_delete_tutor(self):
        call = self.master.delete_tutor(self._id.get(), self._name_tutor.get())
        print(call)
        if call:
            self._on_closing()
    
    def _call_goto_pet(self, *args, **kargs):
        line = self._table.get_row(args[0]['row'])
        id_ = line[0]
        self.master.show_pet(id_)
        self.grab_release()
        self.master.focus_force()
        
    def _on_closing(self):
        self.master.search()
        self.grab_release()
        self.destroy()
