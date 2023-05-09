def combinations(k,n,start=1):
    res = []
    
    if k<1:
        if n==0:
            return [start-1]
        elif n<0:
            return 1
        return 0
    
    for i in range(start,10):
        temp = [i]
        combo = combinations(k-1,n-i,i+1)
        if combo:
            if combo==1:
                return 0
            if k==1:
                return [combo]
            else:
                for l in combo:
                    res.append(temp+l)

    return res
            
            