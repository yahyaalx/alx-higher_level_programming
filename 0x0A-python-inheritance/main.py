#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)


-check instantiation
-check inherits from list
-check __str__
- check append()
-check print_sorted() with not sorted append
-check print_sorted() with no sorted append with negative number
-check print_sorted() with empty list
-: check print_sorted() returns a new list 