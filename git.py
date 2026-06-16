def ler_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro: digite um número inteiro válido.")


def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: digite um número válido.")


def calcular_total():
    quantidade_produtos = ler_int("Quantidade de produtos: ")
    total = 0

    for i in range(quantidade_produtos):
        print(f"\nProduto {i + 1}")

        nome = input("Nome do produto: ")

        preco = ler_float("Preço: R$ ")
        while preco < 0:
            print("O preço não pode ser negativo.")
            preco = ler_float("Preço: R$ ")

        quantidade = ler_int("Quantidade: ")
        while quantidade < 0:
            print("A quantidade não pode ser negativa.")
            quantidade = ler_int("Quantidade: ")

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
    cliente = input("\nNome do cliente: ").strip()

    if not cliente:
        print("Nome do cliente não pode ficar vazio.")
        continue

    total = calcular_total()
    desconto = calcular_desconto(total)

    exibir_resumo(cliente, total, desconto)

    while True:
        continuar = input("\nNova venda? (S/N): ").strip().upper()

        if continuar in ("S", "N"):
            break

        print("Erro: digite apenas S ou N.")

    if continuar == "N":
        print("Sistema encerrado.")
        break