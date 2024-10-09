# Problem 1: Oski Stole Your Power
def computePower(x, y): 
    ans = 1              # ans here is a variable; making it 1 because everytime I run loop, I multiply loop to ans
    while y > 0:
        ans = ans * x    # redefining ans; ans is the variable that has my answer (function that can compute x^(y))
        y -= 1           # this is shorthand to saying y = y -1
    return ans           # here's my final output
print(computePower(2,3))





# Problem 2: What Should I Wear?
readings = [15, 14, 17, 20, 23, 28, 20]

def temperatureRange(readings):
    minimum = 2000              # want to pick a number for minimum that is obviously out of range for ease; positive because of conditional

    for reading in readings:    # here 'reading' is used because it makes intuitive sense (it could be anything), an index in our object 

        if reading < minimum:   # if an index in our object is less than minimum, where minimum = 2000
            minimum = reading   # then the minimum (redifining minimum in line 18) is now equal to that index 

    maximum= -2000              # want to pick a number for maximum that is obviously out of range for ease; negative because of conditional

    for reading in readings:    

        if reading > maximum:   
            maximum = reading   

    return (minimum, maximum)   # this will return the minimum and maximum in our list, stored from the values found in our for loops          

print(temperatureRange(readings))





# Problem 3: Check if its the Weekend
def days(x):                    # x here is an arbitrary input 
    if x == 6 or x == 7:        # == used here because we're checking an equality
        return True
    else: 
        return False
print(days(4)) 
print(days(6))
print(days(7))





# Problem 4: Fuel Efficiency Calculator
def fuel_efficiency(distance, fuel):   # distance in miles, fuel in gallons     
    return (distance / fuel)           
print(round(70 / 21.5, 2))             # returns a float that is rounded (specified number, specified number of decimals) 





# Problem 5: Secret Code
#def decodeNumbers(n):                              

#    while n > 0:                        # loop until n becomes zero (NEED DIFFERENT CONDITION)
#        ans = ans * ( n % 10 )          # multiply ans = 1  by the last digit of n; remainder of dividing by 10 is always the last digit     
#        n //= 10                        # remove the last digit of n using floor division; n //= is shorthand for n = n // 10
    
#    if ans is n:
#        sum(n) + ans
        

#    return ans
#print(decodeNumbers(12345))             # this gives me 120 because it multiplies each digit by the next :/ ????
#                                        # want to stop at first iteration if n = 12345 --> ans = 1 * 5 = 5, n = 1234
#                                        # second iteration --> ans = 5 * 4 = 20 ...


def decodeNumbers(n):                # this function will take the last digit of a positive number and bring it to the front, then add the original sign of the number at the end if negative

    if n < 0:                        # first it checks if the number is negative  
        sign = -1                    # if n is negative, we store the negative sign in the variable 'sign' (i.e. remember it was negative)                               
        n = -n                       # work with the positive version for now
        
    else:                            
        sign = 1                     # if n is positive or zero store 1 in 'sign'

    if n < 10: 
        return n                     # single digit numbers remain unchanged

    last_digit = n % 10              # gives you the last digit of n  (i.e. 12345 % 10 = 5)
    remaining_digits = n // 10       # removes the last digit of n (i.e. n= 12345 // 10 = 1234)

    num_digits = 1                      # remaining_digits has 1 less number because its accounted for in last_digit
    temp = remaining_digits             # temporary copy for counting (want outside of while loop so we don't change our original remaining_digits)
    while temp >= 10:                   # loop as long as n is not a single digit number
        temp //= 10                     # this is extracting the last digit in each iteration and updating temp
        num_digits += 1                 # num_digits = num_digits + 1;keeps track of how many digits are removed from temp (i.e. 1st iteration: num_digits = 2)

    return sign * (last_digit * 10**num_digits + remaining_digits)           
# 10**num_digits ensures we shift the correct number of places

print(decodeNumbers(12345))




# Problem 6: Min & Max but With Loops!
# 6.1 For Loops
nums = [2024, 98, 131, 2, 3, 72]

def extrema(nums):                    # here I define my function as extrema with object being my desired inputs
    minimum = 100000                  # don't add a comma between numbers or will receive error (why?)

    for num in nums:                  # for an index (num) in my object (nums) 
     
        if num < minimum:
            minimum = num             # redifine num as my "new minimum" if it meets condition, num < minimum

    maximum = -100000                  

    for num in nums:

        if num > maximum:
           maximum = num
                                         
    return (minimum, maximum)         # this returns the minimum and maximum values in 'nums' as defined by our 'for' loops

print(extrema(nums))                  





# 6.2 While Loops
nums = [2024, 98, 131, 2, 3, 72]

i = len(nums) - 1              # initialize 'i' to the index of the last element of list 'nums' (5); len(nums) gives total number of elements (6)
count = -100000                # initialize 'count' to a very small number; this variable will be used to store the maximum value found so far 

while i >= 0:                  # loop through list 'nums' as long as condition is true
    if nums[i] >= count:       # check if the element at index 'i' (the last element) is greater than or equal to count  (1st iteration 72 >= 100000)
        count = nums[i]        # if the condition is true, update 'count' to the value of the element at index 'i' (last element, 72)
    i -= 1                     # decrement 'i' by 1; this moves the index to the next-to-last element (i.e. 72 >= 3, 3 >= 2,..)

print(count)                   # this gives me my MAXIMUM 

count = 100000                 # re-initialize 'count' to a very large number; this variable will be used to store the minimum value found so far              
i = 0                          # re-intialize 'i' to the index of the first element of list 'nums'

while i < len(nums):                   
    if nums[i] <= count:       # check if the element at index 'i' (the first element) is less than or equal to count (1st iteration 2024 <= 100000)
        count = nums[i]        # update 'count' if a smaller value is found (first element 2024)
    i += 1                     # increment 'i' by 1; this moves the index to the next element 

print(count)                   # this gives me my MINIMUM





# Problem 7: Counting Vowels
def vowel_and_consonant_count(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char in vowels:
            vowel_count += 1                 # if the character is a vowel this increments the vowel_count by 1

        elif char.isalpha():                 # elif means else if; this checks if a character is a letter (uppercase and lowercase)
            consonant_count += 1             

    return vowel_count, consonant_count

text = "UC Berkeley, founded in 1868!"
print(vowel_and_consonant_count(text))       # this returns (8,11)





# Problem 8: Calculate Digital Root 
def digital_root(num): 
    ans = 0

    while num > 0:                           # this ensures the loop only runs until we run out of digits to iterate; num = 0 ends loop and returns sum
        ans += num % 10                      # this takes the last digit of num and adds it to current value of ans above while loop 
        num //= 10

    return ans
print(digital_root(2468))                