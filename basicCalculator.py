#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2
def add(a,b):
    return a+b
    
def substract(a,b):
    return a-b
    
def multiply(a,b):
    return a*b
    
def divide(a,b):
    try:
        return a/b
    except Exception as e:
        print(e)
        
def power(a,b):
    return a**b
    
def remainder(a,b):
    return a%b
    

#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3
def select_op(choice):
    if(choice=='#'):
        return -1
    elif(choice=='$'):
        return 0
    elif(choice in ('+','-','*','/','^','%')):
        while(True):
            num1=str(input("Enter first number: "))
            print(num1)
            if num1.endswith('$'):
                return 0
            if num1.endswith('#'):
                return -1

            try:
               num=float(num1)
               break
            except:
               print("Not a valid number,please enter again")
               conitnue
               
        while(True):
            num2=str(input("Enter second number: "))
            print(num2)
            if num2.endswith('$'):
                return 0
            if num2.endswith('#'):
                return -1

            try:
               numm=float(num2)
               break
            except:
               print("Not a valid number,please enter again")
               conitnue
#End the select_op(choice) function here
#-------------------------------------

        if choice == '+':
          print(num,"+",numm,"=",add(num,numm))
        elif choice == '-':
          print(num,"-",numm,"=",substract(num,numm))
        elif choice == '*':
          print(num,"*",numm,"=",multiply(num,numm))
        elif choice == '/':
          print(num,"/",numm,"=",divide(num,numm))
        elif choice == '^':
          print(num,"^",numm,"=",power(num,numm))
        elif choice == '%':
          print(num,"%",numm,"=",remainder(num,numm))
          
        else:
            print("Something Went Wrong")
    else:
        print("Unrecognized operation")
        
        #This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()