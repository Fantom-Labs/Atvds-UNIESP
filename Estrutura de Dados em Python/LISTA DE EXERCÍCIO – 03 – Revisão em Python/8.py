'''
8. Escreva um programa que converte uma temperatura em Celsius para Fahrenheit ou vice-versa,
dependendo da escolha do usuário.
'''

def celsius_para_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print("1 - Converter Celsius para Fahrenheit")
print("2 - Converter Fahrenheit para Celsius")
opcao = input("Escolha uma opção: ")

if opcao == "1":
    celsius = float(input("Digite a temperatura em Celsius: "))
    print(f"{celsius}°C = {celsius_para_fahrenheit(celsius):.2f}°F")
elif opcao == "2":
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    print(f"{fahrenheit}°F = {fahrenheit_para_celsius(fahrenheit):.2f}°C")
else:
    print("Opção inválida")
