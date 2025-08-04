import time as t

def soma(a,b):
  return a + b

def diferenca(a,b):
  return a - b 

def multiplicacao(a,b):
  return a * b

def divisao(a,b):
  if b == 0:
    return 'Erro, não se pode dividir por zero'
  return a / b

def radiciacao(a,b):
  return a ** (1/b)

def expoente(a,b):
  return a ** b

memoria = []

while True:
  opcao = input("""Escolha sua opção: \n
  1 - Soma\n
  2 - Subtração\n
  3 - Multiplicação\n
  4 - Divisão\n
  5 - Radiciação\n
  6 - Exponenciação\n
  7 - Memoria\n
  8 - Sair\n
  9 - Dominar o mundo (em teste)\n> """).strip()

  if opcao == '8':
    print('Saindo da calculadora...')
    t.sleep(1)
    print('Até logo!')
    break

  if opcao == '9':
    print('MUAHAHAHA 😈 DOMINANDO O MUNDO EM:')
    print('3')
    t.sleep(1)
    print('2')
    t.sleep(1)
    print('1')
    print('Mas aí os gatinhos também morrem... Não vou fazer isso. 🐈s2')
    continue

  if opcao == '7':
    if not memoria:
      print("Memória vazia.")
    else:
      for i, resp in enumerate(memoria, 1):
        print(f'{i}: {resp}')
    continue

  if opcao not in ["1", "2", "3", "4", "5", "6"]:
    print("Opção inválida.")
    continue

  try:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
  except ValueError:
    print("Entrada inválida.")
    continue

  if opcao == '1':
    resultado = soma(a, b)
  elif opcao == '2':
    resultado = diferenca(a, b)
  elif opcao == '3':
    resultado = multiplicacao(a, b)
  elif opcao == '4':
    resultado = divisao(a, b)
  elif opcao == '5':
    resultado = radiciacao(a, b)
  elif opcao == '6':
    resultado = expoente(a, b)

  print(f"Resultado: {resultado}")
  memoria.append(resultado)
