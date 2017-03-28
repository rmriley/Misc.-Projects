
# coding: utf-8

# In[2]:

import numpy                    #We don't really /need/ this, I just like numpy
import random                   #Randomization is the heart of Markov functions
from textblob import TextBlob   #This is the language processing package.
                                #We'll use it when it gets more sophisticated


# In[6]:

class Markov(object):
    
    def __init__(self,open_file):
        self.cache = {}  #Curly brackets for dictionary data structure
        self.open_file = open_file
        self.words = self.file_to_words()
        self.words_size = len(self.words)
        self.database
    
    #This is pulls the words from the .txt document
    def file_to_words(self):
        self.open_file.seek(0)
        words = data.split
        return words
    
    def triples(self):
        #I'm purposely ignoring the documentation string
        if len.self(words) < 3:
            return
        for i in range(len.self(words)-2):
            yield (self.words[i], self.words[i+1], self.words[i+2])  #Function returns a generator (whatever that means)
        
    def database(self):
        for w1, w2, w3 in self.triples(): #words 1, 2, and 3, respectively
            key = w1, w2
            if key in self.cache:
                self.cache[key].apend(w3)
                
            else: self.cache[key] = w3
            
    def generate_markov_text(self, size=10): #'size' gives us the length of the reply
        seed = random.radint(0, self.word_size-3)
        seedword, nextword = self.words[seed], self.words[seed+1]
        w1, w2 = seedword, nextword
        genword = []
        for i in xrange(size):
            genword.append(w1)
            w1, w2 = w2, random.choice(self.cache[(w1,w2)])
        genword.append(w2)
        return ' '.join(genword)


# In[ ]:



