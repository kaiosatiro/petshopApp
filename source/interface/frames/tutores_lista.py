import customtkinter as ctk
from CTkTable import *

#ADICIONAR MENSAGEM NÂO ENCONTRADO 
class FrameListaTutores(ctk.CTkToplevel):
    def __init__(self, master, lista:list=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title("Tutores")
        self.geometry("600x400")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1) 
        self.protocol("WM_DELETE_WINDOW", self._on_closing)

        self._chosen_id = None #Union[str, None] = None
        
        self.frame = ctk.CTkScrollableFrame(self)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        self.entry = ctk.StringVar()
        self.entry.trace_add('write', self.pesquisa)
        self.entrada = ctk.CTkEntry(
            self, placeholder_text='Nome do tutor...',
            textvariable=self.entry,
            font=('', 18, 'normal')
        )
        self.entrada.grid(row=0, sticky='ew', padx=40, pady=(10, 0))   

        self.lista = lista
        self.head = [['Id', 'Nome']]
        self.head.extend(self.lista)
        self.tabela = CTkTable(
            self.frame, column=2, values=self.head,
            hover=True, hover_color='grey', header_color='grey',
            font=('', 18, 'normal'),
            command=self._on_select
        )
        self.tabela.pack(expand=True, fill="both", padx=20, pady=20)
        self.tabela.edit_column(0, width=1)
        self.tabela.edit_column(1, width=300)

        self.BT_add = ctk.CTkButton(
            self, text='Cancelar',
            font=('', 22, 'normal'),
            border_spacing=4,
            command=self._cancel_event
        )
        self.BT_add.grid(row=2, column=0, pady=(0, 10))
        
        self.grab_set()
    

    def pesquisa(self, *args, **kargs):
        dado = self.entry.get().upper()
        values = []
        for i, item in enumerate(self.lista):
            if dado in item[1].upper():
                values.append(item)
        values.insert(0, self.head[0])
        self.set(values)


    def set(self, dados:list):
        self.tabela.configure(values=dados)
    

    def get_choice(self):
        self.master.wait_window(self)
        return self._chosen_id
    

    def _on_select(self, *args, **kwargs):
        row = self.tabela.get_row(args[0]['row'])
        self._chosen_id = int(row[0])
        self.grab_release()
        self.destroy()          
    

    def _on_closing(self):
        self.grab_release()
        self.destroy()


    def _cancel_event(self):
        self.grab_release()
        self.destroy()

    
if __name__ == '__main__':
    app = ctk.CTk()
    app.geometry("400x240")
    ctk.set_appearance_mode("light")
    lista = [[333, 'Caio Sousa'], [444, 'Caio Satiro De '], [222, ' SATIRO DE SOUSA'], [111, 'Caio   Sousa'], [666, ' SATIRO DE SOUSA'], [999, 'CAIO SATIRO  SOUSA'], [555, 'CAIO SATIRO DE SOUSA'], [777, 'CAIO SATIRO DE SOUSA'], [888, 'CAIO SATIRO DE SOUSA'], [999999, 'CAIO SATIRO DE SOUSA'], [2222222, 'CAIO SATIRO  '], [44444, 'CAIO  DE SOUSA'], [11111, ' SATIRO DE SOUSA'], [33333, 'CAIO   SOUSA'], ]

    t = FrameListaTutores(app, lista)

    print(t)
    app.mainloop()

    
                
        