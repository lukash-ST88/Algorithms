# Fibonacci numbers
f1, f2 = 0, 1
n = 10
for i in range(2, n):
    f1, f2 = f2, f2 + f1
    print(f1, end=" ")








