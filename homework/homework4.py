# Making a List Variable

#num_list = [0]
#if 0 == 0:
#    num_list += 1              # TypeError: 'int' object not iterable; I am getting an error because my list only has a literal (0) 

#elif num_list <= 20:           # this never executes even without TyperError because 0 == 0 is always true 
#    num_list = num_list        # this does not not do anything

#print(num_list)


## (attempt 2)                        # to fix TypeError and execute this code through the end I used len() to return the number of elements in my list 

num_list = [0]

while len(num_list) <= 20:            # this while loop says to check the last element of num_list until the number is less than or equal to 20
    num_list.append(len(num_list))    # if this is true, .append() adds an element to the end of num_list until it reaches 20         
                                      
print(num_list)                       

########################################################################################################################################

# Working with List Elements
#num_list = [0]

#while len(num_list) <= 20:
#    num_list.append(len(num_list))


#def squareList(num_list):                     # this function squares every element in num_list, [1, 2,...,20]
#    factor = 2
    
#    for i in range(len(num_list)):            # for an index in num_list starting at 0
#            num_list[i] **= factor            # this is shorthand for num_list[i] = num_list[i] ** factor


#print(num_list)

# this printed num_list again, which is not what I wanted
# will indent def squareList(num_list) inside the while loop to fix

## (attempt 2)
                                              
num_list = [0]

while len(num_list) <= 20:
    num_list.append(len(num_list))


    def squareList(num_list):                     # this function squares every element in num_list, [1, 2,...,20] within while loop
        factor = 2
    
        for i in range(len(num_list)):            # for an index in the range of len(num_list); starting at 0
            num_list[i] **= factor                # this is shorthand for num_list[i] = num_list[i] ** factor

print(num_list) 
# same result as before nothing changed

########################################################################################################################################







