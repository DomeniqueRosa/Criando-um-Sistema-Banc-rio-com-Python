menu = """
*********Sistema Bancario*********

Digite opção desejada:

[1] - Depositar
[2] - Saque
[3] - Extrato
[4] - Criar usuario
[5] - Criar conta
[6] - Listar contas
[0] - Sair

**********************************
"""
LIMITE_TENTATIVAS_SAQUE = 3
LIMITE_MAXIMO = 500

tentativas_saque_no_dia = 0
saldo_da_conta = 0
extrato = []
contas = []
usuarios = []
contas = []
def listar_contas(contas):
    for c in contas:
        for chave, valor in c.items():
            print(f"{chave} : {valor}")
           
def filtrar_usuario(cpf, usuarios):
    ind = -1
    for u in usuarios:
        ind += 1
        if cpf in u["cpf"]:
            esta = True
            
            break
        else:
            esta = False

    return esta, ind

def criar_conta(contas, usuario, ind, tamanho):
    numero_conta = tamanho + 1
    conta = {"nr_conta" : numero_conta, "agencia" : "0001", "usuario": usuario[ind]}
    return conta

def criar_usuario():
    nome = input("Digite o nome: ")
    data = input("Digite data de nascimento dd-mm-aaaa: ")
    cpf = input("Digite o cpf do usuario: ")
    endereco = input("Digite o endereço rua, nro - bairro - cidade/estado:  ")

    cadastro = {"nome": nome, "data": data, "cpf": cpf, "endereco": endereco}

    return cadastro

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
        if(tentativas_saque_no_dia > LIMITE_TENTATIVAS_SAQUE):
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
    elif(opcao == 4):
        cpf = input("Digite o cpf apenas com numeros: ")
        esta, ind = filtrar_usuario(cpf, usuarios)
        if(esta):
            print("Usuario já cadastrado!")
        else:
            usuarios.append(criar_usuario())
    elif(opcao == 5):
        cpf = input("Digite o cpf apenas com numeros: ")
        esta, ind = filtrar_usuario(cpf, usuarios)
        if(esta):
            tamanho = len(contas)
            contas.append(criar_conta(cpf, usuarios, ind, tamanho))
            print("Cadastrado realizado com sucesso!")
        else:
            print("Usuario não cadastrado, para criar conta o cpf deve estar cadastrado!")
    elif(opcao == 6):
        listar_contas(contas)
    elif(opcao == 0):
        break
    else:
        print("Opção invalida, tente novamente!")

