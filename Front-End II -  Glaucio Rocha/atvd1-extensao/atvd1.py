mcontador = 0
fcontador = 0
alturasmall = 0
alturabig = 0

for i in range (15):
    altura = float(input("Digite sua altura: "))
    genero = input("Digite seu gênero (M ou F): ")
    if genero == "M":
        mcontador = mcontador + 1
    elif genero == "F":
        fcontador = fcontador + 1
    if altura > alturabig:
        alturabig = altura
    elif alturasmall == 0:
        alturasmall = altura
    elif altura < alturasmall:
        alturasmall = altura


print("Número de mulheres:", fcontador)
print("Número de homens: ", mcontador)
print("Menor altura é: ", alturasmall)
print("Maior altura é:", alturabig )



