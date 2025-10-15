#if/else
saldo = 2000
saque = float(input("informe o valor do saque: "))
if saldo >= saque:
    print("Realizando saque!")
else:
    print("saldo insuficiente")
#if/elilf/else 
opcao = int(input("Informe a opcao: [1] Sacar \n[2] Extrato: "))
if opcao == 1:
    valor = float(input("Informe a quantia para o sauqe: "))
elif opcao == 2:
    print("Exibindo extrato...")
else:
    print("Opção invalida")
#if aninhado
conta_normal = True
conta_universitaria = True
cheque_especial = 2000
if conta_normal:
    if saldo > saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

#if ternario
status = "Sucesso" if saldo>= saque else "Falha"
print(f"{status} ao realizar o saque!")
