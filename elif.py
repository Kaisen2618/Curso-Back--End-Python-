idade = int(input("digite sua idade"))

if idade> 15 and idade < 18 or idade > 70:
  print("o visto é opcional")
elif idade < 18:
  print("voce nao pode votar")
else:
   print("voce é obrigado a votar")