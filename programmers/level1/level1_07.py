'''
< 문자열 내 마음대로 정렬하기 >
'''

strings1 = ["sun", "bed", "car"]
strings2 = ["abce", "abcd", "cdx"]

def solution(strings, n):
    answer = []
    strList = []
    strings.sort()

    for string in strings:
        strList.append(string[n])
    strList.sort()

    for strl in strList:
        for string in strings:
            if string not in answer and strl == string[n]:
                answer.append(string)
                break

    return answer

print(solution(strings1))
print(solution(strings2))