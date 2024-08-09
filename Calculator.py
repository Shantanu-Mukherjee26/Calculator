print("~~~~~Mini Calculator~~~~~")
number1=int(input("enter a number here: "))
number2=int(input("enter another number here: "))
print("press 1 for addition \npress 2 for subtraction \npress 3 for multiplication \npress 4 for division")
choice=int(input("enter your choice from 1-4:"))

if choice==1:
  print("the addition of the two number is: ",number1+number2)
elif choice==2:
  print("the subtraction of the two number is: ",number1-number2)
elif choice==3:
  print("the multiplication of the two number is: ",number1*number2)
elif choice==4:
  print("the division of the two number is: ",number1/number2)
