def Valida_int(pergunta,min,max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
          x = int(input(pergunta))
    return x

def existeArquivo(NomeArquivo):
    try:
        a = open(NomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def CriarAquivo(nomeAquivo):
    try:
        a = open(nomeAquivo, 'wt+')
        a.close()
    except :
        print('Erro na CRIACAO do arquivo.')
        
    else:
       print(f'Arquivo {nomeAquivo} criado com sucesso! ')

def cadastrarJogo(nomeArquivo, nomeJogo,nomeVideogame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('erro ao ABRIR o arquivo')
    else:
        a.write(f'{nomeJogo} - {nomeVideogame}\n')
    finally:
        a.close()


def listarArquivo(nomeAquivo):
    try:
        a = open(nomeAquivo, "rt")
    except:
        print('erro ao LER o arquivo')
    else:
        print(a.read())
    finally:
        a.close()

arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo LOCALIZADO no computador.')
else:
    print('Arquivo INEXISTENTE.')
    CriarAquivo(arquivo)

while True:
    print('MENU')
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastros')
    print('3 - Sair')

    op = Valida_int('Escolha a opcao desejada: ', 1, 3)
    if op == 1:#Novo item
        print('Opcao CADASTRAR novo item Selecionada...') 
        nomeJogo = input('Nome do jogo: ')
        nomeVideogame = input('Nome do Videogame: ')
        cadastrarJogo(arquivo, nomeJogo,nomeVideogame)
    elif op ==2:#Lister
         print('Opcao Listar Selecionada...\n')
         listarArquivo(arquivo)
    elif op ==3:
        print('Encerrando o Programa...')
        break