while True:
      resposta = input("deseja sair do programa(s/n)")
      if resposta.lower() == "s":
          print("saindo do programa")
          break
      elif resposta.lower() =="n":
          print("aguardo a tua vontade...")
      else:
            print("opção inválida, por favor escolha uma resposta")