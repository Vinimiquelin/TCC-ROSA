import nltk
#nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import pickle
import numpy
import tflearn
import tensorflow
import random
import json

with open("intents.json") as file:
    data = json.load(file)

with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)

# load our saved model
net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)
model.load('./model.tflearn')

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
           if w == se:
               bag[i] = 1

    return numpy.array(bag)

def chat(text):
    results = model.predict([bag_of_words(text, words)])[0]
    #print(results) # To see the probabilities of the neural network's decision
    results_index = numpy.argmax(results)
    tag = labels[results_index]
    # print(tag) # To see the tag that the neural network is predicting

    if results[results_index] > 0.7:
        for tg in data["intents"]:
            if tg["tag"] == tag:
                responses = tg["responses"]

        return random.choice(responses)

    else:
        tag = "semresposta"
        for tg in data["intents"]:
            if tg["tag"] == tag:
                responses = tg["responses"]

        return random.choice(responses)