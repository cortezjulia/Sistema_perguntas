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
     
def printa_opcoes():
    for pergunta in perguntas:
        print(pergunta['Pergunta'])
        indice=1
        for opcao in pergunta['Opções']:
            print(f'{indice}) {opcao}')
            if opcao==pergunta['Resposta']:
                indice_resp=indice
            indice+=1
        resposta_usuario=input('Resposta: ')
        verificacao=seguranca(resposta_usuario)
        if verificacao==0:
            if resposta_usuario!=str(indice_resp):
                print('Errou','\U0001F614')
            else:
                print('Acertou','\U0001F601')
        
def seguranca(entrada):
        flag=0
        if entrada.isdigit()==False:
            print('Digite apenas números!')
            flag=1
        
            
        return flag 
        

   
       
while True:
 
    printa_opcoes()
