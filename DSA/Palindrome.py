def check_pali(number):
    num=str(number)
    start=0
    end=len(num)-1
    for i in range(len(num)):
        if num[start]!= num[end]:
            return False
        else:
            start+=1
            end-=1
    return True

print(check_pali(1244545))
print(check_pali(124421))