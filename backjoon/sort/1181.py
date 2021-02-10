'''
단어 정렬
'''

import sys
n = int(sys.stdin.readline())

words = []
for i in range(n):
    word = sys.stdin.readline().strip()
    wordCount = len(word)
    words.append((word, wordCount))

words = list(set(words)) # 중복 제거

words.sort(key = lambda word:(word[1], word[0])) # count 오름차순, 사전순

for word in words:
    print(word[0])