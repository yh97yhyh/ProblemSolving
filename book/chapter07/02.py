'''
떡볶이 떡 만들기

Parametric Search : 최적화 문제를 결정 문제로 바꾸어 해결
원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제에 주로 사용
'''

def solution():
    pass

n, m = map(int, input().split())
tteokArr = list(map(int, input().split()))

def solution(m, tteokArr):
    answer = 0
    start = 0
    end = max(tteokArr)

    while start <= end:
        sum = 0
        mid = (start + end) // 2
        for tteok in tteokArr:
            if tteok > mid: # 떡이 더 길어야 절단
                sum = sum + (tteok - mid)

        # 떡이 많거나 같은 경우
        if sum >= m:
            start = mid + 1
            answer = mid
        # 떡이 부족한 경우
        else:
            end = mid - 1

    print(answer)

solution(m, tteokArr)