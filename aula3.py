filmes = ["Filme1", "Filme2", "Filme3", "Filme4", "Filme5"]

print("Bem-vindo(a), vamos classificar os filmes? \n")
print("Você irá classificar 5 filmes. \n")
print("A qualquer momento você pode sair digitando o número 0 \n")

for filme in filmes:
  #classificação do usuário
  classificacao = input(f"Como você classificaria '{filme}' de 1 a 5? (ou 0 para sair): ")

  #verificar se o usuário quer sair
  if classificacao == '0':
    print("Que pena que não irá classificar mais filmes.")
    break #encerrar loop

  #conversão para número inteiro
  classificacao = int(classificacao)

  #verificar se a classificacao está entre os números permitidos
  if classificacao > 5 or classificacao < 1:
    print("Por favor, insira uma classificação válida de 1 a 5.")
  else:
    #registre a classificacao e passe para o proximo filme
    print(f"Você classificou '{filme}' com '{classificacao}' estrelas. \n")
  
#mensagem de agradecimento ao finalizar
print("Obrigado por classificar os filmes!")