import os
import platform
import re

def clear_screen():
    os.system('cls') if platform.system() == 'Windows' else os.system('clear')
    
def read_text(min_length=0, max_length=100, msg=None):
    print(msg) if msg else None
    while True:
        text = input('> ')
        if min_length <=len(text) <= max_length:
            return text
        
def valid_dni(dni):
    if not re.match('[0-9]{2}[A-Z]$', dni):
        print("Incorrect DNI format")
        return False
    return True