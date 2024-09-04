idade = int(input("Por favor, insira sua idade: "))

# Conferência de idade

if idade < 12:
  print("Recomendamos o filme infantil: 'Turma da Mônica: Laços'")
elif 12 <= idade < 18:
  print ("Recomendamos o filme adolescente: 'As Branquelas'")
else:
  print("Recomendamos o filme adulto: 'Matrix'")

# Conferência de ingressos

ingressos = 0

if ingressos > 0:
  print("Ingressos disponíveis, bom filme.")
else:
  print("Ingressos indisponíveis, tente novamente em outro momento.")


