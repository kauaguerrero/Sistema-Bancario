menu = '''
1- Depósito
2- Saque
3- Extrato
4- Criar usuário
5- Criar conta corrente
6- Lista de cliente
7- Lista de contas
8- Sair
Operação: '''

limite = 500
LIMITE_SAQUE = 3
clientes = []
contas = []

def deposito():
    conta = selecionar_conta()
    if not conta:
        return

    try:
        valor_deposito = float(input('Digite o valor do depósito: '))
        if valor_deposito > 0:
            conta['saldo'] += valor_deposito
            print('Depósito realizado com sucesso!')
            conta['extrato'] += f"Depósito: R$ {valor_deposito:.2f}\n"
        else:
            print('O valor do depósito deve ser positivo.')
    except ValueError:
        print('Entrada inválida! Digite um número.')

def saque():
    conta = selecionar_conta()
    if not conta:
        return

    try:
        valor_saque = float(input('Digite o valor do saque: '))
        if valor_saque <= 0:
            print('Operação inválida! O valor deve ser maior que zero.')
        elif valor_saque > conta['saldo']:
            print('Saldo insuficiente.')
        elif valor_saque > limite:
            print(f'Seu limite por saque é de R$ {limite}')
        elif conta['numero_saques'] >= LIMITE_SAQUE:
            print('Limite de saques excedido!')
        else:
            conta['saldo'] -= valor_saque
            conta['numero_saques'] += 1
            print('Saque realizado com sucesso!')
            conta['extrato'] += f"Saque: R$ {valor_saque:.2f}\n"
    except ValueError:
        print('Entrada inválida! Digite um número.')

def criar_cliente():
    cpf = input('Digite o CPF (somente números): ')
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            print('CPF já cadastrado!')
            return

    nome = input('Digite o nome: ')
    data_nascimento = input('Digite a data de nascimento (DD/MM/AAAA): ')
    endereco = input('Digite o endereço (Rua, N°, Bairro, Cidade/Estado): ')

    cliente = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereço': endereco
    }

    clientes.append(cliente)
    print('Cliente cadastrado com sucesso!')

def criar_conta():
    agencia = '0001'
    cpf = input('Digite o número do cpf (somente números): ')
    cliente = buscar_cliente_por_cpf(cpf)
    if not cliente:
        print('É necessário cadastrar o cliente para criar uma conta corrente!')
        return

    numero_conta = len(contas) + 1
    conta = {
        'numero_conta': numero_conta,
        'agencia': agencia,
        'cliente': cliente,
        'saldo': 0,
        'extrato': '',
        'numero_saques': 0
    }
    contas.append(conta)
    print(f'Conta corrente criada no cpf {cpf}')

def lista_clientes():
    print(f'Clientes:\n{clientes}')

def lista_contas():
    if not contas:
        print('Nenhuma conta encontrada!')
        return

    print('\nLISTA DE CONTAS')
    for conta in contas:
        cliente = conta['cliente']
        print(f'''
Agência : {conta['agencia']}
Número da conta: {conta['numero_conta']}
Cliente: {cliente['nome']}
CPF: {cliente['cpf']}
''')

def extrato():
    conta = selecionar_conta()
    if not conta:
        return

    print(f'\n==== EXTRATO ====\n{conta["extrato"]}\n== Saldo: R$ {conta["saldo"]:.2f} ==')

def buscar_cliente_por_cpf(cpf):
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            return cliente
    return None

def buscar_contas_por_cpf(cpf):
    return [conta for conta in contas if conta['cliente']['cpf'] == cpf]

def selecionar_conta():
    cpf = input('Digite o CPF do titular da conta: ')
    contas_do_cliente = buscar_contas_por_cpf(cpf)

    if not contas_do_cliente:
        print('Nenhuma conta encontrada para esse CPF.')
        return None

    if len(contas_do_cliente) == 1:
        return contas_do_cliente[0]

    print('Contas encontradas:')
    for conta in contas_do_cliente:
        print(f"Número: {conta['numero_conta']} - Agência: {conta['agencia']}")

    try:
        numero = int(input('Digite o número da conta que deseja acessar: '))
        for conta in contas_do_cliente:
            if conta['numero_conta'] == numero:
                return conta
        print('Número de conta inválido.')
    except ValueError:
        print('Entrada inválida.')

    return None

while True:
    try:
        operacao = int(input(menu))

        match operacao:
            case 1:
                deposito()
            case 2:
                saque()
            case 3:
                extrato()
            case 4:
                criar_cliente()
            case 5:
                criar_conta()
            case 6:
                lista_clientes()
            case 7:
                lista_contas()
            case 8:
                print('Saindo...')
                break
            case _:
                print('Operação inválida! Escolha uma opção do menu.')
    except ValueError:
        print('Entrada inválida! Digite um número do menu.')
