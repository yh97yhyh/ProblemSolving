'''
컵홀더
'''

n = int(input())
seats = input()

count = seats.count('S')
count += seats.count('LL')

answer = count + 1

if answer > n: # 사람 수보다 컵홀더 수가 더 많을 때
    answer = n
print(answer)