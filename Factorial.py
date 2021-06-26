def factorial():
    numb = input("Enter the number for which you want the factorial: ")
    a=int(numb)
    prod =1
    for n in range(1,a+1):
         prod = n*prod
    print(prod)

factorial()
repeat = input("Want to try again (enter Yes/No): ")
if(repeat == "Yes"):
    factorial()
else:
    print("The program ends")