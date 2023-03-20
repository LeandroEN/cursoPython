nome = "Leandro EN"
altura = 1.68
peso = 95

imc = peso / ( altura ** 2 )

if imc <= 18.5:  
    linha3 = 'Magreza'
elif imc > 18.5 and imc <= 24.9:
    linha3 = 'Normal'
elif imc > 24.9 and imc <= 29.9:
    linha3 = 'Sobrepeso'
elif imc > 29.9 and imc <= 34.9:
    linha3 = 'Obesidade Grau I'
elif imc > 34.9 and imc <= 39.9:
    linha3 = 'Obesidade Grau II'
else:
    linha3 = 'Obesidade Grau III'

linha1 = f'{nome}, você está atualmente com {peso:.2f} Kg. '
linha2 = f'Seu IMC é de {imc:.2f} e você está:'

print(linha1)
print(linha2)
print(linha3)