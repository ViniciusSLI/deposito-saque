saldo = 200.0

def sacar(valor):
    global saldo
    if valor <= saldo:
        saldo -= valor
        print("Saque de R$ {:.2f} realizado com sucesso.".format(valor))
    else:
        print("Saldo insuficiente.")

def depositar(valor):
    global saldo
    saldo += valor
    print("Depósito de R$ {:.2f} realizado com sucesso.".format(valor))

opcao = input("Você deseja sacar (S) ou depositar (D)? ").upper()

if opcao == "S":
    valor_saque = float(input("Informe o valor que deseja sacar: "))
    sacar(valor_saque)
elif opcao == "D":
    valor_deposito = float(input("Informe o valor que deseja depositar: "))
    depositar(valor_deposito)
else:
    print("Opção inválida.")

print("Seu novo saldo é de R$ {:.2f}".format(saldo))
