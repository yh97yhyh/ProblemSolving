'''
< 스킬트리 >
'''

s = "CBD"
st = ["BACDE", "CBADF", "AECB", "BDA"]

def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skillList = list(skill)

        for s in skill_tree:
            if s in skill:
                if s != skillList.pop(0):
                    break
        else:
            answer += 1

    return answer

print(solution(s, st))