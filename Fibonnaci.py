numb = input("Enter number of terms in Fibonnaci Series: ")
a=int(numb)
n=0
f_term = 1
s_term = 2
print(f_term)
print(s_term)
for n in range(a):
    t_term = f_term + s_term
    print(t_term)
    f_term = s_term
    s_term = t_term
    n=n+1

print("The terms have been printed test")