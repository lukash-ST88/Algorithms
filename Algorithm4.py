# Levenshtein distance
str1 = "Привет"
str2 = "Приветк"

def dist(a, b):
    def rec(i, j):
        if i == 0 or j == 0:
            return max(i, j)
        elif a[i-1] == b[j-1]:
            return rec(i-1, j-1)
        else:
            return 1 + min(
                rec(i, j-1),
                rec(i-1, j),
                rec(i-1, j-1)
            )
    return rec(len(a), len(b))
x = dist(str1, str2)
print(x)






