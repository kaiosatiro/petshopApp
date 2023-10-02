__version__ = '1.0'
__author__ = 'Caio Satiro'

import os

from source.backend import DB
from source.main import Main

def main():
    dB = DB(os.getcwd()) #os.path.abspath(__file__)
    app = Main(dB)
    app.mainloop()

if __name__ == '__main__':
    main()