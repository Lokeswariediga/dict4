# 1. Invert a dictionary with list values (group keys by their values) 
# d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
res={}
for x,y in d.items():
    res.setdefault(y,[]).append(x)
print(res)
# Output: 
{1: ['a', 'c'], 2: ['b'], 3: ['d']} 


# 2. Find Max and Min Value in Dictionary 
# Input: 
# d = {'a': 10, 'b': 5, 'c': 15} 
d = {'a': 10, 'b': 5, 'c': 15} 
print ("max",max(d.values()))
print ("min",min(d.values()))
# Output: 
Max Value → 15 
Min Value → 5 


# 3. Create a dictionary using dictionary comprehension for the given list of numbers, 
# where: 
#  Each number is a key.   
# The value is "prime" if the number is prime. 
# The value is "notprime" if the number is not prime.
temp={x:"prime" if all (x%y!=0 for y in range(2,x)) else "Not prime" for x in range(2,7)}
print(temp)
# Output:   
{2: 'prime', 3: 'prime', 4: 'notprime', 5: 'prime', 6: 'notprime'} 


# 4. Create a dictionary from a list of words, keys as words, values as word lengths, but 
# only for words   longer than 3 characters 
# List: ["hi", "hello", "world", "is", "great"] 
List=["hi", "hello", "world", "is", "great"] 
res={M:len(M) for M in List if len(M)>3}
print(res)
# output:
{'hello': 5, 'world': 5, 'great': 5}

# 5. Create a dictionary with uppercase letters as keys and their ASCII values as values use 
# dict     
# Input:    letters = ['a', 'b', 'c'] 
letters=['a','b','c']
res={chr(ord(i)-32):ord(i)-32 for i in letters}
print(res)
# Output: 
{'A': 65, 'B': 66, 'C': 67} 


# 6. Explain about setdefault function in dictionary data type ? 

 The setdefault() function in Python is a built-in dictionary method used to get the value of a key if it exists in the dictionary, and set it with a default value if it does not exist.
 Syntax:
dictionary.setdefault(key, default_value)
1.key: The key to check in the dictionary.
 2.default_value (optional): The value to set if the key is not found. If not provided, defaults to None.


# 7. Difference between d[key] and d.get(key)?
 d[key]:
 1.Raises an error if the key is not present in the dictionary.
 2.It is a direct way to access values.

 d.get(key)
1.Returns None if the key is not present, instead of raising an error.
2.You can also specify a default value: d.get(key, default_value)


# 8. What is the difference between Shallow Copy and Deep Copy in Python? Explain with 
# examples. 
Shallow Copy:
1.Creates a new object, but does not create copies of nested objects.
2.The nested objects are referenced, not copied.
3.Changes made to nested objects in the original or the copy affect both.

Example of Shallow Copy:
list1 = [[1, 2], [3, 4]]
shallow_copy = copy.copy(list1)

shallow_copy[0][0] = 100

 Deep Copy:
1.Creates a new object and recursively copies all nested objects.
2.Changes to nested objects in the copy do not affect the original.

 Example of Deep Copy:
list1 = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(list1)

deep_copy[0][0] = 100
