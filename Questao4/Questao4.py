# Variaveis globais
listaPecas = []
codigopeca = 0


def cadastrarpeca(codigo):
    print('Código da peça: {}' .format(codigo))
    peca = input("Digite o nome da peça: ")
    fabricante = input("Digite o nome do fabricante: ")
    valor = float(input("Digite o valor da peça: "))
    dicionariopeca = {'codigo': codigo, 'peca': peca, 'fabricante': fabricante, 'valor': valor}
    listaPecas.append(dicionariopeca.copy())


def consultapeca():
    while True:
        opcaodaconsulta = input('Digite a opção desejada: \n' +
                                'Digite 1 para consultar todas as peças \n' +
                                'Digite 2 para consultar por código \n' +
                                'Digite 3 para consultar por fabricante \n' +
                                'Digite 4 para voltar ao menu principal ')
        if opcaodaconsulta == '1':
            print('-------------------')
            for peca in listaPecas:
                for chave, valor in peca.items():
                    print('{}: {}' .format(chave, valor))
            print('-------------------')
            continue
        elif opcaodaconsulta == '2':
            codigodapeca = int(input('Digite o código da peça: '))
            for peca in listaPecas:
                if peca['codigo'] == codigodapeca:
                    print('-------------------')
                    for chave, valor in peca.items():
                        print('{}: {}' .format(chave, valor))
                    print('-------------------')
            continue
        elif opcaodaconsulta == '3':
            fabricantedapeca = input('Digite o nome do fabricante: ')
            for peca in listaPecas:
                if peca['fabricante'] == fabricantedapeca:
                    print('-------------------')
                    for chave, valor in peca.items():
                        print('{}: {}' .format(chave, valor))
                    print('-------------------')
            continue
        elif opcaodaconsulta == '4':
            print('Voltando ao menu principal')
            return
        else:
            print('Opção inválida')


def removepeca():
    while True:
        codigodapeca = int(input('Digite o código da peça que deseja remover: '))
        for peca in listaPecas:
            if peca['codigo'] == codigodapeca:
                listaPecas.remove(peca)
                return
            else:
                print('Peça não encontrada')


# Programa principal
print('Bem vindo ao controle de estoque da bicicletaria do Thiago Fortes')
while True:

    opcaoMenu = input('Digite a opção desejada: \n' +
                      'Digite 1 para cadastrar uma peça \n' +
                      'Digite 2 para consultar uma peça \n' +
                      'Digite 3 para remover uma peça \n' +
                      'Digite 4 para sair do programa ')

    if opcaoMenu == '1':
        codigopeca = codigopeca + 1
        cadastrarpeca(codigopeca)
    elif opcaoMenu == '2':
        consultapeca()
    elif opcaoMenu == '3':
        removepeca()
    elif opcaoMenu == '4':
        print('Obrigado por utilizar o programa')
        break
    else:
        print('Opção inválida')


cadastrarpeca()
consultapeca()
removepeca()
