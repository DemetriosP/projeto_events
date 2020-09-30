import cliente
import funcionario
import mysql.connector

connection = mysql.connector.connect(host='localhost', database='evento', user='root', password='')
cursor = connection.cursor(prepared=True)

# Laço principal

while True:

    # Menu inicial do programa
    print("Bem vindo ao Events")
    opcao = input("Menu 1:\n1 - Área do Funcionário\n2 - Área do Cliente\n")

    # Menu de login do funcionário
    if opcao == "1":

        sair_funcionario = True

        print("Faça o seu Login!")
        idfuncinario = funcionario.login(cursor)

        while sair_funcionario:

            # Opções apos o Funcionario logar

            opc = input('Bem vindo á Área do Funcionário\nMenu\n1 - Cadastar Item\n2 - Cadastrar Ambiente\n'
                        '3 - Cadastar Funcionário\n4 - Atualizar informações Ambiente\n5 - Atualizar informações Item\n'
                        '6 - Exibir todos os funcionarios\n7 - Exibir todos os Clientes\n'
                        '8 - Consultar Ocupação Ambientes\n9 - Consultar registro de cadastro dos ambientes\n'
                        '10 - Consultar Informações Item\n11 - Consultar Informações Solicitação\n'
                        '12 - Transferir Item de Localização\n13 - Responder Solicitação\n'
                        '14 - Sair da área do funcionário\n')

            if opc == '1':
                funcionario.cadastar_item(connection, cursor, idfuncinario)

            elif opc == '2':
                funcionario.cadastar_ambiente(connection, cursor, idfuncinario)

            elif opc == '3':
                funcionario.cadastrar_funcionario(connection, cursor)

            elif opc == '4':
                funcionario.atualizar_ambiente(connection, cursor)

            elif opc == '5':
                funcionario.atualizar_item(connection, cursor)

            elif opc == '6':
                funcionario.consultar_funcionario(cursor)

            elif opc == '7':
                funcionario.consultar_cliente(cursor)

            elif opc == '8':
                funcionario.consultar_ambiente_ocupacao(cursor)

            elif opc == '9':
                funcionario.consultar_ambiente_funcionario(cursor)

            elif opc == '10':
                funcionario.consultar_item(cursor)

            elif opc == '11':
                funcionario.consultar_solicitacao_pag(cursor)

            elif opc == '12':
                funcionario.transferir_item(connection, cursor)

            elif opc == '13':
                funcionario.responder_solicitacao(connection,cursor, idfuncinario)

            elif opc == '14':
                sair_funcionario = False

            else:
                print("Opção invalida, por favor escolha outra opção\nPrecione qualquer tecla para continuar...")
                continuar = input()

    # Menu do Cliente
    elif opcao == "2":

        sair = True

        while sair:
            print("Você pode se cadastrar ou fazer o login!")
            opc = input("1 - Se Cadastre!\n2 - Fazer Login\n3 - Voltar ao menu anterior\n")

            if opc == '1':
                cliente.cadastar_cliente(connection, cursor)

            elif opc == '2':
                idcliente = cliente.login(cursor)

                sair_cliente = True

                while sair_cliente:
                    print("Bem vindo a área do Cliente")
                    opc = input("1 - Solicitar locação\n2 - Consultar Solicitação\n3 - Sair da área do cliente")

                    if opc == '1':
                        cliente.solicitar_locacao(connection, cursor, idcliente)

                    elif opc == '2':
                        cliente.consultar_solicitacao(connection, cursor, idcliente)

                    elif opc == '3':
                        sair_cliente = False
                    else:
                        print("Opção invalida, por favor escolha outra opção")

            elif opc == '3':
                sair = False

            else:
                print("Opção invalida, por favor escolha outra opção\nPrecione qualquer tecla para continuar...")
                continuar = input()
