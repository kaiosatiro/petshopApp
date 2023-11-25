from datetime import datetime

from CTkMessagebox import CTkMessagebox

#This file contains functions that display messages. Some are customizable and some are for specific use.

def error_message_bd(frame, error:tuple):
    # try: except AttributeError
    if error.sqlite_errorcode == 2067:
        return CTkMessagebox(
            frame, title="Erro",
            message="Já existe!",
            icon="cancel",
            font=('Torus Notched Regular', 18, 'normal'),
            justify='center',
            option_focus=1
        )
    else:
        time = datetime.now()
        time = time.strftime("%d-%b-%Y %H:%M:%S")
        msg = f"{time}\n{error}"
        return CTkMessagebox(
            frame, title="Erro",
            message=msg,
            icon="cancel",
            font=('Torus Notched Regular', 18, 'normal'),
            justify='center',
            option_focus=1
        )


def error_message(frame, title:str, message:str):
    return CTkMessagebox(
        frame, title=title,
        message=message,
        icon="cancel",
        font=('Torus Notched Regular', 18, 'normal'),
        justify='center',
        option_focus=1,
        sound=True
        )


def done_message(frame, message:str):
    return CTkMessagebox(
        frame,
        title="Aviso",
        icon="check", 
        message=message,
        font=('Torus Notched Regular', 16, 'normal'),
        justify='center'
            )


def delete_message(frame, message:str):
    return CTkMessagebox(
        frame,
        title="Atenção!", icon="warning", 
        message=message,
        font=('Torus Notched Regular', 16, 'normal'),
        sound=True,
        option_1='Sim',
        option_2='Não, cancelar',  
        justify='center',
        option_focus=1                
            )


def delete_many_pets(frame):
    return CTkMessagebox(
        frame,
        title="Excluir PETS?",
        width=500, justify='center',
        message=f"Pets que não possuem outro tutor tambem serão excluídos.\nTem certeza? (Pets com outro tutor permanecem)", 
        icon="warning", font=('Torus Notched Regular', 18, 'normal'),
        sound=True, option_focus=1,
        option_1='Tenho', option_2='Não'
        )