# Melhoria do código da aula 2


# Matriz de filmes
filmes = ["Turma da Mônica: Laços", "As Branquelas", "Matrix"]


# Mensagem inicial
print("Espero que tenha gostado do filme!! \n")
print("O que acha de classifica-lo? \n")
print("VocÊ vai classificar o filme de 1 a 5 (Caso queira sair digite 0) \n")


# Loop baseado na matriz
for filme in filmes:

  # Adicionando a classificação do filme a variável
  classificacao = input(f"Qual a classificação para o filme '{filme}'")

  # Adicionando a condição caso a pessoa queira sair
  if classificacao == '0':
    print("Obrigado pela classificação!")
    break
  
  # Transformando classificação em um número inteiro
  classificacao = int(classificacao)

  # Condição caso a pessoa escolha números acima ou abaixo do estipulado
  if classificacao > 5 or classificacao < 1:
    print("Digite um valor válido de 1 a 5")
  
  # Caso seja dentro do estipulado ele funcionará corretamente
  else: 
    print(f"Você classificou o filme '{filme}' com a classificação '{classificacao}' estrelas")
print("Obrigado por classificar os filmes!")

  
  