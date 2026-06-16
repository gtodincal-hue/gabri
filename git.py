def calcular_total():
    quantidade_produtos = int(input("Quantidade de produtos: "))
    total = 0

    for i in range(quantidade_produtos):
        print(f"\nProduto {i + 1}")

        nome = input("Nome do produto: ")
        preco = float(input("Preço: R$ "))
        quantidade = int(input("Quantidade: "))

        subtotal = preco * quantidade
        total += subtotal

        print(f"Subtotal de {nome}: R$ {subtotal:.2f}")

    return total


def calcular_desconto(total):
    if total >= 500:
        return total * 0.10
    elif total >= 200:
        return total * 0.05
    return 0


def exibir_resumo(cliente, total, desconto):
    total_final = total - desconto

    print("\n" + "=" * 30)
    print("RESUMO DA VENDA")
    print("=" * 30)
    print(f"Cliente: {cliente}")
    print(f"Total: R$ {total:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Total Final: R$ {total_final:.2f}")
    print("=" * 30)


# Programa principal
while True:
    cliente = input("\nNome do cliente: ")

    total = calcular_total()
    desconto = calcular_desconto(total)

    exibir_resumo(cliente, total, desconto)

    continuar = input("\nNova venda? (S/N): ").strip().upper()

    if continuar != "S":
        print("Sistema encerrado.")
        break