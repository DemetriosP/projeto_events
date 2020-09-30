def cadastrar_funcionario(conexao, indicador):

    idfuncionario = input("Matricula: ")
    nome = input("Nome: ")
    senha = input("Senha: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    cargo = input("Cargo: ")
    setor = input("Setor: ")

    indicador.execute("INSERT INTO funcionario (idfuncionario, nome, senha, telefone, email, cargo, setor) "
                      f"VALUES ('{idfuncionario}', '{nome}', '{senha}', '{telefone}', '{email}', '{cargo}', '{setor}')")
    conexao.commit()

    print("Cliente cadastrado com sucesso")
    continuar = input("Precione qualquer tecla para continuar...")


def login(indicador):

    print("|||Tela de Login|||")

    acessar = True

    while acessar:

        nome = input("Usuario: ")

        indicador.execute(f"SELECT idfuncionario, senha FROM funcionario WHERE nome = '{nome}'")
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


def cadastar_ambiente(conexao, indicador, funcionario):

    idambiente = input("Codigo: ")
    localizacao = input("Infome o local: ").upper()
    descricao = input("Informa a descrição: ")
    ocupacao_min = input("Informe a ocupação minima: ")
    ocupacao_max = input("Informe a ocupação máxima: ")
    chv_est_idfuncionario = funcionario

    indicador.execute("INSERT INTO ambiente (idambiente, localizacao, descricao, ocupacao_min, ocupacao_max, "
                      f"idfuncionario) VALUES ('{idambiente}', '{localizacao}', '{descricao}', '{ocupacao_min}', "
                      f"'{ocupacao_max}', '{chv_est_idfuncionario}')")
    conexao.commit()

    print("Ambiente cadastrado com sucesso")
    continuar = input("Precione qualquer tecla para continuar...")


def cadastar_item(conexao, indicador, funcionario, ambiente=2):

    iditem = input("Codigo: ")
    data_inclusao = input("Data: ")
    descricao = input("Descrição: ")
    categoria = input("Categoria: ")
    titulo = input("Título: ")
    tecnica = input("Técnica: ")
    dimensao = input("Dimensão: ")
    autor = input("Autor: ")
    valor = input("Valor: ")
    imagem = input("Imagem: ")
    chv_est_idfuncionario = funcionario
    chv_est_idambiente = ambiente

    indicador.execute("INSERT INTO item (iditem, data_inclusao, descricao, categoria, titulo, tecnica, dimensao, "
                      f"autor, valor, imagem, idfuncionario, idambiente) VALUES ('{iditem}', '{data_inclusao}', "
                      f"'{descricao}' ,'{categoria}', '{titulo}', '{tecnica}', '{dimensao}', '{autor}', '{valor}', "
                      f"'{imagem}', '{chv_est_idfuncionario}', '{chv_est_idambiente}')")
    conexao.commit()

    print("Item cadastrado com sucesso")
    continuar = input("Precione qualquer tecla para continuar...")

def responder_solicitacao(conexao, indicador, funcionario):

    indicador.execute("SELECT idsolicitacao, idambiente, item, ocupacao, hora_inicial, hora_final, "
                      "data_evento FROM solicitacao WHERE situacao = 'Aguardando Aprovação'")
    leitura = indicador.fetchall()

    if len(leitura) != 0:
        print(f"Responder Solicitação\n")

        for row in leitura:

            print(f"Ambiente: {row[1]}")
            print(f"Item: {row[2]}")
            print(f"Quantidade de convidados: {row[3]}")
            print(f"Horário Inicial: {row[4]}")
            print(f"Horário Final: {row[5]}")
            print(f"Data do evento: {row[6]}")

            situacao = input("Status da Solicitação: ")

            indicador.execute(f"UPDATE solicitacao SET situacao = '{situacao}', idfuncionario = '{funcionario}' "
                              f"WHERE idsolicitacao = '{row[0]}'")
            conexao.commit()
    else:
        print("Não há nenhuma solicitação em aberto")
        continuar = input("Precione qualquer tecla para continuar...")



def atualizar_ambiente(conexao, indicador):

    ambiente = input("Informe o codigo do ambiente que deseja alterar as informações: ")

    descricao = input("Descrição: ")
    ocupacao_min = input("Ocupação minima: ")
    ocupacao_max = input("Ocupação máxima: ")
    situacao = input("Situação Ambiente: ")

    comando_sql = "UPDATE ambiente SET descricao = %s, ocupacao_min = %s, " \
                  "ocupacao_max = %s, situacao = %s WHERE idambiente = %s"

    dados = (descricao, ocupacao_min, ocupacao_max, situacao, ambiente)

    indicador.execute(comando_sql, dados)
    conexao.commit()

    print("Ambiente atualizado")
    continuar = input("Precione qualquer tecla para continuar...")

def atualizar_item(conexao, indicador):

    item = input("Informe o codigo do item que deseja alterar as informações: ")
    descricao = input("Descrição: ")
    categoria = input("Categoria: ")
    titulo = input("Titulo: ")
    tecnica = input("Tecnica: ")
    dimensao = input("Dimensão: ")
    autor = input("Autor: ")
    situacao = input("Situação: ")

    indicador.execute(f"UPDATE item SET descricao = '{descricao}', categoria = '{categoria}', titulo = '{titulo}',"
                      f"tecnica = '{tecnica}', dimensao = '{dimensao}', autor = '{autor}', situacao = '{situacao}' "
                      f"WHERE iditem = '{item}'")
    conexao.commit()

    print("Item atualizado")
    continuar = input("Precione qualquer tecla para continuar...")


def transferir_item(conexao, indicador):

    item = input("Informe o codigo do item que deseja transferir de localização: ")
    ambiente = input("Informe o codigo do ambiente para onde deseja transferir o item: ")

    indicador.execute(f"UPDATE item SET idambiente = '{ambiente}' WHERE iditem = '{item}'")
    conexao.commit()

    print("Item transferido")
    continuar = input("Precione qualquer tecla para continuar...")


def consultar_funcionario(indicador):

    indicador.execute('SELECT idfuncionario, nome, email, telefone, setor, cargo  FROM funcionario')
    leitura = indicador.fetchall()
    print(f"Total de funcionários registrados no sistema: {indicador.rowcount}\n")
    for row in leitura:
        print(f"Matricula: {row[0]}")
        print(f"Nome: {row[1]}")
        print(f"E-mail: {row[2]}")
        print(f"Telefone: {row[3]}")
        print(f"Setor: {row[4]}")
        print(f"Cargo: {row[5]}\n")


def consultar_cliente(indicador):

    indicador.execute('SELECT idcpf_cnpj, nome, email, data_nascimento, '
                      'telefone, cep, cidade, endereco, bairro  FROM cliente')
    leitura = indicador.fetchall()
    print(f"Total de cliente registrados no sistema: {indicador.rowcount}\n")
    for row in leitura:
        print(f"CPF/CNPJ: {row[0]}")
        print(f"Nome: {row[1]}")
        print(f"E-mail: {row[2]}")
        print(f"Data de Nascimento: {row[3]}")
        print(f"Telefone: {row[4]}")
        print(f"Cep: {row[5]}")
        print(f"Cidade: {row[6]}")
        print(f"Endereco: {row[7]}")
        print(f"Bairro: {row[8]}\n")


def consultar_ambiente_ocupacao(indicador):

    indicador.execute('SELECT descricao, ocupacao_min, ocupacao_max  FROM ambiente')
    leitura = indicador.fetchall()
    print(f"Consultar Ocupação\n")
    for row in leitura:
        print(f"Ambiente: {row[0]}")
        print(f"Ocupação Minima: {row[1]}")
        print(f"Ocupação Máxima: {row[2]}\n")


def consultar_ambiente_funcionario(indicador):

    indicador.execute('SELECT descricao, idfuncionario  FROM ambiente')
    leitura = indicador.fetchall()

    print(f"Consultar Funcionario\n")
    for row in leitura:
        print(f"Ambiente: {row[0]}")
        print(f"Matricula do funcionario que cadastrou o ambiente: {row[1]}\n")


def consultar_item(indicador):
    indicador.execute('SELECT iditem, idfuncionario, idambiente FROM item')
    leitura = indicador.fetchall()
    print(f"Total de Itens registrados no sistema: {indicador.rowcount}\n")
    for row in leitura:
        print(f"Item: {row[0]}")
        print(f"Matricula do funcionario: {row[1]}")
        print(f"Id do Ambiente: {row[2]}")


def consultar_solicitacao_pag(indicador):
    indicador.execute('SELECT c.nome,s.idpagamento,s.idfuncionario \
                       FROM solicitacao s  LEFT JOIN cliente c\
                       ON s.idsolicitacao = c.nome\
                       ORDER BY  c.nome')
    leitura = indicador.fetchall()
    print(f"O total de  solicitacões registrados no sistema é: {indicador.rowcount}\n")
    for row in leitura:
        print(f"Nome do cliente: {row[0]}")
        print(f"Numero da ordem de pagamento: {row[1]}")
        print(f"Matricula do funcionario que liberou: {row[2]}")
        print("------------------------------------------\n")
