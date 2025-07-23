"""
    2- Calculadora de Desconto
    Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

    * Nome do produto: "Camiseta"
    * Preço original: R$ 50.00
    * Porcentagem de desconto: 20%
    O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

produtoName = "Camiseta"
produtoPreco = 50.00
desconto = 0.8

print(f"Desconto: { (produtoPreco - (produtoPreco*desconto)):.2f}")
print(f"Valor final: { (produtoPreco*desconto):.2f}")