list1 =[]
for i in range(1,101):
  if i%3 ==0 and i%5 == 0:
    print("FizzBuzz")
    x="FizzBuzz"
  elif i%3 == 0:
    print("Fizz")
    x="Fizz"
  elif i%5 == 0:
    print("Buzz")
    x="Buzz"
  else:
    print(i)
    x=i
  list1.append(x)
#print the elements of list1
list1
