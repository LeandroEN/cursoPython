a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)
print(formato)


nome = 'Amber'
idade = 23
altura = 1.55

fraseTeste = 'Nome: {}, {} anos de idade, altura de {}'.format(nome, idade, altura)

print(fraseTeste)




Au = 'ouro'
Ag = 'prata'
Cu = 'cobre'
Pt = 'platina'

metal = 'Alguns metais: {metal1} {metal2} {metal3} {metal4}'
metais = metal.format(
    metal1 = Pt, metal2 = Au, metal3 = Ag, metal4 = Cu
)
print(metal)