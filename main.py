## Alunos: Gabrielle Louise Ferreira de Melo e Thomas Rempel

pergunta1 = input("Voce prefere comer fora ou cozinhar? ")


if (pergunta1 == "cozinhar"):

  #variaveis
  sobremesa = "sobremesa"
  PratoSalgado = "prato salgado"
  chocolate = "chocolate"
  semchocolate = "sem chocolate"
  sim = ("sim")
  nao = ("não")
  Claro = ("Claro")
  Nem = ("Nem") 
  carne = ("com carne")
  sem = ("sem")
  pergunta3 = input("Você está mais a fim de comer uma sobremesa ou um prato salgado ?")

  if (pergunta3 == "sobremesa"):
      opcao_chocolate = input("Escolha: chocolate ou sem chocolate: ")
      if opcao_chocolate == (chocolate):
        opcao_bebida = input("Bebida? Responda com Sim ou Não!!")
        if opcao_bebida == (sim):
          print("Se está um dia quente é uma boa opção um Milkshake, mas se está frio, recomendamos um Chocolate Quente")
        elif opcao_bebida == (nao):
          print("Achamos que uma boa opção é um bolo de chocolate com brigadeiro de chocolate por cima")
        else:
            print("responda apenas com Sim ou Não: ")
      if opcao_chocolate == (semchocolate):
          opcao_comida = input("Fruta? Responda com Claro ou Nem!! ")
          if opcao_comida == (Claro):
            print("Se você souber e tiver paciência de fazer uma Marta Rocha, é uma otima opção")
          elif opcao_comida == (Nem):
            print("Um Pudim de leite é simples, rapido e gostoso")
          else:
            print("responda apenas com as opções dadas!! ")
  elif (pergunta3 == PratoSalgado):
    opcao_carne = input("Escolha: entre com carne ou sem ? ")
    if opcao_carne == (carne):
      print("Uma boa opção barata é uma paleta suina ao molho de mostarda e mel ")
    elif opcao_carne == (sem):
      print("estrogonoff de grão de bico é um prato muito bom para quem é vegetariano ou vegano")
    else:
        print("Responda: com carne ou sem")
  else:
    ("responda apenas com sobremesa ou prato salgado")

elif (pergunta1 == "comer fora"):
  #variaveis
  A = "italiana"
  B = "japonesa"
  C = "fast food"
  pizza = ("pizza")
  macarrao = ("macarrao")
  rodizio = ("rodizío")
  alaCarte = ("à la Carte")
  hamburguer = ("hamburguer")
  arabe = ("arabe")
  mexicana = ("mexicana")
  pergunta2 = input("Responda qual tipo de comida: A (italiana) B (japonesa) C (fast food): ")

  if pergunta2 == "A": 
    perguntaitaliana = input("Esta mais a fim de pizza ou macarrao ? ")
    if perguntaitaliana == pizza:
        print(" Uma ótima opção seria o Pizza Hut")
    elif perguntaitaliana == macarrao:
        print(" Um bom macarrão em Curitiba é um Madalosso")
    else:
        print("responda apenas com as opções acima")

  if pergunta2 == "B":
    perguntajaponesa = input("Hoje você está mais a fim de comer rodízio, ou à la Carte ? ")
    if perguntajaponesa == rodizio:
        print(" Um boa opção seria o restaurante MIYO")
    elif perguntajaponesa == alaCarte:
        print("Vá ao KARE YA que você vai gostar muito")
    else:
        print("responda com as opções acima")


  if pergunta2 == "C":
    perguntafastfood = input("Você esta mais a fim de comer: hamburguer, arabe ou mexicana ? ")
    if perguntafastfood == hamburguer:
        print("Vá ao Burguer King ou McDonald's")
    elif perguntafastfood == arabe:
        print("Se for no Habib's que você irá amar")
    elif perguntafastfood == mexicana:
        print("Zappata é a melhor opção que você pode ir hoje")
    else:
        print("responda com as opção acima")
      

else:
  print("responda apenas cozinhar ou comer fora!")
