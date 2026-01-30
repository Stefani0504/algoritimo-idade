'''
Seu desafio é receber o valor do IMC pelo usuário e imprimir a classificação correta:
 
Faixa de IMC	  Classificação
Abaixo de 18.5	 Abaixo do peso
De 18.5 até 24.9    Peso normal
De 25 até 29.9	  Sobrepeso
De 30 até 39.9	  Obesidade
Acima de 40	     Obesidade grave
 
✅ Critérios para o desafio estar completo:
O código deve utilizar input() para receber o valor do IMC.
Deve conter uma estrutura if, elif, else.
Deve imprimir a classificação correta conforme a tabela.
Enviar o link do repositório com o Código'''

IMC = float(input("Digite o IMC"))

if IMC < 18.5:
     print("abaixo do peso")
elif IMC < 24.9:
     print("peso normal")
elif IMC < 29.9:
     print("sobre peso")
elif IMC < 39.9:
    print("obesidade")
else: 
    print("obesidade grave")