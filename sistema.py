menu = """
*********Sistema Bancario*********

Digite opção desejada:

[1] - Depositar
[2] - Saque
[3] - Extrato
[0] - Sair

**********************************
"""
LIMITE_SAQUE = 3
LIMITE_MAXIMO = 500
tentativas_saque_no_dia = 0
saldo_da_conta = 0
extrato = []
cont = True
while(cont):

    opcao = int(input(menu))
    if(opcao == 1):
        valor = float(input("Digite o valor a ser depositado: "))
        if(valor > 0):
            saldo_da_conta += valor
            msg = [f"Valor depositado em conta: R$ {valor:.2f}"]
            extrato += msg
            print(msg[0])
        else:
            print("Valor invalido, tente novamente!")
    elif(opcao == 2):
        valor_saque = float(input("Digite o valor a ser sacado:"))
        if(saldo_da_conta >= valor_saque and valor_saque <= LIMITE_MAXIMO):
            if(tentativas_saque_no_dia <= LIMITE_SAQUE):
                tentativas_saque_no_dia += 1
                saldo_da_conta -= valor_saque
                msg = [f"Saque realizado no valor de {valor_saque:.2f}"]
                extrato += msg
                print(msg[0])
            else:
                print("Tentativas de saque excedido, por favor tente novamente outro dia!")
        else:
            print("Valor indisponivel!")
    elif(opcao == 3):
        if(extrato == []):
            print("Não foram realizadas movimentações.")
        else:
            for linha in extrato:
                print(linha)
            print(f"Saldo atual da conta R$ {saldo_da_conta:.2f}")
    elif(opcao == 0):
        break
        cont = False
    else:
        print("Opção invalida, tente novamente!")