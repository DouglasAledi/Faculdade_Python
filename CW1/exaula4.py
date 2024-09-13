# Melhorando o exercício da aula 1

nota1 = int(input("Escreva a nota da primeira prova: "))
nota2 = int(input("Escreva a nota da segunda prova: "))
nota3 = int(input("Escreva a nota da terceira prova: "))
nota4 = int(input("Escreva a nota da quarta prova: "))

#definimos a função

def media (nota1, nota2, nota3, nota4):
  soma = sum(nota1, nota2, nota3, nota4)
  calculoMedia = soma/4
  return calculoMedia

# Chamamos a função
mediaFinal = media(nota1, nota2, nota3, nota4)

# Exibindo a média
# :.2f irá mostrar duas casas decimais OU poderiamos usar round(media, 2)
print(f"Sua média foi: {mediaFinal:.2f}")

if mediaFinal > 6:
  print("Parabéns, você passou!!")
else:
  print("Infelizmente você não passou..")
