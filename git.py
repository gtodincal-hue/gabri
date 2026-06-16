# funções
def calcular_total():
    n = int(input("quantidade de produtos: "))
    total = 0

    for i in range(n):
        print("\nproduto", i + 1)
        nome_=input("nome desse produto:")
        preco = float(input("preço: "))
        qtd = int(input("quantidade: "))

        total += preco * qtd

    return total


def calcular_desconto(total):
    if total >= 500:
        return total * 0.10
    elif total >= 200:
        return total * 0.05
    else:
        return 0
# codigo 
nova_compra = True
while nova_compra == True:
    cliente = input("\nnome do cliente: ")

    total = calcular_total()
    desconto = calcular_desconto(total)
    total_final = total - desconto

    print("\n--- RESUMO ---")
    print("cliente:", cliente)
    print("total:", round(total, 2))
    print("desconto:", round(desconto, 2))
    print("total final:", round(total_final, 2))
    continuarcompra = input("nova venda? (S/N): ").upper()
# nova compra 
    if continuarcompra == "N":
        nova_compra = False
    
    elif continuarcompra == "S":
        print("nova venda:")
        nova_compra = True

