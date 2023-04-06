from collections import deque

class ExpressaoService:
    def __init__(self):
        self.expressoesCaracteres = '{[()]}'

    def validarExpressaoAction(self):
        expressao = input('Digite a Expressao Aritmética')

        if(self._validarExpressao(expressao)):
            print('Expressão válida')
        else:
            print('Expressão inválida')

    def _validarExpressao(self, expressao):
        pilha = deque()

        for caractere in expressao:
            if caractere in self.expressoesCaracteres:
                if caractere in ['(', '[', '{']:
                    pilha.append(caractere)
                else:
                    if len(pilha) == 0:
                        return False
                    else:
                        top = pilha.pop()

                        isParentesis = caractere == ')' and top == '('
                        isColchetes = caractere == ']' and top == '['
                        isChaves = caractere == '}' and top == '{'

                        if not(isParentesis or isColchetes or isChaves):
                            return False

        return len(pilha) == 0