'''
피보나치 수 5
10870번
'''

num = int(input())

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(num))