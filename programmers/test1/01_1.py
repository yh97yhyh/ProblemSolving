'''
완전탐색
조합
상품 한개 선택했을때, 두개 선택했을때 , 세개 선택했을때 나오는 경우의 수
'''

t1 = ["XOXO", "OXXO", "XXOX", "XOOO"]
t2 = ["OXXO", "XOXO", "XXOO"]
t3 = ["OXOXO", "OOOOO", "XOXOX"]

from itertools import combinations

def check_flag(flag): # 모두 1인지 확인하는 코드, 하나라도 1이 아니면 False
    for f in flag:
        if f == 0:
            return False
    return True

def solution(table):
    answer = 1
    length = len(table)
    n = len(table[0])
    flag = [0 for _ in range(n)] # flag = [0, 0, 0, 0]
    # print(flag)
    tmp = [[0]*n for _ in range(length)] # tmp = [[0, 0, 0, 0]...] 선언
    # print(tmp)
    arr = []
    for i in range(length):
        arr.append(i)
    # print(arr) # arr = [0, 1, 2, 3]

    for i in range(len(table)): # tmp 리스트 "O" = 1로, "X" = 0 으로 치환
        for j in range(len(table[i])):
            if table[i][j] == "O":
                tmp[i][j] = 1
            elif table[i][j] == "X":
                tmp[i][j] = 0
    print("tmp : ", tmp)

    while True:
        if answer >= length:
            break

        combi = list(combinations(arr, answer)) #answer개 뽑아서 조합
        print(combi)

        for com in combi: # combi : 상품의 index
            # print("combi : ", com)
            for c in com:
                # print("tmp[c] : ", tmp[c])
                for i in range(len(tmp[c])):
                    if tmp[c][i] == 1:
                        flag[i] = 1
                    # print("flag : ", flag)

            if check_flag(flag) == True:
                return answer
            else: # flag = [0, 0, 0, 0]
                flag = [0 for _ in range(len(table[0]))]
        answer += 1

    return answer

print(solution(t1))
# print(solution(t2))
# print(solution(t3))