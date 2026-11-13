opcao=-1

while (opcao!=0):
    print("Escolha uma opcao:")
    print("1.administracao")
    print("2.companhia")
    print("3.passageiro")
    print("0.sair")
    opcao=input("a sua opcao")
    if (opcao.isnumeric()):
            opcao = int(opcao)
    else: 
          print("o valor a ser inserido precisa ser numerico") 
          continue
    
    if opcao == 0:
        print("opcao valida")
        

    elif opcao==1:
        print("opcao valida")

    elif opcao==2:
        print("opcao valida")

    elif opcao==3: 
     print("opcao valida")

    elif opcao > 4 or opcao < 0 :
        print("Opcao invalida")
menu={"administracao"}



   