#A simple calculator program 
import os

while True:
# print options for user
    print('1. Enter an equation')
    print('2. Read equations in equations.txt file')
    print('3. Quit')
#ask user to choose option
    choice = input("Enter option 1, 2 or 3: ")
#if user selects incorrect option ask them to try again
    if choice not in ('1', '2', '3'):
        print('Please enter valid option')
        continue
# if user chooses to enter an equation, option 1
    elif choice == '1':
#run loop indefinitely
        while True:
            try:
# ask user to select numbers and operator
                a = int(input('Please enter a number: '))
                b = int(input('Please enter another number: '))
                break
#if they don't input a correct character print error
            except Exception:
                print('Not a valid number. Please try again...')
        
        while True:
            oper = input('Please enter an operator +, -, * or /: ')
            if oper not in ('+', '-', '*', '/'):
                print('Please select a valid operation.')
#if the user tries to divide by zero print error message
            elif oper == '/':
                try:
                    answer = round((a / b), 2)
                except ZeroDivisionError:
                    print("Error: Cannot divide by zero")

            else:
                break

# do the requested operatipn and save result as 'answer'
        if oper == '+': answer = (a + b)
        elif oper == '-': answer = (a - b)
        elif oper == '*': answer = (a * b)
        elif oper == '/': answer = round((a / b),2)
# format the equation as a string to print
        equation = str(a) +' '+ oper + ' ' + str(b) + ' = ' + str(answer)
# if the file does not exist create and write the equation to the text file
        if not os.path.exists('equations.txt'):
# open file in append mode and write equation to file followed by a new line and close file
                with open('equations.txt', 'a')as file:
                    file.write(str(equation) + '\n')
                    file.close()
                    continue
# open file in append mode and write equation to file followed by a new line and close file
        with open('equations.txt', 'a') as file:
            file.write(str(equation) + '\n')
            file.close()
# if user chooses to open the file, option 2
    elif choice == '2':
# ask user to enter the name of the file to open    
        file_name = input("Enter the file name: ")
#set file to none to be used in final block
        file = None
           
        try:
# open file in read only mode and print the contents of the file
            with open(file_name, 'r') as file:
                contents = file.read()
                print(contents)
                break
# if the file name don=esn't exist the print error
        except FileNotFoundError as error:
            print("The file that you are trying to open does not exist")
            print(error)
# if file is found, or not then close it
        finally:
            if file is not None:
                file.close()
            continue
 # if user chooses option 3, exit program   
    elif choice == '3':
        print("Good Bye !")
        break

