print ("Solicitar a idade de várias pessoas e imprimir: Total de pessoas com menos de
21 anos. Total de pessoas com mais de 50 anos. O programa termina quando idade")
for = -99.
print ("me diga algumas idades e direi quantas pessoas tem menos de 21 e mais de 50 amos")
menor_21= 0
maior_50=0
while True:
    idade=int(input("me diga sua idade"))
    if idade == -99:
        print("voce escolheu sair")
        break
    elif idade< 21:
        menor21= menor_21+1
    if idade >50:
        maior_50=maior_50+1
print(f" o total de pessoas com idade menor que 21 é {menor_21} e pessoas com mais de 50 é de {maior_50}")