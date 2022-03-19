import funcoes

num_aluno = funcoes.pergunta_int("Digite o numero do aluno: ")
num1 = funcoes.pergunta_int("Digite primeiro numero: ")
num2 = funcoes.pergunta_int("Digite um segundo número: ")
num3 = funcoes.pergunta_int("Digite um terceiro número: ")
num4 = funcoes.pergunta_int("Digite um quarto número: ")
resultado = funcoes.calc_media_4_notas(num_aluno, num1, num2, num3, num4)



num1 = funcoes.pergunta_int("Digite primeiro numero: ")
num2 = funcoes.pergunta_int("Digite um segundo número: ")
num3 = funcoes.pergunta_int("Digite um terceiro número: ")
opcao = funcoes.pergunta_string("Digite 1-aritmética 2-ponderada ou 3-harmônica para escolher o calculo da média: ")
resultado = funcoes.calc_media_ari_pond_harm(num1, num2, num3, opcao)
