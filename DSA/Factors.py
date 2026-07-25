from math import sqrt
def Factors(num):
    print("Brute force")
    result=[]
    for i in range(1,num+1):
        if num%i ==0:
            result.append(i)
    return result

def better_Factors(num):
    print("better than Brute force")
    result=[]
    for i in range(1,num//2+1):     
        if num%i ==0:
            result.append(i)
    result.append(num)
    return result

def opti_Factors(num):
    print("Optimal soln")
    result=[]
    for i in range(1,int(sqrt(num))+1):     # loop rum half the num... after half no factors
        if num%i ==0:
            result.append(i)
            if i != num//i:
                result.append(num//i)
    result.sort()
    return result

print(Factors(20))
print(better_Factors(20))
print(opti_Factors(20))