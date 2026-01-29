'''

Dona Maria precisa de um algoritimo que faça a seguinte decisões:

1. Se a idade for menor que 12, deve mostrar a mensagem "CRIANÇA"
2. Se a idade for menor que 18, deve mo0strar a mensagem "ADOLESCENTE"
3. Se a idade  for menor que 60, deve mostrar a mensagem "ADULTO"
4. Se a idade não for nenhuma dessas opções, deve mostrar "IDOSO"

#Entrada de Infomações 
''' 
idade = 26

if idade < 13:
    print("Criança")
elif idade < 18:
    print("ADOLESCENTE")
elif idade < 60:
    print("ADULTO")
else:
    print('IDOSO')