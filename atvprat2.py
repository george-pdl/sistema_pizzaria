print("Bem-Vindo a Pizzaria do Fulano!\n")
print("---------------- >> CARDÁPIO << --------------------")
print("| Código |   Sabor    | Pizza Média | Pizza Grande |")
print("|--------|------------|-------------|--------------|")
print("|   21   | Napolitana |   R$ 20,00  |    R$ 26,00  |")
print("|   22   | Margherita |   R$ 20,00  |    R$ 26,00  |")
print("|   23   | Calabresa  |   R$ 25,00  |    R$ 32,50  |")
print("|   24   | Toscana    |   R$ 30,00  |    R$ 39,00  |")
print("|   25   | Portuguesa |   R$ 30,00  |    R$ 39,00  |")
print("----------------------------------------------------")
subtotal = 0  # Guardará e somará os valores das pizzas desejadas

while True:  # Cria o looping necessário para o cliente efetuar os pedidos
    tam = input("Qual é o tamanho desejado para a pizza? (M/G): ")
    if tam == "M":
        sabor = input("Digite o Código do sabor desejado: ")
        if sabor == "21":
            subtotal = subtotal + 20
            print("Você pediu uma Pizza Napolitana!")
        elif sabor == "22":
            subtotal = subtotal + 20
            print("Você pediu uma Pizza Margherita!")
        elif sabor == "23":
            subtotal = subtotal + 25
            print("Você pediu uma Pizza Calabresa!")
        elif sabor == "24":
            subtotal = subtotal + 30
            print("Você pediu uma Pizza Toscana!")
        elif sabor == "25":
            subtotal = subtotal + 30
            print("Você pediu uma Pizza Portuguesa!")
        else:
            print("Opção Inválida!")
            continue

    elif tam == "G":
        sabor = input("Digite o Código do sabor desejado: ")
        if sabor == "21":
            subtotal = subtotal + 26
            print("Você pediu uma Pizza Napolitana!")
        elif sabor == "22":
            subtotal = subtotal + 26
            print("Você pediu uma Pizza Margherita!")
        elif sabor == "23":
            subtotal = subtotal + 32.50
            print("Você pediu uma Pizza Calabresa!")
        elif sabor == "24":
            subtotal = subtotal + 39
            print("Você pediu uma Pizza Toscana!")
        elif sabor == "25":
            subtotal = subtotal + 39
            print("Você pediu uma Pizza Portuguesa!")
        else:
            print("Opção Inválida!")
            continue
    else:
        print("Opção Inválida!")
        continue
    validade = int(input("Deseja pedir mais Pizzas?\n"
                         "1 - SIM\n"
                         "0 - NÃO\n"
                         ">> "))
    if validade == 0:
        break
print("O Valor Total a ser pago é: R$%.2f\nPor gentileza, dirija-se ao Caixa para efetuar o Pagamento!" % subtotal)
