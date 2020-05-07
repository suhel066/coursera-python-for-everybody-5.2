largest = None
smallest = None

while True:
    inp = input("Enter a number: ")
    if inp == "done" : break
    try:
        num = float(inp)
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


print ("Maximum is", int(largest) ) 
print ("Minimum is", int(smallest))

