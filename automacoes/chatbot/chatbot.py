# O codigo não está mais funcionando, uma vez que a API em que ocorria a conexão se tornou paga ->
# não é mais possivel utilizar o chatbot atraves da conexão pela API
'''
Documentação: https://platform.openai.com/docs/api-reference/introduction
'''


import openai
import requests
from keys import OPENAI


# !pip install openai==0.28
# !pip install requests

# 1 - Acessando a API 

openai.api_key=OPENAI

# 2 - Função para gerar texto a partir do modelo de linguagem

def gera_texto(texto):
    
    response = openai.Completion.create(
        
        # Modelo usado (https://platform.openai.com/account/limits)
        engine = 'text-davinci-003',
        
        # Texto inicial da conversa com o chatbot
        prompt = texto,
        
        # Comprimento máximo da resposta gerada pelo modelo
        max_tokens = 150,
        
        # Quantas conclusões para cada prompt
        n = 5,

        # Uma medida da aletoriedade de um texto gerado pelo modelo. (0-1)
        # Valores próximos a 1 significam que a saida é a mais aleatória, enquanto valores proximos a 0 significam que a saída é muito identificável.
        temperature = 0.8,
            
        stop = None,
    )

    return response.choices[0].text.strip()

def main():
    print('\nBem-vindo ao chatbot criado com API do GPT-3')
    print('(Digite "sair" a qualquer momento para encerrar o chat)')
    
    while True:
        
        user_message = input('\nVocê: ')
        
        if user_message.lower() == 'sair':
            break
        
        gpt3_prompt = f'\nUsuário: {user_message}\nChatbot:'
        
        chatbot_response = gera_texto(gpt3_prompt)
        
        print(f'\nChatbot: {chatbot_response}')
        
if __name__ == '__main__':
    main()