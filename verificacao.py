def cpf():

    while True:

        cpf = input("CPF: ")

        cpf_limpo = []

        for caracter in cpf:

            if caracter.isdigit():
                cpf_limpo.append(caracter)

        if len(cpf_limpo) == 11:

            dig_verif_um = int(cpf_limpo[9])
            dig_verif_dois = int(cpf_limpo[10])

            verifica = 0
            peso = 1

            for numero in range(9):

                verifica += (peso * int(cpf_limpo[numero]))
                peso += 1

            if verifica % 11 == dig_verif_um or (verifica % 11 == 10 and dig_verif_um == 0):

                verifica = 0

                for numero in range(10):

                    verifica += (numero * int(cpf_limpo[numero]))

                if verifica % 11 == dig_verif_dois or (verifica % 11 == 10 and dig_verif_dois == 0):
                    return cpf

                else:
                    print("O CPF é inválido")

            else:
                print("O CPF é inválido")

        else:
            print("O CPF é inválido")


def cnpj():

    while True:

        cnpj = input("CNPJ: ")

        cnpj_limpo = []

        for caracter in cnpj:

            if caracter.isdigit():
                cnpj_limpo.append(caracter)

        if len(cnpj_limpo) == 14:

            dig_verif_um = int(cnpj_limpo[12])
            dig_verif_dois = int(cnpj_limpo[13])

            verifica = 0
            peso = 6

            for numero in range(12):

                verifica += (peso * int(cnpj_limpo[numero]))
                peso += 1

                if peso == 10:
                    peso = 2

            if verifica % 11 == dig_verif_um or (verifica % 11 == 10 and dig_verif_um == 0):

                verifica = 0
                peso = 5

                for numero in range(13):

                    verifica += (peso * int(cnpj_limpo[numero]))
                    peso += 1

                    if peso == 10:
                        peso = 2

                if verifica % 11 == dig_verif_dois or (verifica % 11 == 10 and dig_verif_dois == 0):
                    return cnpj

                else:
                    print("O CNPJ é inválido")

            else:
                print("O CNPJ é inválido")
        
        else:
            print("O CNPJ é inválido")
