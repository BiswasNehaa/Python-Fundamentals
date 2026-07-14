# no need to add break statement   

x=int(input("enter a num :"))

match x:
    case 0:
        print("hii")
    
    case 2:
        print("Hiii 2")
        
    # Default case
    # can be multiple default case
    case _ if x!=90:
        print(x,"x is not 90")  
    
    case _ if x==90:
        print(x,"x is  90")     