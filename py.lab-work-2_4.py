'''Write the code to do following:
1. Generate list with lowercase and uppercase alphabet plus numbers
2 Print 1st symbol of list
3 Print last symbol
4 Print 3rd from start and 3rd from the end
5 Slice first 10 symbols
6 Print only symbols with index, which divides on 2 without remaining
7 Print only integer values from list
8 Reverse list using slice
9 Convert base list into string'''


import string
# Generate list with lowercase and uppercase alphabet plus numbers
lst = list(string.ascii_letters + string.digits)
print(list(string.ascii_letters + string.digits))

#Print 1st symbol of list
print(lst[0])
#Print last symbol
print(lst[-1])

#Print 3rd from start and 3rd from the end
print(lst[2])      #3rd from start
print(lst[-3])    # Third from the end

#Slice first 10 symbols
print(lst[:10])
#Print only symbols with index, which divides on 2 without remaining
print(lst[::2]) 	# Print each 2nd symbol

# Print only integer values from list
int_lst = []
for i in lst:
    try:
        int_lst.append(int(i)) # Only integer can be converted here
    except:
        pass
    
print(int_lst)
print(int_lst[::-1])

print("-".join(lst))  # String from list

