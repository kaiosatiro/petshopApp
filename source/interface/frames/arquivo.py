import customtkinter as ctk
from PIL import Image
from tkinter import filedialog
import os

class FrameArquivo(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Arquivo")
        self.geometry("640x320+500+200")
        self.maxsize(640, 320)
        self.minsize(640, 320)
        
        self.protocol("WM_DELETE_WINDOW", self._on_closing)

        self.lupe_img = ctk.CTkImage(Image.open(os.path.realpath("source/interface/images/lupe.png")), size=(28,28))

        self.var_radio = ctk.IntVar(value=1)
        self.var_entry = ctk.StringVar(value='')
        self.var_option = ctk.StringVar(value='Pets')
        self.options_lista_imp = ['Pets', 'Tutores', 'Racas']
        self.options_lista_ex = ['Pets', 'Tutores', 'Racas', 'Tudo']
        
        self.frame = ctk.CTkFrame(self)
       
        self.importar = ctk.CTkRadioButton(
            self.frame, text=" Importar", font=('', 30, 'normal'), hover=True,
            variable=self.var_radio, value=1, command=self._radio
        )
        self.options = ctk.CTkOptionMenu(
            self.frame, variable=self.var_option,
            state='normal', values=self.options_lista_imp,
            font=('', 26, 'normal'), dropdown_font=('', 26, 'normal'),
            width=240
        )
        self.exportar = ctk.CTkRadioButton(
            self.frame, text=" Exportar", font=('', 30, 'normal'), hover=True,
              variable=self.var_radio, value=2, command=self._radio
        )

        self.label = ctk.CTkLabel(self.frame, text='Arquivo:', font=('', 24, 'normal'), width=100)
        self.diretorio = ctk.CTkEntry(self.frame, font=('', 22, 'normal'), textvariable=self.var_entry)

        self.bt_busca = ctk.CTkButton(
            self.frame, text='', image=self.lupe_img,
            font=('', 24, 'normal'),
            width=60, height=30
        )

        self.bt_exe = ctk.CTkButton(
            self, text='Importar',
            font=('', 28, 'normal'),
            width=200,
        )

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frame.grid_configure(row=1, padx=10, pady=(5, 0), sticky='nsew')
        self.frame.grid_rowconfigure((0,1), weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

        self.importar.grid_configure(row=0, column=0, columnspan=3, sticky='w', pady=(10, 0), padx=100)
        self.options.grid_configure(row=1, column=0, columnspan=3, pady=(0, 70))
        self.exportar.grid_configure(row=0, column=0, columnspan=3, sticky='e', pady=(10, 0), padx=100)
        self.label.grid_configure(row=3, column=0, padx=5, pady=(0,10), sticky='w')
        self.diretorio.grid_configure(row=3, column=1, padx=5, pady=(0,10), sticky='ew')
        self.bt_busca.grid_configure(row=3, column=2, padx=5, pady=(0,10), stick='e')
        self.bt_exe.grid_configure(row=2, padx=130, pady=5)

        self._radio()
        self.focus_force()
        self.grab_set()
        # CTkMessagebox(self.master, title="Aviso!", message="Dê preferência aos formatos Jpeg e PNG!", justify='center', option_focus=1)


    def _radio(self):
        if self.var_radio.get() == 1:
            self.bt_exe.configure(text='Importar', command=self._importar_dados)
            self.bt_busca.configure(command=self._lupe_file)
            self.options.configure(state='normal')
            self.label.configure(text='Arquivo:')
            self.options.configure(values=self.options_lista_imp)
            self.var_option.set('Pets')
            self.var_entry.set('')
        elif self.var_radio.get() == 2:
            self.bt_exe.configure(text='Exportar', command=self._exportar_dados)
            self.bt_busca.configure(command=self._lupe_dir)
            self.label.configure(text='Pasta:')
            self.options.configure(values=self.options_lista_ex)
            self.var_option.set('Tudo')
            self.var_entry.set('')
    

    def _lupe_file(self):
        get = filedialog.askopenfile(mode ='r', filetypes =[('Planilhas .csv .xlsx, .xls', ['.csv', '.xlsx', '.xls'])])
        if not get:
            return None
        self.var_entry.set(get.name)
        self.diretorio.configure(border_color='grey')
        self.focus_force()
    

    def _lupe_dir(self):
        get = filedialog.askdirectory()
        if not get:
            return None
        self.var_entry.set(get)
        self.diretorio.configure(border_color='grey')
        self.focus_force()

    def _exportar_dados(self):
        path = self.var_entry.get()
        op = self.var_option.get()
        if not os.path.exists(path):
            self.diretorio.configure(border_color='red')
        else:
            self.master.export_data(op, path)



    def _importar_dados(self):    
        path = self.var_entry.get()
        op = self.var_option.get()
        if not os.path.exists(path):
            self.diretorio.configure(border_color='red')
        else:
            self.master.import_data(op, path)
            
    

    def _on_closing(self):
        self.grab_release()
        self.destroy()


if __name__ == '__main__':
    ctk.set_appearance_mode("light")
    app = ctk.CTk()
    t = FrameArquivo(app)
    
    app.mainloop()