# Empty list called my_list
my_list = []

# Appending items to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print('Appended items: ',my_list)

# Inserting item to my_list
my_list.insert(1,15)
print('Inserted 15 at the second position: ',my_list)

# Extending my_list with another list
another_list = [50,60,70]
my_list.extend(another_list)
print('Extended list with 50,60,70: ',my_list)

# Removing the last element from my list
my_list.pop()
print('Removed the last item from the list: ',my_list)

# Sorting my_list in ascending order
my_list.sort()
print('Sorted list in ascending order',my_list)

# Finding and printing the index of value 30
print('Printing the index of 30: ',my_list.index(30))