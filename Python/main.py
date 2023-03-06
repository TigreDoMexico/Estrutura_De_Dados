from src import ExecutarMenuUsuario, BoasVindas, MontarBancoDeDados

if MontarBancoDeDados():
    BoasVindas()

    while True:
        ExecutarMenuUsuario()
else:
    print("Erro ao Gerar Banco de Dados. Não é possível executar o programa")