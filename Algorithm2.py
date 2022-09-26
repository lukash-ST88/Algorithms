# factorial function
num = 5
def factorial(n):
    if n == 0:
        return 1
    f = 1
    i = 1
    while i <= n:
        f = f * i
        i += 1
    return f
x = factorial(4)
print(x)
