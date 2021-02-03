'''
그룹 단어 체커
'''

import sys

n = int(sys.stdin.readline())

words = []
for i in range(n):
    word = sys.stdin.readline()
    word = word.replace('\n', '')
    words.append(word)

count = n # 모두 그룹 단어라고 가정

for word in words:
    for w in word:
        if word.rfind(w) - word.find(w) > 1:
            cutted = word[word.find(w):word.rfind(w)]
            if cutted.count(w) == len(cutted):
                continue
            else: # 그룹 단어가 아님 ex)cca'zzzz'bb가 여기서 걸러진다
                count -= 1
                break

print(count)





