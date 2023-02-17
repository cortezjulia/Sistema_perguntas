# Exercício - sistema de perguntas e respostas
import emoji

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
    




#serve para imprimir indice e conteudo
#for chave,valor in perguntas.items():
 #   print(chave,valor)

   


 
def printa_opcoes():
    indice=1
    for valor in perguntas['Opções']:
        print(f'{indice}) {valor}')
        indice+=1

def avalia_resposta():
    resposta_usuario=input('Resposta: ')
    
    if resposta_usuario!=perguntas['Resposta']:
        print('Errou','\U0001F614')
    else:
        print('Acertou','\U0001F601')
    
for pergunta in perguntas:
    print(pergunta['Pergunta'])
    printa_opcoes()
    avalia_resposta()