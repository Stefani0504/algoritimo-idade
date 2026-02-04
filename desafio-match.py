'''
Docstring for desafio-match 

 
Você foi contratado para criar um menu interativo de atendimento para uma empresa fictícia. O sistema deve exibir as opções abaixo e, de acordo com o número digitado, apresentar uma resposta:

Opções do menu:
[1] Falar com atendente
[2] Segunda via de boleto
[3] Cancelar serviço
[4] Informações sobre planos
[5] Sair

O que o programa deve fazer:

Mostrar o menu acima.
Receber a opção digitada pelo usuário.
Utilizar match case para responder com base na opção.
Exibir uma mensagem apropriada para cada caso.
Caso digite algo inválido, exibir: "Opção inválida, tente novamente!"

Critérios para o desafio estar completo:
Testar diferentes entradas para verificar todas as respostas.
Enviar o link do repositório com o Código
''' 


print('''[1] Falar com atendente
[2] Segunda via de boleto
[3] Cancelar serviço
[4] Informações sobre planos
[5] Sair

''')


#Entrada de Dados (opção desejada)

opção_usuario = input("entre com a opção desejada: ")


match opção_usuario:
    case "1":
        print("=== iremos colocar você em contato com atendente ===")
    case "2":
        print("=== iremos enviar a segunda via do boleto para seu e-mail ===")
    case "3":
        print("=== cancelando serviço ===")
    case "4":
        print("=== informações sobre o plano")
    case "5":
        print("=== saindo ===")
    case _:
        print("=== Opção inválida ===")
    