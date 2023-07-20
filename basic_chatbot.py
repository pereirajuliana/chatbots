from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Criando uma instância do chatbot
chatbot = ChatBot('MeuBot')

# Criando um treinador para o chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Treinando o chatbot usando o conjunto de dados em inglês
trainer.train('chatterbot.corpus.english')

# Iniciando a interação com o chatbot
while True:
    user_input = input("Você: ")
    if user_input.lower() == 'sair':
        break
    response = chatbot.get_response(user_input)
    print("Bot: ", response)
