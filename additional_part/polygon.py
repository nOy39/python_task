from collections import *

list_of_word = ['s', 't', 'r', 'e', 's', 's']
cnt = (Counter(list_of_word))
o_cnt = OrderedDict.fromkeys('stress')
print('cnt: ', cnt)
print('o_cnt: ', o_cnt.keys())
for i in range(len(list_of_word)):
    for j in list_of_word:
        if list_of_word[i] == j:
            print(i, list_of_word[i], sep=" - ")

