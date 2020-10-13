'''
< 다리를 지나는 트럭 >
'''

bl1, w1, tw1 = 2, 10, [7,4,5,6]
bl2, w2, tw2 = 100, 100, [10]
bl3, w3, tw3 = 100, 100, [10,10,10,10,10,10,10,10,10,10]

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0 for i in range(bridge_length)]

    while bridge:

        time += 1
        bridge.pop(0)

        if truck_weights:
            if truck_weights[0] + sum(bridge) <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return time


print(solution(bl1, w1, tw1))
print(solution(bl2, w2, tw2))
print(solution(bl3, w3, tw3))