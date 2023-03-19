nome = "Leandro EN"
altura = 1.68
peso = 95

imc = peso / ( altura ** 2 )

if(imc <= 18.5):  
    linha3 = 'Magro'
if(imc > 18.5 and imc <= 24.9):
    linha3 = 'Normal'
if(imc > 24.9 and imc <= 29.9):
    linha3 = 'Com Sobrepeso'
if(imc > 29.9 and imc <= 34.9):
    linha3 = 'Com Obesidade Grau I'
if(imc > 34.9 and imc <= 39.9):
    linha3 = 'Com Obesidade Grau II'
if(imc > 39.9):
    linha3 = 'Com Obesidade Grau III'

linha1 = f'{nome}, você está atualmente com {peso:.2f} Kg. '
linha2 = f'Seu IMC é de {imc:.2f} e você está:'

print(linha1)
print(linha2)
print(linha3)
