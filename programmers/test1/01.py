...

...

t1 = ["XOXO", "OXXO", "XXOX", "XOOO"]
t2 = ["OXXO", "XOXO", "XXOO"]
t3 = ["OXOXO", "OOOOO", "XOXOX"]

def solution(table):
    l = len(table[0])
    answer = []
    for t1 in table:
        temp = [0 for i in range(l)]
        cnt = 0
        for i in range(l):
            if t1[i] == "O":
                temp[i] = 1
        for t2 in table:
            if t1 == t2:
                continue
            cnt += 1
            for j in range(l):
                if t2[j] == "O":
                    temp[j] = 1
            if temp == [1 for i in range(l)]:
                answer.append(cnt)

    return answer


print(solution(t1))
print(solution(t2))
print(solution(t3))