class Operacao:
    def __init__(self, delegateTuple, valores):
        self.Delegate = delegateTuple[0]
        self.Simbolo = delegateTuple[1]
        self.Valores = valores

    def __str__(self):
        out = ''
        for valor in self.Valores:
            out += str(valor) + ' ' + self.Simbolo + ' '

        return out[:-3]

    def executarDelegate(self):
        return self.Delegate(self)

def operacao_soma(operacao: Operacao):
    return sum(operacao.Valores)

def operacao_subtracao(operacao: Operacao):
    resultado = operacao.Valores[0]
    for valor in operacao.Valores[1:]:
        resultado -= valor
    return resultado

def operacao_multiplicacao(operacao: Operacao):
    func = lambda valores: valores[0] if len(valores) == 1 else valores[0] * func(valores[1:])
    return func(operacao.Valores)

def operacao_divisao(operacao: Operacao):
    resultado = operacao.Valores[0]
    for valor in operacao.Valores[1:]:
        resultado = resultado / valor if valor > 0 else resultado
    return resultado

opcoesOperacoes = {
    1: (operacao_soma, '+'),
    2: (operacao_subtracao, '-'),
    3: (operacao_multiplicacao, '*'),
    4: (operacao_divisao, '/'),
}