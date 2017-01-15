'''Write the code to do following:
1 Generate two sets with not unique numbers and few symbols
2 Print 1st set
3 Create tuple from intersection of first and second set
4 Create tuple from difference first and second set
5 Slice first 3 symbols from first tuple
6 Print only symbols with numbers from second set
7 Reverse tuple using slice
8 Convert both tuples into list'''

import string
# Generate two sets with not unique numbers and few symbols
set1 = set(string.ascii_letters + string.digits[3:10] + string.digits[:4])
set2 = set(string.ascii_letters + string.digits[2:8] + string.digits[5:])

print(set1)	# First set
print(set2)	# Second set
#Create tuple from intersection of first and second set
tpl_intersection = tuple(set1.intersection(set2))
print(tpl_intersection)
#Create tuple from difference first and second set
tpl_diff = tuple(set1.difference(set2))
print(tpl_diff)

#Slice first 3 symbols from first tuple
print(tpl_intersection[:3])

#Print only symbols with numbers from second set
print(set(string.digits).intersection(set2))

#Reverse tuple using slice
print(tpl_intersection[::-1])

#Convert both tuples into list
print(list(tpl_intersection), list(tpl_diff))

