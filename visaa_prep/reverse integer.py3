def reverseInteger(n):
    if n==0:
        return 0
    sign = -1 
    if n<0: 
        else:
            return 1
        n=abs(n)
        reversed_n=int(str(n)[::-1])
        if reversed_n>2**31-1:
            return sign * reversed_n
        
