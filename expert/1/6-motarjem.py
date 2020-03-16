from functools import reduce # these two library make list flat (between [......])
from operator import concat
number = int(input())
list_of_word = list()
list_of_sentence = list()
list_translate = list()
n=1

while n <= number:
    word = str(input())
    list_of_word.append(word.split())
    n=n+1
flat_list = reduce(concat, list_of_word)

sentence = str(input())
list_of_sentence.append(sentence.split())
flat_sentence = reduce(concat, list_of_sentence)

for letter in flat_sentence:
    for param in flat_list:
        if letter==param :
            temp = (flat_list.index(param))%4
            result = flat_list.index(param)-temp
            list_translate.append(flat_list[result]+ " ")
            flat_translate = reduce(concat, list_translate)
        elif (letter in flat_sentence) and (letter not in flat_list) and (letter not in flat_translate) :
            list_translate.append(letter + " ")
            flat_translate = reduce(concat, list_translate)

print(flat_translate)
