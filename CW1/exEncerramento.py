print("Seja bem-vindo(a) à calculadora de descontos \n")

# Recebe o valor da compra e o desconto como números (float)
valor = float(input("Insira o valor da compra: "))
descontoPorcentagem = float(input("Insira o desconto oferecido (em %): "))

# Função para calcular o valor final com desconto
def calculoDesconto(valor, descontoPorcentagem):
    desconto = descontoPorcentagem / 100  # Calcula a fração do desconto
    valorFinal = valor - (valor * desconto)  # Aplica o desconto
    return valorFinal

if descontoPorcentagem > 100 or descontoPorcentagem < 0:
  print("Erro: valor muito alto ou muito baixo")
else:
   # Chama a função para calcular o valor final com desconto
  novoValor = calculoDesconto(valor, descontoPorcentagem)

  # Exibe os resultados
  print(f"\nO valor original é: R$ {valor:.2f}")
  print(f"O desconto é de: {descontoPorcentagem}%")

  print(f"O valor com o desconto é de: R$ {novoValor:.2f}")