nome = "Leandro EN"
altura = 1.68
peso = 95

imc = peso / ( altura ** 2 )
print(nome)
print("Seu IMC é de", imc)

print("Resultado: ")
if imc <= 18.5:  
    print("Magreza")
elif imc > 18.5 and imc <= 24.9:
    print("Normal")
elif imc > 24.9 and imc <= 29.9:
    print("Sobrepeso")
elif imc > 29.9 and imc <= 34.9:
    print("Obesidade Grau I")
elif imc > 34.9 and imc <= 39.9:
    print("Obesidade Grau II")
else:
    print("Obesidade Grau III")

