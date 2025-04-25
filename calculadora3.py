print("Seja Bem-Vindo")

inicio = input("para começar pressione a tecla C ")



for C in inicio:

    while True:
        print("Vamos iniciar, caso queira sair escreva exit")

        operador = input("Qual operação deseja realizar ? ")
        
        if operador == "exit":
            print("Saindo...")
            break
        else:
              print("Não entendi a operação, repita novamente")
              

        if operador == "+":
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Informe o numero que deseja Somar "))
            print(numero1 + numero2)
        elif operador == "-":
                numero1 = float(input("Digite o primeiro número: "))
                numero2 = float(input("Informe o numero que deseja subtrair "))
                print(numero1 - numero2)
        elif operador == "*":
                numero1 = float(input("Digite o primeiro número: "))
                numero2 = float(input("Informe o numero que deseja multiplicar "))
                print(numero1 * numero2)

        elif operador == "/":
                numero1 = float(input("Digite o primeiro número: "))
                numero2 = float(input("Informe o numero que deseja dividir "))
                print(numero1 / numero2)
        else:
              print("Operação invalida")

        print("\n")    
