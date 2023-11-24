import os
from tkinter import filedialog

import customtkinter as ctk
from PIL import Image


class FileHandler(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Arquivo")
        self.geometry("640x320+500+200")
        self.maxsize(640, 320)
        self.minsize(640, 320)
        
        self.protocol("WM_DELETE_WINDOW", self._on_closing)

        self._lupe_img = ctk.CTkImage(Image.open(os.path.relpath("petApp/images/lupe.png")), size=(28,28))

        self._radio_choice = ctk.IntVar(value=1)
        self._entry_path = ctk.StringVar(value='')
        self._options_choice = ctk.StringVar(value='Pets')
        self._options_import = ['Pets', 'Tutores', 'Racas']
        self._options_export = ['Pets', 'Tutores', 'Racas', 'Tudo']
        
        self._frame = ctk.CTkFrame(self)
       
        self._bt_import = ctk.CTkRadioButton(
            self._frame, text=" Importar", font=('Torus Notched Regular', 30, 'normal'), hover=True,
            variable=self._radio_choice, value=1, command=self._radio
        )
        self._options_menu = ctk.CTkOptionMenu(
            self._frame, variable=self._options_choice,
            state='normal', values=self._options_import,
            font=('Torus Notched Regular', 26, 'normal'), 
            dropdown_font=('', 26, 'normal'),
            dropdown_fg_color="#BBDEFB", dropdown_hover_color="#90CAF9",
            width=240
        )
        self._bt_export = ctk.CTkRadioButton(
            self._frame, text=" Exportar", font=('Torus Notched Regular', 30, 'normal'), hover=True,
              variable=self._radio_choice, value=2, command=self._radio
        )

        self._label = ctk.CTkLabel(self._frame, text='Arquivo:', font=('Torus Notched Regular', 24, 'normal'), width=90)
        self._path = ctk.CTkEntry(self._frame, font=('Torus Notched Regular', 22, 'normal'), textvariable=self._entry_path)

        self._bt_search = ctk.CTkButton(
            self._frame, text='', image=self._lupe_img,
            font=('Torus Notched Regular', 24, 'normal'),
            width=60, height=30
        )

        self._bt_exe = ctk.CTkButton(
            self, text='Importar',
            font=('Torus Notched Regular', 28, 'normal'),
            fg_color='#66BB6A', hover_color='#4CAF50',
            width=200,
        )

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self._frame.grid_configure(row=1, padx=10, pady=(5, 0), sticky='nsew')
        self._frame.grid_rowconfigure((0,1), weight=1)
        self._frame.grid_columnconfigure(1, weight=1)

        self._bt_import.grid_configure(row=0, column=0, columnspan=3, sticky='w', pady=(10, 0), padx=100)
        self._options_menu.grid_configure(row=1, column=0, columnspan=3, pady=(0, 70))
        self._bt_export.grid_configure(row=0, column=0, columnspan=3, sticky='e', pady=(10, 0), padx=100)
        self._label.grid_configure(row=3, column=0, padx=5, pady=(0,10), sticky='w')
        self._path.grid_configure(row=3, column=1, pady=(0,10), sticky='ew')
        self._bt_search.grid_configure(row=3, column=2, padx=5, pady=(0,10), stick='e')
        self._bt_exe.grid_configure(row=2, padx=130, pady=5)

        self._radio()
        self.focus_force()
        self.grab_set()
        # CTkMessagebox(self.master, title="Aviso!", message="Dê preferência aos formatos Jpeg e PNzG!", justify='center', option_focus=1)

    def _radio(self):
        if self._radio_choice.get() == 1:
            self._bt_exe.configure(text='Importar', command=self._import_data)
            self._bt_search.configure(command=self._lupe_file)
            self._options_menu.configure(state='normal')
            self._label.configure(text='Arquivo:')
            self._options_menu.configure(values=self._options_import)
            self._options_choice.set('Pets')
            self._entry_path.set('')
        elif self._radio_choice.get() == 2:
            self._bt_exe.configure(text='Exportar', command=self._export_data)
            self._bt_search.configure(command=self._lupe_dir)
            self._label.configure(text='Pasta:')
            self._options_menu.configure(values=self._options_export)
            self._options_choice.set('Tudo')
            self._entry_path.set('')
    
    def _lupe_file(self):
        get = filedialog.askopenfile(mode ='r', filetypes =[('Planilhas .csv .xlsx, .xls', ['.csv', '.xlsx', '.xls'])])
        if not get:
            return None
        self._entry_path.set(get.name)
        self._path.configure(border_color='grey')
        self.focus_force()
    
    def _lupe_dir(self):
        get = filedialog.askdirectory()
        if not get:
            return None
        self._entry_path.set(get)
        self._path.configure(border_color='grey')
        self.focus_force()

    def _export_data(self):
        path = self._entry_path.get()
        op = self._options_choice.get()
        if not os.path.exists(path):
            self._path.configure(border_color='red')
        else:
            self.master.export_data(op, path)

    def _import_data(self):    
        path = self._entry_path.get()
        op = self._options_choice.get()
        if not os.path.exists(path):
            self._path.configure(border_color='red')
        else:
            self.master.import_data(op, path)

    def _on_closing(self):
        self.grab_release()
        self.destroy()
