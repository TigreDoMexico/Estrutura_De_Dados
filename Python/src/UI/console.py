import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait():
    input('Pressione ENTER para continuar...')