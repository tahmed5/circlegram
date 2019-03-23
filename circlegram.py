from copy import *
import math
words = ['eennyhe', 'nillno', 'nodrco']
answers = []
word_index = 0
while words:
    shortest_word = words.pop()
    smallest_length = len(shortest_word)
    word_index += 1

    dictionary = []
    mydict = []

    with open('ukenglish.txt', 'r',encoding="Latin-1") as f:
        for word in f.read().split('\n'):
            dictionary.append(word)
            
    mydict = deepcopy(dictionary)

    max_length = smallest_length + 1 #e.g decembe = 7
    for word in dictionary:
        if len(word) > max_length:
            mydict.remove(word)
            
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

    countLetters = deepcopy(myCountLetters)

    final_words = []
    for word in countLetters.keys():
        final_words.append(word)
    final_words.remove(shortest_word)

    shortest_sum = 0
    sigma = 0

    for letter in shortest_word:
        sigma += ord(letter)
    
    for word in final_words:
        question_mark = chr(wordSum[word] - sigma)
        answers.append((word,question_mark,word_index))

for answer in answers:
    print(answer)
    



