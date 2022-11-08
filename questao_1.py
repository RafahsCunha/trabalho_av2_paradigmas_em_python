

# 1 – Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
# taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de
# um item antes do imposto. A função "altera" o valor de custo para incluir o imposto sobre vendas. (0,5
# ponto).


def somaImposto(custoItem, taxaImposto):
    valorComImposto = custoItem + (custoItem * (taxaImposto / 100))
    return valorComImposto


custoItem = float(input("Digite o custo do item: "))
taxaImposto = float(input("Digite a taxa de imposto: "))

print("O valor total do item com imposto é: ",
      somaImposto(custoItem, taxaImposto))
