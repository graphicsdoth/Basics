#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from replit import clear
# clear() to clear the output in the console.
from art1 import logo
print(logo)

dict1={}
run_again = True
while(run_again):
  name = input("What is your name? :")
  bid= int(input("What is your bid amount? $"))
  again = input("Are there more bidders - Y/N")
  dict1[name]=bid
  if again=='N':
    run_again = False
    clear()
  else:
    clear()

maxi = 0.0
finalname=""
for people in dict1:
  if dict1[people]>maxi:
    maxi=dict1[people]
    finalname=people

print(f"The winner is {finalname} with a bid of {maxi} ")
print("The auction is completed")

