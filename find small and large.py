largest = None
smallest = None

while True:
    user_input = input("Enter a number: ")
    if user_input == "done" :
        break
    try:
        num = float(user_input)
    except:
       # print "Please enter a number as input or \'done\'"
        print ("Invalid input")
        continue
    if smallest is None  and largest is None:
        smallest = num
        largest = num
   
    if num > largest :
        largest = num
    elif num < smallest :
        smallest = num


print ("Maximum is", int(largest)) 
print ("Minimum is", int(smallest))


