#To evaluate if a number is even number or odd number

#Request the information we will work
print("Hey there let's review if the number you provide is even number or odd number.")
number = int(input("Could you please provide a natural number? "))

if number == 1 or number == -1:
    print("Come on men we all know that 1 and -1 are odd numbers")

else:  
    remainder = number % 2

#Based on the evaluation we can conclude using the following
    if remainder >= 1:
        print ("This is a odd number, because it can't be divisible by 2  without leaving a remainder.")
#elif remainder == 1:
#    print("Come on men, all we known number 1 us a odd number")
    else:
        print("This is a even number because the whole number is divisible by 2.")