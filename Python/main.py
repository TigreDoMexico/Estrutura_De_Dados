from src import ExecutarMenuRaiz, BoasVindas, MontarBancoDeDados



if MontarBancoDeDados():
    BoasVindas()

    opcao = 0

    while opcao != 1:
        opcao = ExecutarMenuRaiz()
else:
    print("Erro ao Gerar Banco de Dados. Não é possível executar o programa")