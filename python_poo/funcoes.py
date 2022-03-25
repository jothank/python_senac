def pergunta_int(pergunta):
    return int(input(pergunta))


def pergunta_float(pergunta):
    return float(input(pergunta))


def pergunta_string(pergunta):
    return input(pergunta)


def calc_media_ari_pond_harm(n1, n2, n3, opcao):
    if opcao == "1":
        print((n1 + n2 + n3) / 3)
    elif opcao == "2":
        print((n1*5 + n2*3 + n3*2) / 10)
    elif opcao == "3":
        print((1/n1 + 1/n2 + 1/n3) / 3)
    else:
        print("Opção inválida!")


def calc_media_4_notas(n_aluno, n1, n2, n3, n4):
    med_exe = ((n1+(n2*2)+(n3*3)+n4)/7  )
    if med_exe < 4.0:
        resultado = "E"
        print(f"Número do aluno é {n_aluno}, a média dos exercícios é {n4:.2f}, média de aproveitamento é {med_exe:.2f}, você foi reprovado")
    elif med_exe >= 4.0 and med_exe < 6.0:
        resultado = "D"
        print(f"Número do aluno é {n_aluno}, a média dos exercícios é {n4:.2f}, média de aproveitamento é {med_exe:.2f}, você foi reprovado")
    elif med_exe >= 6.0 and med_exe < 7.5:
        resultado = "C"
        print(f"Número do aluno é {n_aluno}, a média dos exercícios é {n4:.2f}, média de aproveitamento é {med_exe:.2f}, você foi aprovado")
    elif med_exe >= 7.5 and med_exe < 9.0:
        resultado = "B"
        print(f"Número do aluno é {n_aluno}, a média dos exercícios é {n4:.2f}, média de aproveitamento é {med_exe:.2f}, você foi aprovado")
    elif med_exe >= 9.0:
        resultado = "A"
        print(f"Número do aluno é {n_aluno}, a média dos exercícios é {n4:.2f}, média de aproveitamento é {med_exe:.2f}, você foi aprovado")