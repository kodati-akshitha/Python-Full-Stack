#List Built-in Functions
list1=[10,40,30,70,60,90]

#len()
print(len(list1))

#max()
print(max(list1))

#min()
print(min(list1))

#sum()
print(sum(list1))

#sorted()
print(sorted(list1))

#list()
print(list("Akshitha"))
#List Built-in methods

lst=[10,20]
print("Original List: ",lst)

#appending element to a list
lst.append(30)
print("After Appending: ",lst)

#extending the list with another sublist
lst.extend([40,50])
print("After extending: ",lst)

#inserting an element at a specified position
lst.insert(1,10)
print("After inserting: ",lst)

#removing the first occurance of an element
lst.remove(10)
print("After removing: ",lst)

#poping the element using index
lst.pop(4)
print("After popping: ",lst)

#clearing the element in the list
lst.clear()
print("After Clearing: ",lst)

lst.extend([10,40,20,40,30,40])
print("After Recreation: ",lst)

#searching the element using index
print(lst.index(20))

#counting the occurances
print(lst.count(40))

#sorting the list
lst.sort()
print("After sorting: ",lst)

#reversing the list
lst.reverse()
print("After reversing :",lst)

lst.copy()
print(lst)

del lst
#Lists and the operations on lists

numbers=[10,20,30]
print(numbers,type(numbers)) # Output: [10, 20, 30] <class 'list'>

#Concatenation
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c) # Output: [1, 2, 3, 4, 5, 6]

#Repetition
print(a*3) # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

#Indexing
print(numbers[0]) # Output: 10 (1st element)
print(numbers[-1]) # Output: 30 (last element)
print(numbers[2])

#Slicing
print(numbers[0:2]) # Output: [10, 20] (from index 0 to 1)
print(numbers[:2]) # Output: [10, 20] (default start is 0)
print(numbers[1:3]) # Output: [20, 30] (from index 1 to 2)
print(numbers[::-1]) # Output: [30, 20, 10] (reversed list)

#Membership Operators
print(20 in numbers) # Output: True
print(40 not in numbers) # Output: True