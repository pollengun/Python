present_students=input("Enter the number of students in the class: ")
present_students = int(present_students)
no_of_desk = 14
max_per_desk = 3
if present_students > no_of_desk * max_per_desk:
    print("You need more desks")
elif present_students < no_of_desk:
    print("You have enough desks(decrease the no. of desks accordingly)")
else:
    if present_students % no_of_desk == 0:
        print("Desks can be filled with equal number of students")
    elif present_students % no_of_desk != 0:
        print("Desks can't be filled with equal number of students")    
    

 
