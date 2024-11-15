def reverse_integer(n):
    int_min, int_max=-2**31, 2**31 -1
    sign = -1 if n<0 else 1
    reversed_n=int(str(abs(n))[::-1]) * sign
    if reversed_n < int_min or reversed_n > int_max:
        print(0)
    else:
        print(reversed_n)
n=int(input().strip())
reverse_integer(n)
