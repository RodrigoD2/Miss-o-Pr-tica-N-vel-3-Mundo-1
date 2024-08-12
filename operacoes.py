#Missão Prática | Estruturando os Dados 💻
#Operações da missão prática

from main import calcular_media, verificar_reprovacao, alunos_reprovados

dados_alunos = [               #dados dos alunos
    (26, "Maria", [8, 7, 5, 9]),
    (101, "Ana", [9, 9, 8, 9]),
    (13, "João", [6, 5, 5, 5]),
    (37, "Ágatha", [8, 6, 7.5, 9]),
    (72,"Joaquin", [6, 5.5, 5, 7]),
    (5, "Félix", [10, 8, 8, 8])
]


alunos_reprovados = alunos_reprovados(dados_alunos)

for aluno in alunos_reprovados: #imprenção dos alunos reporvados
    print(aluno)