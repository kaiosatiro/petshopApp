import customtkinter as ctk
from CTkTable import *

# This is the TOP display that used the TUTOR data cached on the interface instance, 
# to seek a tutor to be added on a relation with the pet. 
# This is during the pet addition or edition.

class TutorSearchPanel(ctk.CTkToplevel):
    def __init__(self, master, lista:list=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title("Tutores")
        self.geometry("600x400")
        self.maxsize(600, 400)
        self.minsize(600, 400)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1) 
        self.protocol("WM_DELETE_WINDOW", self._on_closing)

        self._chosen_id = None #Union[str, None] = None
        
        self._frame = ctk.CTkScrollableFrame(self)
        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        self._data = ctk.StringVar()
        self._data.trace_add('write', self._search)
        self._entry = ctk.CTkEntry(
            self, placeholder_text='Nome do tutor...',
            textvariable=self._data,
            font=('Torus Notched Regular', 18, 'normal')
        )
        self._entry.grid(row=0, sticky='ew', padx=40, pady=(10, 0))   

        self._pre_list = lista
        self._table_head = [['Id', 'Nome']]
        self._table_head.extend(self._pre_list)
        self._table = CTkTable(
            self._frame, column=2, values=self._table_head,
            hover=True, hover_color='grey', header_color='grey',
            font=('Torus Notched Regular', 18, 'normal'),
            command=self._on_select
        )
        self._table.pack(expand=True, fill="both", padx=20, pady=20)
        self._table.edit_column(0, width=1)
        self._table.edit_column(1, width=300)

        self._bt_add = ctk.CTkButton(
            self, text='Cancelar',
            font=('Torus Notched Regular', 22, 'normal'),
            border_spacing=4,
            command=self._cancel_event
        )
        self._bt_add.grid(row=2, column=0, pady=(0, 10))
        
        self.grab_set()
    

    def _search(self, *args, **kargs):
        data = self._data.get().upper()
        values = []
        for i, item in enumerate(self._pre_list):
            if data in item[1].upper():
                values.append(item)
        values.insert(0, self._table_head[0])
        self._set(values)


    def _set(self, data:list):
        self._table.configure(values=data)
    

    def get_choice(self):
        self.master.wait_window(self)
        return self._chosen_id
    

    def _on_select(self, *args, **kwargs):
        row = self._table.get_row(args[0]['row'])
        self._chosen_id = int(row[0])
        self.grab_release()
        self.destroy()          
    

    def _on_closing(self):
        self.grab_release()
        self.destroy()


    def _cancel_event(self):
        self.grab_release()
        self.destroy()


    
                
        