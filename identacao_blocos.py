def sacar(valor):
    saldo = 200
    if saldo >= valor:
        print("valor sacado")
        print("retire seu dinheiro na boca do caixa")

def depositar(valor):
    saldo = 500
    saldo += valor
    print("valor depositado")
    
print("Obrigado por ser nosso cliente, tenha um bom dia!")
    


sacar(100)
depositar(1000)