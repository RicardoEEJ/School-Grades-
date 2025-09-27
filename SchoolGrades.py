score = input("Enter Score: ")
sc = float(score) 
if sc>10.0 :
    print ("error")
else: 
    if sc >= (9.0):
        print(f"your grade is : A")
    elif sc >= (8.0): 
        print(f"your grade is : B")
    elif sc >= (7.0):
        print(f"your grade is : C")
    elif sc >= (6.0):
        print(f"your grade is : D")
    elif sc < (6.0):
        print (f"your grade is : F")
