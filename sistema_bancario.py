menu = '''
1- Depósito
2- Saque
3- Extrato
4- Sair
Operação: '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

def deposito():
    global saldo
    global extrato
    valor_deposito = int(input('Digite o valor do deposito: '))
    if valor_deposito > 0:
        saldo += valor_deposito
        print('Deposito realizado!')
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"

def saque():
    global saldo
    global numero_saques
    global extrato
    valor_saque = int(input('Digite o valor do saque: '))
    if 0 < valor_saque <= saldo and valor_saque < 500 and numero_saques < LIMITE_SAQUE:
        saldo -= valor_saque
        print('Saque Realizado!')
        numero_saques +=1
        extrato += f"Saque: R$ {valor_saque:.2f}\n"
    elif valor_saque < 0:
        print('Operação inválida!')
    elif valor_saque > saldo:
        print('Saldo insuficiente')
    elif numero_saques >= LIMITE_SAQUE:
        print('Limite de saques excedido!')
    elif valor_saque > 500:
        print('Seu limite por saque é de R$500')


while True:
    operacao = int(input(menu))
    match operacao:
        case 1:
            deposito()
        case 2:
            saque()
        case 3:
            print(f'\n==== EXTRATO ====\n{extrato}\n== Saldo: {saldo} ==')
        case 4:
            print('Saindo...')
            break
        case _:
           print('Operação Inválida!')
           exit()