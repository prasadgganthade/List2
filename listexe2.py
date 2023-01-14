#Python program to print negative numbers in a list
list1 = [11, -21, 0, 45, 66, -93]
for i in list1:
    if i < 0:
        print(i, end=" ")
print()
# using while loop
num = 0
while (num < len(list1)):
    if list1[num] < 0:
        print(list1[num], end=" ")
    num +=1
print()
#Python program to count positive and negative numbers in a list
list1 = [10, -21, 4, -45, 66, -93, 1]
positive_count = 0
negative_count = 0
for i in list1:
    if i > 0:
        positive_count += 1
    elif i < 0:
        negative_count += 1
print('Positive count is',positive_count)
print('Negative count is',negative_count)
# using while loop
num = 0
while (num < len(list1)):
    if list1[num] > 0:
        positive_count += 1
    elif list1[num] < 0:
        negative_count += 1
    num += 1
print('Positive count is',positive_count)
print('Negative count is',negative_count)
#Remove multiple elements from a list in Python
#Let’s say we want to delete each element in the list which is divisible by 2 or all the even numbers.
list2 = [11, 5, 17, 18, 23, 50]
for i in list2:
    if i % 2 == 0:
        list2.remove(i)
print(list2)
# Python | Remove empty tuples from a list
# 1. using list comprehension
"""
def remove_tuple(tuples):
    tuples = [t for t in tuples if t]
    return tuples
tuples = [(),('ram','15','8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('',''),()]
print(remove_tuple(tuples))
"""

#2. using filter method
tuples = [(),('ram','15','8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('',''),()]
"""
def remove_tuple(tuples):
    tuples = filter(None, tuples)
    return tuples
print(remove_tuple(tuples))
"""
# 3. using len function
def remove_tuple(tuples):
    for i in tuples:
        if len(i) == 0:
            tuples.remove(i)
    return tuples
print(remove_tuple(tuples))
# Python | Program to print duplicates from a list of integers
list1 = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
new_list = []
for i in list1:
    n = list1.count(i)
    if n > 1:
        if new_list.count(i) == 0:
            new_list.append(i)
print(new_list)
# level 2
#Python – Remove empty List from List
# using filter
test_list = [5, 6, [], 3, [], [], 9]
res = list(filter(None,test_list))
print(res)
# using function
def empty_list_remove(test_list):
    new = []
    for i in test_list:
        if i:
            new.append(i)
    return new
print(empty_list_remove(test_list))
# Python – Convert List to List of dictionaries
# Python3 code to demonstrate working of
# Convert List to List of dictionaries
# Using dictionary comprehension + loop

# initializing lists
test_list = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]
key_list = ["name", "number"]

# loop to iterate through elements
# using dictionary comprehension
# for dictionary construction
n = len(test_list)
res = []
for i in range(0, n, 2):
	res.append({key_list[0]: test_list[i], key_list[1] : test_list[i + 1]})

# printing result
print("The constructed dictionary list : " + str(res))
# count total number of digits using while loop
num = '56278416'
count1 = 0
while (count1 < len(num)):
    count1 += 1
print('The total numbers are',count1)

