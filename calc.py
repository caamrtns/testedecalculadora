while True:
  print("******Calculadora Simples******* \n\n Verifique as opções \n 1.Adição \n 2.Subtração \n 3.Multiplicação \n 4.Divisão \n 5.Sair")
  opc = int(input("Digite a opção desejada: "))
  print('Ok, você escolheu a opção: ',opc)
  if opc==1:
    a = float(input('Digite o primeiro número: '))
    b = float(input('Digite o segundo número número: '))
    r=a+b
    print("o resultado é: ",r)
  elif opc==2:
    a = float(input('Digite o primeiro número: '))
    b = float(input('Digite o segundo número número: '))
    r=a-b
    print("o resultado é: ",r)
  elif opc==3:
    a = float(input('Digite o primeiro número: '))
    b = float(input('Digite o segundo número número: '))
    r=a*b
    print("o resultado é: ",r)
  elif opc==4:
    a = float(input('Digite o primeiro número: '))
    b = float(input('Digite o segundo número número: '))
    r=a/b
    print("o resultado é: ",r)
  elif opc==5:
    break
  else:
    print('digite uma opção valida')
