numb = input("Enter a number which is to be checked for Pallindrom: ")
a = int(numb)
sum=0
while (a > 0):
    p = a % 10
    sum = (sum * 10) + p
    a = int(a/10)

if (sum == int(numb)):
    print("Yes")
else:
    print("no")
