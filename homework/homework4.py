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
                                      
print('Question 2.1 Answer: ', num_list)                       

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
                                              
#num_list = [0]

# while len(num_list) <= 20:
#     num_list.append(len(num_list))


def squareList(num_list):                      # this function squares every element in num_list, [1, 2,...,20] within while loop
    factor = 2

    for i in range(len(num_list)):             # for an index in the range of len(num_list); starting at 0
        #num_list[i] **= factor                # this is shorthand for num_list[i] = num_list[i] ** factor
        num_list[i] = num_list[i] ** factor

    return num_list                            # return my final output

result_squareList= squareList(num_list)                       
print('Question 2.2 Answer: ', result_squareList)                       # print my function squareList(num_list)

########################################################################################################################################

# Slicing

def slicing_squareList(squareList):

    return squareList[0:15]
print('Question 2.3 Answer: ', slicing_squareList(result_squareList))       # NameError: name 'slicing_squarelist' is not defined 

#########################################################################################################################################

# Striding

# def striding_squareList(squareList):

#     return squareList[: : 5]              # This did not slice what I wanted it to slice because index starts at [0]; one number past desired number [0, 25, 100, 225, 400]
# print('Question 2.4 Answer: ', striding_squareList(result_squareList))

# Attempt 2
def striding_squareList(result_squareList):

    return result_squareList[4 : : 5]              # this will skip to every fifth element in my current list following from 2.3
print('Question 2.4 Answer: ', striding_squareList(result_squareList))

#########################################################################################################################################

# Slicing and Striding

def slice_n_stride_result(result_squareList):           # result_squareList is the variable that contains my saved result from problem 2.2 

    return result_squareList[21 : : -3]                 # could also de [-1 : : -3]
print('Question 2.5 Answer: ', slice_n_stride_result(result_squareList))

##########################################################################################################################################

# Creating a 5x5 2D List
x=5 

def matrix():
    outter = [] 

    for row in range(5):
        inner = []

        for num in range(1, 6):
            inner.append((row *5 + num))

        outter.append(inner)

    return(outter)

print('Question 3.1 Answer: ', matrix())  

##########################################################################################################################################

# Replacing 2D List with Multiples of 3
matrix_answer = matrix()

def multiples_of_three(input_matrix):

    for i in range(0, len(input_matrix)):
        for j in range(0, len(input_matrix[i])):

            if input_matrix[i][j] % 3 == 0:
                input_matrix[i][j] = '?'

    return (input_matrix)

new_matrix = multiples_of_three(matrix_answer)
print('Question 3.2 Answer:', new_matrix)  

##########################################################################################################################################

# Summing None- '?' Elements 

def last_matrix(matrix):
    total_sum = 0

    for row in matrix:
        for element in row:
             
             if element != '?':
                 total_sum += element

    return(total_sum)

print('Question 3.3. Answer', last_matrix(new_matrix))             
                 











