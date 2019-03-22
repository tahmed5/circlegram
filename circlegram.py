from copy import * 
words = ['decembe', 'februay', 'octobe']
dictionary = []
mydict = []

with open('english2.txt', 'r') as f:
    for word in f.read().split('\n'):
        dictionary.append(word)
        

smallest_length = 10000000
shortest_word = ''
for word in words:
    if len(word) < smallest_length:
        smallest_length = len(word)
        shortest_word = word

print(shortest_word,smallest_length)

mydict = deepcopy(dictionary)
print(len(mydict))

max_length = smallest_length + 1 #e.g decembe = 7
for word in dictionary:
    if len(word) > max_length:
        mydict.remove(word)
print(len(mydict))

alphabet = []
for letter in range(97,123):
    alphabet.append(chr(letter))

unique_letters = []
for word in words:
    for letter in word:
        if letter not in unique_letters:
            unique_letters.append(letter)
wordSum = {}

for word in mydict:
    sigma = 0
    for letter in word:
        sigma += ord(letter)
    wordSum[word] = sigma

print(wordSum['october'])



