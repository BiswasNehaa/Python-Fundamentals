def check_armstrong(num):
    s=str(num)
    n=len(s)
    sum=0
    for i in range(n):
        sum=pow(int(s[i]),n)+sum
    if sum==num:
        return True
    else:
        return False
    
print(check_armstrong(153))
print(check_armstrong(2553))