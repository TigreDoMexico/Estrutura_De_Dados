from src.UI.message import EntradaInvalida

def ObterInputUsuario(mensagem = 'Digite um valor: \n'):
    valor = 0
    valorValido = False

    while not(valorValido):
        valorDigitado = input(mensagem)
        try:
            valor = int(valorDigitado)
            valorValido = True
        except:
            EntradaInvalida()

    return valor
