while True:
    print("\n","WELCOME TO THE WORLD OF CALCULATOR")
    print("")
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    print("If you want Addition type 'add'","\n","If you want Subtraction type 'sub","\n","If you want Multiplication type 'mul'","\n","If you want Division type 'div'")
    opr=input("add/sub/div/mul: ")
    if (opr=="add"):
        print("ANSWER:",a+b)
    elif(opr=="sub"):
        print("ANSWER:",a-b)
    elif(opr=="mul"):
        print("ANSWER:",a*b)
    elif(opr=="div"):
        print("ANSWER:",a//b)
    else:
        print("Invalid operation")
    i=input("Do you want to try again?....(y/n)")
    while i not in["y","n"]:
        i=input("Do you want to try again?....(y/n)")
    if i=="n":
        break
