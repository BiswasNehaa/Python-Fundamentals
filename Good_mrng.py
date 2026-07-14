from datetime import datetime

cur_time=datetime.now().hour

if 5<= cur_time <12:
    print("good mrng")
    
elif 12 <= cur_time < 17:
        print( "Good afternoon!")
elif 17 <= cur_time < 22:
        print("Good evening!")
else:
        print( "Good night!")

