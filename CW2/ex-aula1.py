# Lista de convidados
convidados = ("João", "Maria")

# Pessoas confirmadas
confirmados = ["Maria"]

# Chamamos a lista de convidados como convidado, e verificamos se o convidado não está na lista de confirmados, se não estiver irá adicionar a pessoa a lista de naoConfirmados
naoConfirmados = [convidado for convidado in convidados if convidado not in confirmados]

# Mostramos uma mensagem de pessoas que estão na lista de não confirmados
print("Convidados que ainda não confirmaram:")
for pessoa in naoConfirmados:
  print(pessoa)

print("Enviando lembrete para quem ainda não confirmou")