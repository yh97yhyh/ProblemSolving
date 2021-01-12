array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print('result : {}'.format(result))
print('array : {}'.format(array))

array.sort()
print('array : {}'.format(array))

array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)

def setting2(data):
    return data[0]

result = sorted(array, key=setting2)
print(result)
