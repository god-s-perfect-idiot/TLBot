from chattymarkov import ChattyMarkov

markov = ChattyMarkov("memory://")

#markov.learn("Hello World")
print(markov.generate())
