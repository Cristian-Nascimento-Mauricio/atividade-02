"""
    1- Conversor de Moeda
    Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

    * Valor em reais: R$ 100.00
    * Taxa do dólar: R$ 5.20
    * Taxa do euro: R$ 6.15
    O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""

real  = 100.0
dolar =  5.20
euro  =  6.15

print(f"Em dolar: {(real/dolar):.2f}")
print(f"Em euro: {(real/euro):.2f}")
