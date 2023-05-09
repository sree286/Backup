n, s = map(int,input().split())
def findLargest(n, s):
    
    if s > 9 * n:
        return -1
    result = ''
    for i in range(n):
        if s >= 9:
            result += '9'
            s -= 9
        else:
            result += str(s)
            s = 0
        if s == 0 and i < n-1:
            result += '0' * (n-i-1)
            break
    return int(result)


print(findLargest(n, s))
