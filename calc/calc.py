while True:


        methods = ["plus", "minus", "multiply", "divide", "square"]


        result = 0
        calc = raw_input("Choose a calculation method (Plus, Minus, Multiply, Divide, Square): ").lower()

    
        while calc not in methods:
                print("Invalid Calculation Method")
                print("")
        
                calc = raw_input("Choose a calulation method (Plus, Minus, Multiply, Divide, Square): ").lower()
       
##Checking if you entered 5. And if so, it will only ask you for the first number.
        num1 = input("First number: ")
        if calc == "square":
                result = num1 * num1
                print(str("Result: ") + str(float(result)))
        else:
##If none of these statements above are true, it will just continue by asking you for the second number.
                num2 = input("Necond number: ")


       
        


        if calc == "plus":
                result = num1 + num2
                print(str("Result: ") + str(float(result)))
        elif calc == "minus":
                result = num1 - num2
                print(str("Result: ") + str(float(result)))
        elif calc == "multiply":
                result = num1 * num2
                print(str("Result: ") + str(float(result)))

        elif calc == "divide":
                try:
                        result = num1 / num2
                        print(str("Result: ") + str(float(result)))
                except ZeroDivisionError:
                        print("")
                        print("Error. Can't divide value by 0.")


        print("")
        again = raw_input("Do you want to Calculate again? (y/n): ").lower()
        if again != "y":
                break
print("Process Ended.")
        

