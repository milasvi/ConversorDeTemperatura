#ConversorDeTemperatura: Você foi viajar para um país estrangeiro
#e quer saber quantos graus estaria fazendo no Brasil:

medida = input('Bem-vinde ao conversor de temperaturas! \nVocê deseja converter:\n\nFahrenheit [1] \nKelvin[2]')
conversao = int

if medida == '1':
    print('Bem-vinde ao Conversor de Fahrenheit pra Celcius!')
    Temperatura = int(input('Quantos graus está fazendo aí?'))
    conversao = (Temperatura - 32) * 5 / 9
    print(f'Aí está fazendo {round(conversao,2)} graus celsius!')
    print('Obrigade por usar o Conversor de Temperatura! \nAté mais!')
if medida == '2':
    print('Bem vinde ao Conversor de Kelvin pra Celsius!')
    kelvin = int(input('Quantos graus está fazendo aí?'))
    conversao1 = kelvin - 273.15
    print(f'Aí está fazendo {round(conversao1, 2)} graus celsius!')
    print('Obrigade por usar o Conversor de Temperatura! \nAté mais!')