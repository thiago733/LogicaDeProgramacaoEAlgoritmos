#Função para calcular o volume
def dimensoesobjeto():
    while True:
        try:
            comprimento = int(input('Insira o comprimento em cm: '))
            largura = int(input('Insira a largura em cm: '))
            altura = int(input('Insira a altura em cm: '))
            volume = comprimento * largura * altura

            if 1 <= volume < 1000:
                subtotalvolume = 10
            elif 1000 <= volume < 10000:
                subtotalvolume = 20
            elif 10000 <= volume < 30000:
                subtotalvolume = 30
            elif 30000 <= volume < 100000:
                subtotalvolume = 50
            else:
                print('O volume não pode ser maior que 100.000 cm³')
                continue

            print('O volume do objeto em cm³ é: {:.1f}'.format(volume))
            return subtotalvolume
        except ValueError:
            print('Valor inválido')

#Função para calcular o peso
def pesoobjeto():
    while True:
        try:
            peso = int(input('Insira o peso em kg: '))
            if 0.1 > peso:
                multiplicadorpeso = 1
            elif 0.1 <= peso < 1:
                multiplicadorpeso = 1.5
            elif 1 <= peso < 10:
                multiplicadorpeso = 2
            elif 10 <= peso < 30:
                multiplicadorpeso = 3
            else:
                # peso > 30
                print('O peso não pode ser maior que 30kg')
                continue

            return multiplicadorpeso
        except ValueError:
            print('Valor inválido')

#Função para calcular a rota
def rotaobjeto():
    while True:
        try:
            print('Selecione a rota: \n' +
                  'RS - De Rio de Janeiro até São Paulo \n' +
                  'SR - De São Paulo até Rio de Janeiro \n' +
                  'BS - De Brasília até São Paulo \n' +
                  'SB - De São Paulo até Brasília \n' +
                  'BR - De Brasília até Rio de Janeiro \n' +
                  'RB - De Rio de Janeiro até Brasília')

            rota = input('Insira a rota: ')

            if rota == 'RS':
                multiplicadorrota = 1

            elif rota == 'SR':
                multiplicadorrota = 1

            elif rota == 'BS':
                multiplicadorrota = 1.2

            elif rota == 'SB':
                multiplicadorrota = 1.2

            elif rota == 'BR':
                multiplicadorrota = 1.5

            elif rota == 'RB':
                multiplicadorrota = 1.5

            else:
                print('Rota inválida')
                continue

            return multiplicadorrota
        except ValueError:
            print('Entre com a rota novamente')

#Programa principal
print('Bem Vindo a companhia de logística do Thiago Fortes')
volumeDoObjeto = dimensoesobjeto()
pesoDoObjeto = pesoobjeto()
rotaEscolhida = rotaobjeto()
#Calcula o total a pagar
total = volumeDoObjeto * pesoDoObjeto * rotaEscolhida
print('O total a pagar é de: R$ {:.2f} (volume: {} * peso: {} * rota: {})'
      .format(total, volumeDoObjeto, pesoDoObjeto, rotaEscolhida))
