import random
import mysql.connector


def cadastar_cliente(conexao, indicador):

    while True:
        try:
            idcpf_cnpj = input("CPF/CNPJ: ")
            indicador.execute(f"INSERT INTO cliente (idcpf_cnpj) VALUES ('{idcpf_cnpj}')")
            conexao.commit()
            break
        except mysql.connector.IntegrityError:
            print("Cliente já cadastrado.")
    
    nome = input("Nome: ")
    senha = input("Senha: ")

    while True:
        try:
            email = input("E-mail: ")
            indicador.execute(f"UPDATE cliente SET email = '{email}' WHERE idcpf_cnpj = {idcpf_cnpj}")
            conexao.commit()
            break
        except mysql.connector.IntegrityError:
            print("E-mail já cadastrado.")
    
    data_nascimento = input("Data de Nascimento: ")
    telefone = input("Telefone: ")
    cep = input("Cep: ")
    cidade = input("Cidade: ")
    endereco = input("Endereço: ")
    bairro = input("Bairro: ")

    indicador.execute(f"UPDATE cliente SET nome = '{nome}', senha = '{senha}', data_nascimento = '{data_nascimento}', "
                      f"telefone = '{telefone}', cep = '{cep}', cidade = '{cidade}', endereco = '{endereco}', bairro = '{bairro}' "
                      f"WHERE idcpg_cnpj = {idcpf_cnpj}")
    conexao.commit()

    print("Cliente cadastrado com sucesso")
    input("Precione qualquer tecla para continuar...")


def login(indicador):

    acessar = True

    while acessar:

        nome = input("Usuario: ")

        indicador.execute(f"SELECT idcpf_cnpj, senha FROM cliente WHERE nome = '{nome}'")
        leitura = indicador.fetchall()

        if len(leitura) == 0:
            print("Usuario não cadastrado\n")
            continuar = input("Deseja continuar? S para sim, N para não: ").upper()

            if continuar == 'N':
                acessar = False
                exit()
        else:
            senha = input("Digite a senha: ")

            if leitura[0][1] == senha:
                print("Loggin efetuado")
                return leitura[0][0]

            else:
                print("Senha errada")
                continuar = input("Deseja continuar? S para sim, N para não: ").upper()

                if continuar == 'N':
                    acessar = False
                    exit()


def solicitar_locacao(conexao, indicador, cliente):

    localizacao = input("Localizacao: ")
    idambiente = input("Ambiente: ")
    tipo_evento = input("Tipo de Evento: ")
    data_evento = input("Data: ")
    formato_evento = input("Formato do Evento: ")
    item = input("Item: ")
    hora_inicial = input("Hora inicial: ")
    hora_final = input("Hora final: ")
    ocupacao = input("Número de convidados: ")
    chv_est_idcpf_cnpj = cliente

    indicador.execute("INSERT INTO solicitacao (localizacao, idambiente, tipo_evento, data_evento, "
                      "formato_evento, item, hora_inicial, hora_final, ocupacao, idcpf_cnpj) VALUES "
                      f"('{localizacao}', '{idambiente}', '{tipo_evento}', '{data_evento}', '{formato_evento}', "
                      f"'{item}', '{hora_inicial}', '{hora_final}', '{ocupacao}', '{chv_est_idcpf_cnpj}')")
    conexao.commit()

    print("Solicitação realizada com sucesso")
    continuar = input("Precione qualquer tecla para continuar...")


def consultar_solicitacao(conexao, indicador, cliente):

    indicador.execute(f"SELECT idambiente, situacao FROM solicitacao WHERE idcpf_cnpj = '{cliente}'")
    leitura = indicador.fetchall()
    print(f"Solicitação\n")
    for row in leitura:
        print(f"Ambiente: {row[0]}")
        print(f"Status: {row[1]}")

    if leitura[0][1] == 'Aguardando Pagamento':

        pagar = input("Deseja realizar o pagamento das solicitações "
                      "em aberto, S para sim, N para não: ").upper()
        if pagar == 'S':
            idpagamento = realizar_pagamento(conexao, indicador)
            indicador.execute(f"UPDATE solicitacao SET idpagamento = '{idpagamento}', "
                              f"situacao = 'Pagamento Aprovado' WHERE idcpf_cnpj = '{cliente}'")
            print("Pagamento realizado com sucesso")
            continuar = input("Precione qualquer tecla para continuar...")
            conexao.commit()


def realizar_pagamento(conexao, indicador):

    idpagamento = random.randint(0, 1000000)

    numero_cartao = input("Número Cartão: ")
    titular = input("Titular: ")
    validade = input("Validade: ")
    cvv = input("CVV: ")
    parcelas = input("Parcelas: ")

    indicador.execute(f"INSERT INTO pagamento (idpagamento, numero_cartao, titular, validade, cvv, parcelas) "
                      f"VALUES ('{idpagamento}', '{numero_cartao}', '{titular}', '{validade}', '{cvv}', '{parcelas}')")
    conexao.commit()

    return idpagamento
