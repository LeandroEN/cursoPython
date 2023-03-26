"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = input('Digite seu nome: ')
preco = input('Digite o preço do produto: ')
saldo = input('Digite o saldo disponível: ')

preco_float = float(preco)
saldo_float = float(saldo)

print(preco_float)
print(saldo_float)

faltante = preco_float - saldo_float

possivelComprar = '%s, com o seu saldo atual de %.2f, é possível comprar o produto de valor %.2f' % (nome, saldo_float, preco_float)
naoPossivelComprar = '%s, com o seu saldo atual de R$%.2f, não é possível efetuar a compra. \nSão necessários R$%.2f para realizar a compra no valor de R$%.2f' % (nome, saldo_float, faltante, preco_float)

if saldo >= preco:
    print(possivelComprar)
else:
    print(naoPossivelComprar)