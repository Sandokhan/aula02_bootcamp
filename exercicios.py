# #### Inteiros (`int`)

# # 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# print(f"A soma dos números é: {num1 + num2}")
# # 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# num = int(input("Digite um número: "))
# print(f"O resto da divisão por 5 é: {num % 5}")
# # 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# print(f"A soma dos números é: {num1 * num2}")
# # 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# print(f"A Divisão dos números é: {num1 // num2}")
# # 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# num = int(input("Digite um número: "))
# print(f"O quadrado do número é: {num ** 2}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))
# print(f"A soma dos números é: {num1 + num2}")
# # 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))
# print(f"A média dos números é: {(num1 + num2) / 2}")
# # 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# num1 = float(input("Digite a base: "))
# num2 = float(input("Digite o expoente: "))
# print(f"A média dos números é: {num1 ** num2}")
# # 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# c = float(input("Digite a temperatura em Celsius: "))
# print(f"A temperatura em Fahrenheit é: {(c * 1.8) + 32}")
# # 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# r = float(input("Digite o raio do círculo: "))
# print(f"A área do círculo é: {3.14 * r ** 2}")

# #### Strings (`str`)

# # 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# string = input("Digite uma string: ")
# print(f"A string em maiúsculas é: {string.upper()}")
# # 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# nome = input("Digite seu nome completo: ")
# print(f"Seu nome em minúsculas é: {nome.lower()}")
# # 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# frase = input("Digite uma frase: ")
# print(f"A frase sem espaços em branco é: {frase.strip()}")
# # 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data = input("Digite uma data no formato 'dd/mm/aaaa': ")
# print(f"O dia é: {data.split("/")[0]}")
# print(f"O mês é: {data.split("/")[1]}")
# print(f"O ano é: {data.split("/")[2]}")
# # 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# string1 = input("Digite a primeira string: ")
# string2 = input("Digite a segunda string: ")
# print(f"A concatenação das strings é: {string1 +" "+ string2}")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# try:
#     c = float(input("Digite a temperatura em Celsius: "))
#     print(f"A temperatura em Fahrenheit é: {(c * 1.8) + 32}")
# except ValueError:
#     print("Por favor, informe um inteiro para temperatura")
# 22: Verificador de Palíndromo
# palavra = input("Digite uma palavra ou frase: ")
# word = palavra.replace(" ", "").lower()
# if isinstance(word, str):
#     if word == word[::-1]:
#         print("A palavra é um palíndromo")
#     else:
#         print("A palavra não é um palíndromo")
# else:
#     print("Por favor, informe uma string")
# 23: Calculadora Simples
# try:
#     num1 = float(input("Digite o primeiro número: "))
#     num2 = float(input("Digite o segundo número: "))
#     operacao = input("Digite a operação desejada (+, -, *, /): ")
#     while operacao not in ["+", "-", "*", "/"]:
#         operacao = input("Operação inválida. Digite a operação desejada (+, -, *, /): ")
#     if operacao == "+":
#         print(f"A soma dos números é: {num1 + num2}")
#     elif operacao == "-":
#         print(f"A subtração dos números é: {num1 - num2}")
#     elif operacao == "*":
#         print(f"A multiplicação dos números é: {num1 * num2}")
#     elif operacao == "/":
#         if num2 == 0:
#             print("Não é possível dividir por zero")
#         else:
#             print(f"A divisão dos números é: {num1 / num2}")
# except ValueError:
#     print("Por favor, informe um número para a operação")
# 24: Classificador de Números
try:
    number = float(input("Digite um número: "))
    is_even = 'e par' if number % 2 == 0 else 'e ímpar'
    if number > 0:
        print(f"O número é positivo {is_even}.")
    elif number < 0:
        print(f"O número é negativo {is_even}.")
    else:
        print("O número é zero.")
except ValueError:
    print("Por favor, informe um número.")
# 25: Conversão de Tipo com Validação
