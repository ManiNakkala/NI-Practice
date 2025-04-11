def fab(n):
    if n<=0:
        return 0
    elif n == 1:
        return 1
    else:
        return fab(n-1) + fab(n-2)
n = int(input())
print(fab(n),end="")