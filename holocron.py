from chatterbot import ChatBot
chatbot = ChatBot("HOLOCRON")
from chatterbot.trainers import ListTrainer
import twitter

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

response = chatbot.get_response("fuck")
print(response)