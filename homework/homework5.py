import numpy as np

# Question 1: The Odd Ones Out

def onlyOdd(arr):                          # returns all rows of a 2D numpy array (matrix) where all values are odd numbers
    odd_rows = []                          # initializing an empty list to store rows

    for row in arr:
        if np.all(row % 2 != 0):           # check if all elements in the row are odd
            odd_rows.append(row)           # if conditional is true then add the row to the list ('odd_rows = []')
    return np.array(odd_rows)              # convert the list of rows to a numpy array 

arr = np.array([[1, 2, 3], [5, 7, 9], [2, 4, 6], [7, 7, 7]])
result = onlyOdd(arr)
print('Question 1 Answer:')
print(result)



# Question 2.1: 

def checkerboard(n):                     # this function creates an nxn square matrix (we want an 8x8 matrix)

    board = np.empty((n,n), dtype = int)
    board.fill(0)

    return board

board = checkerboard(8)
print('Question 2.1 Answer:')
print(board)    



# Question 2.2:

new_board = checkerboard(8)
def alternating_rows(new_board):

    new_board[0:7:2, 0::2] = 1 

    return(new_board)
print('Question 2.2 Answer:')
print(alternating_rows(new_board))


# Question 2.3:

final_board = alternating_rows(new_board)

def alternating_rows_two(final_board):

    final_board[1:8:2, 1::2] = 1

    return(final_board)
print('Question 2.3 Answer:')
print(alternating_rows_two(final_board))



# Question 2.4:

def reverse_checkerboard(n):                     

    board = np.zeros((n,n), dtype = int)
    
    board[::2, 1::2] = 1
    board[1::2, ::2] = 1

    return board

board = reverse_checkerboard(8)
print('Question 2.4 Answer:')
print(board)



# Question 3

def string_number( arr, n ):
 
    print( "The original input array: \n", arr )

    if n >= 0:

        space = ''
        for i in range(n):
             space += ' '

        sep = np.array([space])

        output = np.char.join(sep, arr)
        return output
    
print('Question 2.4 Answer:')
print("The output joined array:  \n", string_number(np.array( ['galaxy', 'clusters'] ), 1))
print("The output joined array:  \n", string_number(np.array( ['galaxy', 'clusters'] ), 2))



# Question 4

np.random.seed(42)
planets = np.random.randint(100, 1000, (5, 5))
print(planets)
# print(planets.T)
# print( np.sort( planets.T[0])[-2])

def secondLargest(planets):
    planets_transpose = planets.T
    list_secondLargest = np.array([])

    for i in range(0,len(planets_transpose)):
        
        secondLargest = np.sort(planets_transpose[i])[-2]
        list_secondLargest = np.append(list_secondLargest, secondLargest)

    return list_secondLargest

print(secondLargest(planets))
    


# secondLargest(planets)
# arr = np.array([[192, 898, 747, 692, 914],
# [849, 249, 370, 658, 451],
# [802, 785, 143, 198, 616],
# [696, 926, 269, 788, 642],
# [583, 372, 468, 899, 911]])