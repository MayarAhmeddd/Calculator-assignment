
import calc
sel = True
while sel:

   print("Enter the operation you want to perform: ")
   print("1. Addition")
   print("2. Subtraction")
   print("3. Multiplication")
   print("4. Division")
 
   choice = int(input("Select 1, 2, 3 or 4:  "))

   num1 = int(input("Please enter the first number: "))
   num2 = int(input("Please enter the second number: "))



   if choice == 1:
    print(num1 , " + " ,num2, " = ", calc.add(num1, num2))

   elif choice == 2:
    print(num1 , " - " ,num2, " = ", calc.sub(num1, num2))

   elif choice == 3:
    print(num1 , " * " ,num2, " = ", calc.mult(num1, num2))

   elif choice == 4:
    print(num1 , " / " ,num2, " = ", calc.div(num1, num2))

   else:
    print("Invalid input")

   sel = input("Would you like to make another operation? ")
   if sel == "stop":
    break

    


