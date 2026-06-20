# nessd loop
'''Print numbers 1 to 100:
If divisible by 3 → print “Fizz”
If divisible by 5 → print “Buzz”
If both → “FizzBuzz'''

'''
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)'''

'''Sum of Two Lists:
Given two lists of the same length, use a nested loop to calculate 
the sum of elements at corresponding positions in the two lists.

Example:

list1 = [1, 2, 3]
list2 = [4, 5, 6]


Output should be: [5, 7, 9]'''
'''
list1 = [1, 2, 3]
list2 = [4, 5, 6]

result=[]
for i in range(len(list1)):
    for j in range(len(list2)):
        if i == j:
            result.append(list1[i]+list2[j])
print(result)'''

'''Find Pairs in a List:
Write a program to find all pairs of numbers in a list whose sum is
10. You can assume the list has integers and may have duplicates.

Example input:
numbers = [2, 8, 3, 7, 4, 6]

Output should be:
(2, 8), (3, 7), (4, 6)'''
'''
numbers = [1,2,3,4,5,6,7,8,9,0]
pairs=[]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] + numbers[j] == 10:
            pairs.append((numbers[i],numbers[j]))
print(pairs)       '''

#list
'''Rotate a list to the right by 2 positions:
Example:

[1,2,3,4,5] → [4,5,1,2,3] '''
'''
list=[1,2,3,4,5]
n = 2   
rotate = list[-n:]+list[:-n]
print(list[-n:])'''

'''Find the second largest number in a list.'''

num=[1,2,3,4,5,6,7,8,9]

print(max(num))
print(min(num))







