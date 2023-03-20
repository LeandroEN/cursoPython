numero1 = input('Digite o primeiro valor: ')
numero2 = input('Digite o segundo valor: ')

#numero1_float = float(numero1)
#numero2_float = float(numero2)

if numero1 > numero2:
    print(f'O numero1 "{numero1}" é maior que numero2 "{numero2}"')
elif numero1 < numero2:
    print(f'O numero2 "{numero2}" é maior que numero1 "{numero1}"')
else:
    print(f'Os valores de numero1 "{numero1}" e numero2 "{numero2}" são iguais')

#soma = numero1_float + numero2_float    
#print(f'A soma dos valores numero1 "{numero1}" e numero2 "{numero2}" é: {soma}')