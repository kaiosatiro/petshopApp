import customtkinter as ctk
from CTkTable import *

#This is the main result table. The table needs to be remade on every result. 
# I need to rethink this on a case for heavy loads of data.

class SearchTable(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color='transparent')

        self._master_blaster = master
        
        self._head_pet = [['#', 'id', 'Nome', 'Raça', 'Porte', 'Sexo']]
        self._head_tutor = [['#', 'id', 'Nome', 'Telefone 1', 'Telefone 2', 'Frequência']]

        self._table = CTkTable(
            self, column=6, values=self._head_pet,
            hover=True, hover_color='grey', header_color='grey',
            font=('Torus Notched Regular', 22, 'normal'), command=self._filter_exclude_hearder_from_search,
        )
        self._table.pack(expand=True, fill="both", padx=20, pady=20)

    def set(self, head, data:list):
        for i in range(1, self._table.rows+1):
            self._table.delete_row(i)
        if head == 1:
            table_data = self._head_pet.copy()
            for i in data:
                table_data.append(i)
            for i, list_ in enumerate(table_data):
                if i == 0:
                    self._table.add_row(list_, i)
                else:
                    list_ = list(list_ )
                    list_.insert(0, i)
                    self._table.add_row(list_, i)
        elif head == 2:
            table_data = self._head_tutor.copy()
            for i in data:
                table_data.append(i)
            for i, list_ in enumerate(table_data):
                if i == 0:
                    self._table.add_row(list_, i)
                else:
                    list_ = list(list_)
                    list_.insert(0, i)
                    self._table.add_row(list_, i)
                    
        self._table.edit_column(0, width=10)
        self._table.edit_column(1, width=100)
        self._table.edit_column(2, width=400)
        self._table.edit_column(3, width=150)
        self._table.edit_column(4, width=150)
        self._table.edit_column(4, width=150)
        
    def _change_header(self, type_):
        if type_ == 1:
            self._table.configure(values=self._head_pet)
        elif type_ == 2:
            self._table.configure(values=self._head_tutor)
    
    def _get_id(self, line):
        return int(self._table.get(line, 1))
    
    def get_name(self, line):
        return self._table.get(line, 2)
    
    def _filter_exclude_hearder_from_search(self, *args):
        if args[0]['row'] == 0:
            return
        else:
            line = args[0]['row']
            id_ = int(self._get_id(line))
            type_ = self._master_blaster._search_type.get()
            if type_ == 1:
                self._master_blaster.show_pet(id_)
            elif type_ == 2:
                self._master_blaster.set_tutor_panel(id_)
            