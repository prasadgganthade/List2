# Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second
l1 = [3,6,9,12,15,18,21]
l2 = [4,8,12,16,20,24,28]

print('Odd index element from list1 are :',l1[1::2])
print('Even index elemrnt from list2 are :',l2[::2])

print('Final list is',(l1[1::2]+l2[::2]))

# Exercise 2: Remove and add item in a list
print('Remove the last element from list1 :',l1.pop())
print('Insert at 0 value at 0 th index :',l1.insert(0,0))
print(l1)
print('Appending the value 0f 30 :',l1.append(30))
print('After appending 30 :',l1)

# Exercise 3: Slice list into 3 equal chunks and reverse each chunk
list1 = [11,45,8,23,14,12,78,45,89]
print('Chuk 1',list1[:3])
print('Reversing the chunk 1 :',list1[2::-1])
print('Chunk 2 :',list1[3:6])
print('Reversing the chunk 2 :',list1[5:2:-1])
print('Chunk 3 :',list1[6:])
print('Reversing hunk 3 is :',list1[8:5:-1])

# Exercise 4: Count the occurrence of each element from a list
print(list1)
count_dict = dict()
for i in list1:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] =1
print('Printing count of each dict :',count_dict)

# Exercise 5: Create a Python set such that it shows the element from both lists in a pair
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

print('First list is :',first_list)
print('Second list is :',second_list)
result = zip(first_list,second_list)
result_set = set(result)
print('The result is :',result_set)

# Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
print('Intersection is :',first_set.intersection(second_set))
intersection = first_set.intersection(second_set)

for i in intersection:
    first_set.remove(i)

print('After removig item from set1 :',first_set)

# Exercise 7: Checks if one set is a subset or superset of another set. If found, delete all elements from that set

first_set = {57, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

print('Firstset is subset of second set :',first_set.issubset(second_set))
print('Second set is subset of first set :',second_set.issubset(first_set))

print('Check for superset')
print('First set is super set of second set :',first_set.issuperset(second_set))
print('Second set is super set of first set :',second_set.issuperset(first_set))

if first_set.issubset(second_set):
    first_set.clear()
if second_set.issubset(first_set):
    second_set.clear()

print('First set :',first_set)
print('Second set :',second_set)

# Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

print('List :',roll_number)
print('Dictionary :',sample_dict)

# create new list
roll_number[:] = [item for item in roll_number if item in sample_dict.values()]
print('After removing the unwanted elements from list :',roll_number)

# Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
a = speed.values()
a = list(set(a))
print(a)

# Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
b = list(set(sample_list))
print('Unique list :',b)
c = tuple(b)
print('Tuple ',c)
print('Max :',max(c))
print('Min :',min(c))