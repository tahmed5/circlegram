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

def multiSum(char,shortest_word):
    sigma = 0
    shortest_word += char
    for letter in shortest_word:
        sigma += ord(letter)
    valid_ascii.append(sigma)
        
valid_ascii = []

for letter in alphabet:
    multiSum(letter,shortest_word)

myWordSum = deepcopy(wordSum)

for key,value in wordSum.items():
    if value not in valid_ascii:
        del myWordSum[key]

countLetters = {}
wordSum = deepcopy(myWordSum)
countLetters[shortest_word] = {}

for letter in shortest_word:
    if letter not in countLetters[shortest_word].keys():
        countLetters[shortest_word][letter] = 0
    countLetters[shortest_word][letter] += 1

for word in wordSum:
    countLetters[word] = {}

for word in wordSum.keys():
    for letter in word:
        if letter not in countLetters[word].keys():
            countLetters[word][letter] = 0
        countLetters[word][letter] += 1

myCountLetters = deepcopy(countLetters)

with open('dict.txt', 'w') as f:
    f.write(str(countLetters))

for word in countLetters.keys():
    for letter in countLetters[shortest_word].keys():
        try:
            if countLetters[word][letter] < countLetters[shortest_word][letter]:
                del myCountLetters[word]
                break
        except:
            del myCountLetters[word]
            break

        
print(myCountLetters)




