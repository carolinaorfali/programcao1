companhias = {"TAP": {"pais": "Portugal", "ativa": True},
              "Iberia": {"pais": "Espanha", "ativa": True}}          
aeroportos = {"Lisboa": "Portugal", "Porto": "Portugal", "Madrid": "Espanha"}  
voos = {"TP1": {"companhia": "TAP", "origem": "Lisboa", "destino": "Madrid", "preco": 120.0},    # voo comum
        "TP2": {"companhia": "TAP", "origem": "Porto", "destino": "Lisboa", "preco": 60.0},      # sem reservas
        "IB1": {"companhia": "Iberia", "origem": "Lisboa", "destino": "Madrid", "preco": 99.0},  # voo comum
        "IB2": {"companhia": "Iberia", "origem": "Madrid", "destino": "Porto", "preco": 110.0}}
reservas = [["Ana", "TP1"], ["Ana", "IB2"], ["Rui", "TP1"]]  # Ana com 2 reservas; TP1 com 2 passageiros

# ===== MENU PRINCIPAL====
perfil = ""
while perfil != "0":
    perfil = input("\nPERFIL: 1-Gestão 2-Companhia 3-Passageiro 0-Sair: ")

    # ----- PERFIL 1: GESTÃO -----
    if perfil == "1":
        op = ""
        while op != "0":
            op = input("\nGESTÃO: 1-Inserir companhia 2-Alterar país 3-Ativar/desativar 4-Inserir aeroporto 0-Voltar: ")
            if op == "1":
                nome = input("Nome da companhia: ")
                if nome == "" or nome in companhias:
                    print("Nome vazio ou já existe.")
                else:
                    companhias[nome] = {"pais": input("País: "), "ativa": True}
            elif op == "2" or op == "3":
                print(companhias)
                nome = input("Companhia: ")
                if nome not in companhias:
                    print("Companhia não existe.")
                elif op == "2":
                    companhias[nome]["pais"] = input("Novo país: ")
                else:
                    companhias[nome]["ativa"] = not companhias[nome]["ativa"]  # inverte o estado
            elif op == "4":
                nome = input("Nome do aeroporto: ")
                if nome == "" or nome in aeroportos:
                    print("Nome vazio ou já existe.")
                else:
                    aeroportos[nome] = input("País: ")
            elif op != "0":
                print("Opção inválida.")

    # ----- PERFIL 2 COMPANHIA -----
    elif perfil == "2":
        print(companhias)
        minha = input("Sua companhia: ")
        if minha not in companhias or not companhias[minha]["ativa"]:
            print("Companhia inexistente ou inativa.")
        else:
            op = ""
            while op != "0":
                op = input(f"\n{minha}: 1-Inserir voo 2-Alterar voo 3-Anular voo 4-Ver reservas 0-Voltar: ")
                if op == "1" or op == "2":
                    cod = input("Código do voo: ")
                    if op == "1" and cod in voos:
                        print("Esse código já existe.")
                    elif op == "2" and (cod not in voos or voos[cod]["companhia"] != minha):
                        print("Voo não existe nesta companhia.")
                    else:
                        print("Aeroportos:", list(aeroportos.keys()))
                        origem = input("Origem: ")
                        destino = input("Destino: ")
                        try:
                            preco = float(input("Preço: "))
                            # origem e destino têm de ser aeroportos existentes
                            if origem not in aeroportos or destino not in aeroportos or origem == destino or preco <= 0:
                                print("Dados inválidos.")
                            else:
                                voos[cod] = {"companhia": minha, "origem": origem, "destino": destino, "preco": preco}
                                print("Voo guardado.")
                        except ValueError:
                            print("Preço inválido.")
                elif op == "3":
                    cod = input("Código do voo: ")
                    if cod not in voos or voos[cod]["companhia"] != minha:
                        print("Voo não existe nesta companhia.")
                    else:
                        tem = False
                        for r in reservas:
                            if r[1] == cod:
                                tem = True
                        if tem:
                            print("O voo tem reservas, não pode ser anulado.")
                        else:
                            del voos[cod]
                            print("Voo anulado.")
                elif op == "4":
                    for r in reservas:
                        if voos[r[1]]["companhia"] == minha:
                            print(r[0], "->", r[1])
                elif op != "0":
                    print("Opção inválida.")

    # ----- PERFIL 3: PASSAGEIRO -----
    elif perfil == "3":
        nome = input("Seu nome: ")
        if nome == "":
            print("Nome vazio.")
        else:
            if nome not in passageiros:
                passageiros.append(nome)
            op = ""
            while op != "0":
                op = input(f"\n{nome}: 1-Ver voos 2-Comparar 3-Reservar 4-Alterar reserva 5-Anular reserva 0-Voltar: ")
                if op == "1" or op == "2":
                    if op == "2":
                        origem = input("Origem: ")
                        destino = input("Destino: ")
                    for cod in voos:
                        v = voos[cod]
                        # na opção 2 só mostra os voos com a mesma origem e destino
                        if op == "1" or (v["origem"] == origem and v["destino"] == destino):
                            print(cod, v["companhia"], v["origem"], "->", v["destino"], v["preco"], "€")
                elif op == "3" or op == "4" or op == "5":
                    antigo = ""
                    if op != "3":
                        print("Suas reservas:")
                        for r in reservas:
                            if r[0] == nome:
                                print(r[1])
                        antigo = input("Código da reserva: ")
                    if op != "3" and [nome, antigo] not in reservas:
                        print("Reserva inexistente.")
                    elif op == "5":
                        reservas.remove([nome, antigo])
                        print("Reserva anulada.")
                    else:
                        cod = input("Código do voo: ")
                        if cod not in voos or not companhias[voos[cod]["companhia"]]["ativa"]:
                            print("Voo inexistente ou companhia inativa.")
                        elif [nome, cod] in reservas:
                            print("Você já tem essa reserva.")
                        else:
                            if op == "4":
                                reservas.remove([nome, antigo])   # alterar = trocar a reserva antiga pela nova
                            reservas.append([nome, cod])
                            print("Reserva guardada.")
                elif op != "0":
                    print("Opção inválida.")

    elif perfil != "0":
        print("Opção inválida.")

print("Programa finalizado.")