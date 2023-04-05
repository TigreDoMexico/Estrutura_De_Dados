from src import ExecutarMenuOperacao, BoasVindas, MontarBancoDeDados

if MontarBancoDeDados():
    BoasVindas()

    while True:
        ExecutarMenuOperacao()
else:
    print("Erro ao Gerar Banco de Dados. Não é possível executar o programa")