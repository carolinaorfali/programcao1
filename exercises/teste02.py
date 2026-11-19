companhias = []
aeroportos = []
passageiros = []
voos = []
reservas = []

# ADMINISTRACAO

def administracao():
    while True:
        print("\n1 - Gerir companhias")
        print("2 - Inserir aeroporto")
        print("0 - Voltar")

        op = input("Opcao: ")

        if op == "1":
            print("1 - Inserir")
            print("2 - Alterar")
            print("3 - Ativar/Desativar")
            escolha = input("Opcao: ")

            if escolha == "1":
                companhias.append({
                    "id": len(companhias)+1,
                    "nome": input("Nome: "),
                    "pais": input("Pais: "),
                    "ativa": True
                })

            elif escolha == "2" or escolha == "3":
                for c in companhias:
                    print(c)

                try:
                    id = int(input("ID: "))
                    c = procurar(companhias, id)

                    if c != None:
                        if escolha == "2":
                            c["nome"] = input("Novo nome: ")
                            c["pais"] = input("Novo pais: ")
                        else:
                            c["ativa"] = not c["ativa"]
                    else:
                        print("Nao encontrado!")

                except ValueError:
                    print("ID invalido!")

        elif op == "2":
            codigo = input("Codigo IATA: ").upper()

            if procurar_codigo(codigo) == None:
                aeroportos.append({
                    "id": len(aeroportos)+1,
                    "codigo": codigo,
                    "nome": input("Nome: "),
                    "cidade": input("Cidade: "),
                    "pais": input("Pais: ")
                })
            else:
                print("Aeroporto ja existe!")

        elif op == "0":
            break


def procurar_codigo(codigo):
    for a in aeroportos:
        if a["codigo"] == codigo:
            return a
    return None


# COMPANHIA AEREA

def companhia_aerea():
    for c in companhias:
        print(c)

    try:
        id = int(input("ID da companhia: "))
        c = procurar(companhias, id)

        if c == None or not c["ativa"]:
            print("Companhia inexistente ou inativa!")
            return

    except ValueError:
        print("ID invalido!")
        return

    while True:
        print("\n1 - Gerir voos")
        print("2 - Consultar reservas")
        print("0 - Voltar")
        op = input("Opcao: ")

        if op == "1":
            print("1 - Inserir")
            print("2 - Alterar")
            print("3 - Anular")
            escolha = input("Opcao: ")

            if escolha == "1":
                origem = input("Origem: ").upper()
                destino = input("Destino: ").upper()

                if (procurar_codigo(origem) == None
                    or procurar_codigo(destino) == None
                    or origem == destino):
                    print("Aeroportos invalidos!")
                    continue

                try:
                    preco = float(input("Preco: "))
                    if preco <= 0:
                        print("Preco invalido!")
                        continue

                    voos.append({
                        "id": len(voos)+1,
                        "companhia": id,
                        "origem": origem,
                        "destino": destino,
                        "data": input("Data: "),
                        "preco": preco,
                        "estado": "ativo"
                    })
                    print("Voo inserido!")

                except ValueError:
                    print("Preco invalido!")

            elif escolha == "2" or escolha == "3":
                for v in voos:
                    if v["companhia"] == id:
                        print(v)

                try:
                    id_voo = int(input("ID do voo: "))
                    v = procurar(voos, id_voo)

                    if v != None and v["companhia"] == id and v["estado"] == "ativo":

                        if escolha == "2":
                            origem = input("Nova origem: ").upper()
                            destino = input("Novo destino: ").upper()

                            if (procurar_codigo(origem) != None
                                and procurar_codigo(destino) != None
                                and origem != destino):

                                v["origem"] = origem
                                v["destino"] = destino
                                v["data"] = input("Nova data: ")

                                try:
                                    preco = float(input("Novo preco: "))
                                    if preco > 0:
                                        v["preco"] = preco
                                    else:
                                        print("Preco invalido!")
                                except ValueError:
                                    print("Preco invalido!")
                            else:
                                print("Aeroportos invalidos!")

                        else:
                            tem_reserva = False

                            for r in reservas:
                                if r["voo"] == id_voo and r["estado"] == "ativa":
                                    tem_reserva = True

                            if not tem_reserva:
                                v["estado"] = "anulado"
                                print("Voo anulado!")
                            else:
                                print("Voo possui reservas!")

                    else:
                        print("Voo nao encontrado!")

                except ValueError:
                    print("ID invalido!")

        elif op == "2":
            for r in reservas:
                v = procurar(voos, r["voo"])
                if v != None and v["companhia"] == id:
                    print(r)

        elif op == "0":
            break


# PASSAGEIRO

def passageiro():
    while True:
        print("\n1 - Cadastrar passageiro")
        print("2 - Consultar/comparar voos")
        print("3 - Gerir reservas")
        print("0 - Voltar")
        op = input("Opcao: ")

        if op == "1":
            passageiros.append({
                "id": len(passageiros)+1,
                "nome": input("Nome: "),
                "documento": input("Documento: ")
            })

        elif op == "2":
            origem = input("Origem: ").upper()
            destino = input("Destino: ").upper()

            for v in voos:
                if (v["origem"] == origem and
                    v["destino"] == destino and
                    v["estado"] == "ativo"):
                    print(v)

        elif op == "3":
            print("1 - Reservar")
            print("2 - Alterar")
            print("3 - Anular")
            escolha = input("Opcao: ")

            if escolha == "1":
                for p in passageiros:
                    print(p)

                try:
                    id_p = int(input("ID do passageiro: "))
                    p = procurar(passageiros, id_p)

                    if p == None:
                        print("Passageiro inexistente!")
                        continue

                    for v in voos:
                        if v["estado"] == "ativo":
                            print(v)

                    id_v = int(input("ID do voo: "))
                    v = procurar(voos, id_v)

                    if v != None and v["estado"] == "ativo":
                        reservas.append({
                            "id": len(reservas)+1,
                            "passageiro": id_p,
                            "voo": id_v,
                            "estado": "ativa"
                        })
                        print("Reserva efetuada!")
                    else:
                        print("Voo indisponivel!")

                except ValueError:
                    print("ID invalido!")

            elif escolha == "2" or escolha == "3":
                try:
                    id_r = int(input("ID da reserva: "))
                    r = procurar(reservas, id_r)

                    if r != None and r["estado"] == "ativa":
                        id_p = int(input("ID do passageiro: "))

                        if r["passageiro"] == id_p:

                            if escolha == "2":
                                id_v = int(input("Novo ID do voo: "))
                                v = procurar(voos, id_v)

                                if v != None and v["estado"] == "ativo":
                                    r["voo"] = id_v
                                    print("Reserva alterada!")
                                else:
                                    print("Voo indisponivel!")

                            else:
                                r["estado"] = "anulada"
                                print("Reserva anulada!")

                        else:
                            print("Passageiro incorreto!")

                    else:
                        print("Reserva inexistente!")

                except ValueError:
                    print("ID invalido!")


# MENU PRINCIPAL

while True:
    print("\n===== VIAGENS DE AVIAO =====")
    print("1 - Administracao")
    print("2 - Companhia aerea")
    print("3 - Passageiro")
    print("0 - Sair")

    op = input("Escolha o perfil: ")

    if op == "1":
        administracao()
    elif op == "2":
        companhia_aerea()
    elif op == "3":
        passageiro()
    elif op == "0":
        break
    else:
        print("Opcao invalida!")
