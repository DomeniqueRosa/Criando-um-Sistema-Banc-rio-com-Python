menu = """
*********Sistema Bancario*********

Digite opção desejada:

[1] - Depositar
[2] - Saque
[3] - Extrato
[0] - Sair

**********************************
"""
LIMITE_TENTATIVAS_SAQUE = 3
LIMITE_MAXIMO = 500

tentativas_saque_no_dia = 0
saldo_da_conta = 0
extrato = []

def depositar (saldo_da_conta, valor, extrato):    
    if(valor > 0):
        saldo_da_conta += valor
        msg = [f"Valor depositado em conta: R$ {valor:.2f}"]
        extrato += msg
        return saldo_da_conta, extrato
    else:
        print("Valor invalido, tente novamente!")

def sacar(saldo_da_conta=None, valor_saque=None, extrato=None, limite=LIMITE_MAXIMO, tentativas_saque_no_dia=tentativas_saque_no_dia):
    if(tentativas_saque_no_dia <= LIMITE_TENTATIVAS_SAQUE and valor_saque <= LIMITE_MAXIMO and valor_saque <= saldo_da_conta):
        msg = [f"Valor sacado em conta: R$ {valor_saque:.2f}"]
        extrato += msg
        saldo_da_conta -= valor_saque
        tentativas_saque_no_dia += 1
    else:
        if(valor_saque > saldo_da_conta):
            print("Valor maior que disponivel em conta, saque cancelado.")
        if(valor_saque > LIMITE_MAXIMO):
            print("Limite ultrapassado, é permitido saque apenas de valores de R$500,00 ou menor!")
        if(tentativas_saque_no_dia > LIMITE_MAXIMO):
            print("Excedito tentativas de saque por dia!")
    return saldo_da_conta, extrato, tentativas_saque_no_dia

def extrato_conta(saldo, extrato):
    print("*"*34)
    print("Extrato da Conta".center(34,"*")+"\n\n")
    
    if(extrato != []):
        for linha in extrato:
            print(linha)
        print("\n")
        print(f"Saldo da conta: R$ {saldo:.2f}".center(34," "))
    else:
        print("Sem movimentações na conta!".center(34," "))
    print("*"*34)

while(True):
    
    opcao = int(input(menu))
    if(opcao == 1):
        valor = float(input("Digite o valor que deseja depositar: "))
        saldo_da_conta, extrato = depositar(saldo_da_conta, valor, extrato)
    elif(opcao == 2):
        valor_saque = float(input("Digite o valor que deseja sacar:"))
        saldo_da_conta, extrato, tentativas_saque_no_dia = sacar(saldo_da_conta= saldo_da_conta, valor_saque= valor_saque, extrato= extrato, limite=LIMITE_MAXIMO,tentativas_saque_no_dia=tentativas_saque_no_dia)     
    elif(opcao == 3):
       extrato_conta(saldo_da_conta, extrato)
       input("Digite Enter para continuar.")     
    elif(opcao == 0):
        break
    else:
        print("Opção invalida, tente novamente!")

