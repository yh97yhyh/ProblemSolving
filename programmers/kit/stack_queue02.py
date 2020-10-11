'''
< 기능 개발 >
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다.
각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
또, 각 기능의 개발속도는 모두 다르기 때문에
뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고,
이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.
먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와
각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때
각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

- 작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
- 작업 진도는 100 미만의 자연수입니다.
- 작업 속도는 100 이하의 자연수입니다.
- 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다.
    예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면
    배포는 2일 뒤에 이루어집니다.
'''

p1 = [93, 30, 55]
s1 = [1, 30, 5]
p2 = [95, 90, 99, 99, 80, 99]
s2 = [1, 1, 1, 1, 1, 1]
p3 = [5, 5, 5]
s3 = [21, 25, 20]
p4 = [99, 1]
s4 = [1, 99]


def solution(progresses, speeds):
    answer = []
    time = []
    for progress, speed in zip(progresses, speeds):
        if (100 - progress) % speed == 0:
            time.append(int((100 - progress) / speed))
        else:
            time.append(int((100 - progress) / speed) + 1)

    before_i = 0
    count = 0
    for i in range(len(time)):
        if i <= before_i + (count-1):
            continue
        count = 1
        for j in range(i+1, time[i]+1):
            if j == len(time) or time[j] > time[i]:
                break
            else:
                count += 1
        answer.append(count)
        before_i = i

    return answer


print(solution(p1, s1))
print(solution(p2, s2))
print(solution(p3, s3))
print(solution(p4, s4))