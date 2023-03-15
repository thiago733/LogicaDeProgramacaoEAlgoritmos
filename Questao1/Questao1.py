print('Bem Vindo a loja do Thiago Fortes')
#Insere o valor do produto
valorDoProduto = float(input('Entre com o valor do produto: '))
#Insere a quantidade do produto
quantidadeDoProduto= int(input('Entre com a valor da quantidade: '))
#Calcula o subtotal da compra
subTotal = valorDoProduto * quantidadeDoProduto
#Calcula o desconto conforme a quantidade do produto
if  quantidadeDoProduto >= 1000:
    totalComDesconto = subTotal - (subTotal * (15 / 100))
    valorDoDesconto = 15

elif 100 <= quantidadeDoProduto <= 999:
    totalComDesconto = subTotal - (subTotal * (10 / 100))
    valorDoDesconto = 10

elif 10 <= quantidadeDoProduto <= 99:
    totalComDesconto = subTotal - (subTotal * (5 / 100))
    valorDoDesconto = 5

else:
    totalComDesconto = subTotal
    valorDoDesconto = 0
#Imprime o valor da compra original e com o desconto caso exista
print('O valor sem desconto foi: R$ {:.2f}' .format(subTotal))
print('O valor com desconto foi: R$ {:.2f}. (Desconto de {}%)' .format(totalComDesconto,valorDoDesconto))