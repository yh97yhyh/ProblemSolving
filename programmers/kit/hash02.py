'''
< 전화번호 목록 >
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.
- 구조대 : 119
- 박준영 : 97 674 223
- 지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를
그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.
'''

pb1 = ['119', '97674223', '1195524421']
pb2 = ['123', '456', '789']
pb3 = ['12', '123', '1235', '567', '88']

# 효율성 테스트 실패 (첫 번째 시도)
def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book), 1):
            if phone_book[j].find(phone_book[i]) == 0 or phone_book[i].find(phone_book[j]) == 0:
                answer = False
    return answer

# 내가 푼 답 (두 번째 시도)
def solution(phone_book):
    answer = True
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.find(p1) == 0:
            answer = False
    return answer

print(solution(pb1))
print(solution(pb2))
print(solution(pb3))

# 다른 사람의 답
def solution2(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True