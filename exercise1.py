def Valida_int(pergunta,min,max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
          x = int(input(pergunta))
    return x

def fatorial (num):
    '''
    Funcao que calcula o fatorial de um numero inteiro
    '''
    fat = 1
    if num == 0:
        return fat
    #so executa se num > 0
    for i in range(1, num + 1, 1 ):
        fat *= i
    return fat


x = Valida_int('Digite um valor para calcular a fatorial: ', 0, 99999)

print(f'{x}! = {fatorial(x)}')
help(fatorial)