

# 2 - Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o
# programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos
# duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um
# valor "A" para A.M. e "P" para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal
# para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos
# valores de entrada todas as vezes que desejar. (0,5 ponto).

def converta(h, m):
    if 0 < h <= 12 and 0 < m < 60:
        print(f'{h}:{m} AM')
    elif 12 < h < 24 and 0 < m < 60:
        print(f'{h - 12}:{m} PM')
    else:
        print('Valor inválido')


while True:
    h = int(input('Hora: '))
    if h == 999:
        break
    m = int(input('Minuto: '))
    converta(h, m)
    print('='*12)