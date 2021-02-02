'''
단어 공부
'''

import sys
string = sys.stdin.readline()
string = string.upper()

stringSet = set(string) # 문자열에 포함된 문자 저장
stringSet.remove('\n')
stringSet = list(stringSet)

nums = [] # stringSet에 대응되는 문자 갯수 저장
for s in stringSet:
    nums.append(string.count(s))

# max값이 두 개 이상인지 확인
sortedNum = sorted(nums, reverse=True)
if len(sortedNum) > 1 and sortedNum[0] == sortedNum[1]: # length가 2 이상일 때!
    print('?')
else:
    answerIndex = nums.index(max(nums))
    print(stringSet[answerIndex])