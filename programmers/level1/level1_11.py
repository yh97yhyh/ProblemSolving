'''
< 서울에서 김서방 찾기 >
'''

seoul = ["Jane", "Kim"]

def solution(seoul):
    i = seoul.index("Kim")
    return ("김서방은 " + str(i) + "에 있다")

print(solution(seoul))