print("MINI CALCOLAROR")
num1 = float(input("Enter first number here :"))
num2 = float(input("Enter second number here :"))

print("press 1 for addition \n press 2 for subtraction \n press 3 for multiplication \n press 4 for division ")

choice = int(input("Enter your choice from 1--4: "))

if choice == 1:
    print("The addition of given pip number  is",num1 + num2)
elif choice  == 2:
    print("The subtraction of given number is",num1 - num2) 
elif choice  == 3:
    print("The multiplacation of given number is",num1 * num2) 
elif choice  == 4:
    print("The division of given number is",num1 / num2)   
else:
    print("Invalid input12")        
      