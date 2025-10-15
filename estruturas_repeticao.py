texto = input("informe o texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
print()

for tabuada in range(0, 51, 5):
    print(tabuada, end=" ")

opcao = -1
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n:"))
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("exibindo extrato...")

#imprimir somente numeros impares
for numero in range(0,100):
    if numero % 2 == 0:
        continue
    print(numero, end=" ")