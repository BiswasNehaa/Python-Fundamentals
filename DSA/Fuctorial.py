def Fact(num):
    if num==0 or num==1:
        return 1
    return num*Fact(num-1)
        
print(Fact(5)) 