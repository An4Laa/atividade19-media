# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

nota_a = float(input("Digite nota 1: "))
nota_b = float(input("Digite nota 2: "))
media = (nota_a + nota_b) / 2

if media < 5.0 :
    print("Você está REPROVADO!")

elif media >= 5.0 and media <= 6.9 :
    print("Você está de recuperação.")

else :
    print("Parabéns! Você foi aprovado.")