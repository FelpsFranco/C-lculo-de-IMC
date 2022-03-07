def calcula_imc(peso_imc, altura_imc):
    imc = peso_imc / (altura_imc ** 2)
    print('Seu IMC é: {:.2f}\n'.format(imc))
    op(imc)

def armazena_info():
    peso = float(input('Digite seu PESO em KG: '))
    altura = float(input('Digite sua ALTURA em METROS: '))
    if altura > 30:
        altura = altura / 100
    calcula_imc(peso, altura)

def info(indice_imc):
    print('INDICE DE IMC ')
    print('\t    IMC\t             |      Entre 18,5 e 24,9\t       |        Entre 25,0 e 29,9\t           |        Acima de 30,0\t       |       Maior que 40,0')
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('\tClassificação\t     |      Normal\t                   |          Sobrepeso\t                   |        Obesidade\t           |      Obesidade Grave\n\n\n')
    resultado(indice_imc)

def resultado(indice_imc):
    if indice_imc >= 18.5 and indice_imc <= 24.9:
        print('Seu Índice de Massa Corporal está NORMAL {:.2f}'.format(indice_imc))
    if indice_imc >= 25.9 and indice_imc <= 29.9:
        print('Cuidado de Acordo com seu Índice de Massa Corporal {:.2f}, você está com SOBREPESO! '.format(indice_imc))
    if indice_imc >= 30.0 and indice_imc <= 39.9:
        print('É melhor começar uma Dieta, de acordo com seu Índice de Massa Corporal {:.2f}, você está com OBESIDADE!'.format(indice_imc))
    if indice_imc >= 40.0:
        print('É melhor procurar um Médico, de acordo com seu Índice de Massa Corporal {}:.2f, você está com OBESIDADE GRAVE!'.format(indice_imc))

    op = input(('\nDeseja Calcular novamente?\n'
                '1 - Sim\n'
                '2 - Não\n'))
    if op == '1' or op == 'Sim' or op == 'sim':
        armazena_info()
    else:
        print('Obrigado por utilizar nosso sistema!')

def op(imc_calculado):
    imc = imc_calculado

    opera = input(('Deseja saber mais sobre o seu IMC?\n'
                '1 - Sim\n'
                '2 - Não\n'))

    if opera == '1' or opera == 'Sim' or opera == 'sim':
        info(imc)
    else:
        print('\nFINALIZANDO!')





armazena_info()
