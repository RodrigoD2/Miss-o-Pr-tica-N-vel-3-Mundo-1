# Missão Prática | Estruturando os Dados 💻
# funções da missão prática

def calcular_media(notas):  #calculo das notas
    if len(notas) != 4:
        raise ValueError("A lista de notas deve conter exatamente 4 elementos.")
    return sum(notas) / len(notas)

def verificar_reprovacao(media):  #verificação de da média
    return media < 6

def alunos_reprovados(dados_alunos): #verificando alunos reprovados
    reprovados = []
    for matricula, nome, notas in dados_alunos:
        media = calcular_media(notas)
        if verificar_reprovacao(media):
            reprovados.append(f"Aluno Reprovado: {nome} - Matrícula: {matricula} - Média Final: {media:.2f}")
    return reprovados
