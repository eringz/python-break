from nltk.chat.util import Chat, reflections

# Define possible patterns and responses
pairs = [
    (r"my name is (.*)", ["Hello %1, nice to meet you!"]),
    (r"hi|hello", ["Hello!", "Hey there!"]),
    (r"what is your name?", ["My name is Eringz."]),
    (r"quit", ["Bye-bye!"]),
    (r"Ako ay isang tagahanga mo", ["Talaga? Salamat!"])
]

# Reflections replace 'I' with 'you' and vice-versa
chat = Chat(pairs, reflections)
chat.converse()