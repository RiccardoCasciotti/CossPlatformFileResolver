import controller as cont

while True:
    path = input("\nInsert the root folder to be analyzed recursively: ")
    path = path.replace("'","")
    print("\nThe root folder to be analyzed is: " + path)
    res1 = input("\nDo you wish to continue? (y or n): ")
    if res1 == "y":
       
       cont.controller(path)
       break
    elif res1 == "n":
        res2 = input("\nDo you wish to insert the root directory again? (y to continue or n to exit the program): ")
        if res2 == "y":
            continue
        else:
            break

print("\n Program terminated\n")