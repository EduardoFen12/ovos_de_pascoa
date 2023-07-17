# OVOS DE PÁSCOA:

print("--------------------------------------------------------------------------    ")
print("|                                                                        |    ")
print("|                              OPÇÕES DE OVOS                            |    ")
print("|                                                                        |    ")
print("| SIMPLES      (A): com valor unitário de R$12.00, limite por pedido 50. |    ")
print("| RECHEADO     (B): com valor unitário de R$15.50, limite por pedido 30. |    ")
print("| COM SURPRESA (C): com valor unitário de R$21.30, limite por pedido 20. |    ")
print("|                                                                        |    ")
print("--------------------------------------------------------------------------    ")

tipo = input("    Digite o tipo do ovo desejado: ")
quantidade = int(input("    Digite a quantidade desejada: "))

erro = False

if quantidade <= 0:
    erro = True
    print("    Quantidade de ovos inválida!")

match tipo:
    case 'A' | 'a':
        valor = float(12)
        if quantidade > 0:
            if quantidade > 50:
                quantidade = 50
            print(f"    Você selecionou {quantidade} ovo(s) SIMPLE(S)!")
    case 'B' | 'b':
        valor = float(15.50)
        if quantidade > 0:
            if quantidade > 30:
                quantidade = 30
            print(f"    Você selecionou {quantidade} ovo(s) RECHEADO(S)!")
    case 'C' | 'c':
        valor = float(21.30)
        if quantidade > 0:
            if quantidade > 20:
                quantidade = 20
            print(f"    Você selecionou {quantidade} ovo(s) COM SURPRESA!")
    case _:
        erro = True
        print("    Produto Inválido!")
        print("    (tipos validos: 'A', 'B', 'C')")

if not erro:
    resultado = quantidade * valor
    print(f"    O valor Total da sua compra é: R${resultado:.2f}")
