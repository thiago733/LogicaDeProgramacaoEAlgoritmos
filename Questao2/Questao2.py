#exibindo o menu
print('Bem vindo a lanchonete do Thiago Fortes')
print('******************* Cardápio *******************')
print('|Código|       Descrição                 |Valor|')
print('| 100  |       Cachorro Quente           | 9,00|')
print('| 101  |       Cachorro Quente Duplo     |11,00|')
print('| 102  |       X-Egg                     |12,00|')
print('| 103  |       X-Salada                  |12,00|')
print('| 104  |       X-Bacon                   |14,00|')
print('| 105  |       X-Tudo                    |17,00|')
print('| 200  |       Refrigerante Lata         | 5,00|')
print('| 201  |       Chá Gelado                | 4,00|')

#iniciando variaveis
subTotal = 0
valorDoProduto = 0

#fazendo os pedidos
while True:

    codigoDoProduto = int(input('Entre com o código desejado: '))
    if  codigoDoProduto == 100:
        valorDoProduto = 9.00
        subTotal = valorDoProduto + subTotal
        print(subTotal)

    elif  codigoDoProduto == 101:
          valorDoProduto = 11.00
          subTotal = valorDoProduto + subTotal
          print(subTotal)

    elif  codigoDoProduto == 102:
          valorDoProduto = 12.00
          subTotal = valorDoProduto + subTotal
          print(subTotal)

    elif  codigoDoProduto == 103:
          valorDoProduto = 13.00
          subTotal = valorDoProduto + subTotal
          print(subTotal)

    elif  codigoDoProduto == 104:
          valorDoProduto = 14.00
          subTotal = valorDoProduto + subTotal
          print(subTotal)

    elif  codigoDoProduto == 105:
          valorDoProduto = 17.00
          subTotal = valorDoProduto + subTotal
          print(subTotal)

    elif  codigoDoProduto == 200:
          valorDoProduto = 5.00
          subTotal = valorDoProduto + subTotal
          print(subTotal)

    elif  codigoDoProduto == 201:
          valorDoProduto = 4.00
          subTotal = valorDoProduto + subTotal
          print(subTotal)

    else:
        print('Opção inválida')
#verficando se o cliente quer adicionar mais produtos
    print('Deseja pedir mais alguma coisa?')
    print('1 - Sim')
    print('0 - Não')
    continuarPedido = input()
    if  continuarPedido == '1':
        continue
#exibindo o total da compra
    else:
        print('O total a ser pago é: R${:.2f}' .format(subTotal))
        break
