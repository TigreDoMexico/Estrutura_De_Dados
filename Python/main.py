from src import ExecutarMenuExpressao, BoasVindas, MontarBancoDeDados

if MontarBancoDeDados():
    BoasVindas()

    while True:
        ExecutarMenuExpressao()
else:
    print("Erro ao Gerar Banco de Dados. Não é possível executar o programa")