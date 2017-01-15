##Braine academy. Python Course. Laboratory Work #2

<b>Laboratory Work #2.1.</b>
<div>
   <i>Write the code to do following:</i>
   <ol>
   1. Create any variable with name var1
   2. Check type of var1 with type function
   3. Check is var1 is True
   4. Check is var1 is False
   5. Create var2 that equal to (var1 or True)
   6. Check is var2 is True
   7.  Check is var2 is False
   8. Check result for var2 and var1
   </ol>
</div>

<h6>Here is it solution code:</h6>  
```python
# 1. Create variable with name var1
var1 = 15

# 2. Check type of var1 with type function
var_type = type(var1)
print(var_type)

# 3. Check is var1 is True
print(var1 is True)

# 4. Check is var1 is False
print(var1 is False)

# 4. Create var2
var2 = var1 or True
# in case of var1 value False or None or 0, etc we will get True else var 1
print (var2)

# 6. Check is var2 is True
print(var2 is True)

# 7. Check is var2 is False
print(var2 is False)

# 8. Check result
print(var1 and var2)
```


<b>Laboratory Work #2.2.</b>
<div>
   <i> Write the code to perform following task:</i>
   <ol>
1. Generate sequence 5 integers long from range(0, 100)
2. Generate random float 
3. Print variables above
4. Find max element from generated sequence
5. Make a floor division between max element and generated float
6. Find factorial of the result above
7. Shorten the code as much as possible
   </ol>
</div>

<h6>Here is it solution code:</h6>  

```python
# Importing modules
import math
import random

# 1. Generate sequence 5 integers long from range(0, 100)
int_seq = random.sample(range(100), 5)

# 2. Generate random float
float_random = random.random()

# 3. Print variables above
print(int_seq)
print(float_random)

# 4. Find max element from generated sequence
int_seq_max = max(int_seq)
print(max(int_seq))

# 5. Make a floor division between max element and generated float
floor_div_result = int_seq_max // float_random
print(int_seq_max // float_random)

# 6. Find factorial of the result above
print(math.factorial(floor_div_result))    
```

<b>Laboratory Work #2.3.</b>
<div>
   <i>Write the code to do following:</i>
   <ol>
    1. Generate string with lowercase and uppercase alphabet plus numbers
    2. Print 1st symbol of string
    3. Print last symbol
    4. Print 3rd from start and 3rd from the end
    5. Slice first 8 symbols
    6. Print only symbols with index, which divides on 3 without remaining
    7. Print the symbol of the middle of the string text
    8. Reverse text using slice
   </ol>
</div>

<h6>Here is it solution code:</h6>
```python
import string
# 1. Generate string with lowercase and uppercase alphabet plus numbers
text = string.ascii_letters + string.digits
print(string.ascii_letters + string.digits)

#2. Print 1st symbol of string
print(text[0])

# 3. Print last symbol
print(text[-1])	  # Last symbol

# 4. Print 3rd from start and 3rd from the end
print(text[2])  # Third from beginning
print(text[-3])    # Third from the end

# 5. Slice first 8 symbols
print(text[:8])		#  Slice of first 8 symbols

# 6. Print only symbols with index, which divides on 3 without remaining
print(text[::3]) 	# Print each 3rd symbol

# 7. Print the symbol of the middle of the string text
# First solution
print(text[int(len(text)/2):int(len(text)/2)+1])	# Counting first and last boundary
# Another solutuon
print(text[int(len(text) / 2 + 0.5)])			# Counting index

# 8. Reverse text using slice
print(text[::-1])		# Reversed text. -1 means the it will print each symbol but will start from the end because of minus
```

<b>Laboratory Work #2.4.</b>
<div>
   <i> Write the code to do following:</i>
   <ol>
   1. Generate list with lowercase and uppercase alphabet plus numbers
   2. Print 1st symbol of list
   3. Print last symbol
   4. Print 3rd from start and 3rd from the end
   5. Slice first 10 symbols
   6. Print only symbols with index, which divides on 2 without remaining
   7. Print only integer values from list
   8. Print only integer values from list * Reverse list using slice
   9. Convert base list into string
   </ol>
</div>

<h6>Here is it solution code:</h6>
```python
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

```

<b>Laboratory Work #2.5.</b>
<div>
   <i> Write the code to do following:</i>
   <ol>
   1. Create dict with 5 items, where keys will be country name and value - domain name, i.e. {Ukraine:UA}
   2. Create another dict with 5 items, where values of countries will be keys, and values will be the capitals i.e. {'UA': 'Kiev'}
   3. Add one more element to each dict above
   4. Print sentence "Domain for COUNTRY is DOMAIN." for each record in countries with the replace from dicts
   5. Print sentence "The capital of COUNTRY is CAPITAL" for each record in capitals with the replace from dicts
   6. Merge sentences above together with one cycle
   7. Add to each value of first dict another two domains: COM and GOV
   </ol>
</div>

<h6>Here is it solution code:</h6>
```python
# Mapping of coutry to their domain code
countries = {
	'Ukraine': 'UA',
	'Belgium': 'BE',
	'England': 'UK',
	'Italy': 'IT',
	'Germany': 'DE'
	}

capitals = {
	'UA': 'Kyiv',
	'BE': 'Brussels',
	'UK': 'Londan',
	'IT': 'Rome',
	'DE': 'Berlin'
	}
# add one more element to each dict above
countries['Netherlands'] = 'NL'
capitals['NL'] = 'Amsterdam'

for key, value in countries.items():
	print ("Domain for {} is {}.".format(key, value))

for key, value in capitals.items():
	print ("The capital of {} is {}".format(key, value))	

for key, value in countries.items():
	print ("Domain for {} is {}.The capital is {}".format(key, value, capitals[value]))
		
for key, value in countries.items():
	countries[key] = [value, 'COM', 'GOV']
	
for key, value in countries.items():
	print ("Domain for {} is {}.The capital is {}".format(key, value, capitals[value[0]]))
```

<b>Laboratory Work #2.6.</b>
<div>
   <i>Write the code to do following:</i>
   <ol>
  1. Generate two sets with not unique numbers and few symbols
  2. Print 1st set
  3. Create tuple from intersection of first and second set
  4. Create tuple from difference first and second set
  5. Slice first 3 symbols from first tuple
  6. Print only symbols with numbers from second set
  7. Reverse tuple using slice
  8. Convert both tuples into list
   </ol>
</div>

<h6>Here is it solution code:</h6>
```python
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
```

<b>Laboratory Work #2.7.</b>
<div>
   <i> Write the code to do following:</i>
   <ol>
  1. Write a script that creates a new output file called myfile.txt
  2. Writes the string "Hello file world!" into it
  3. Write another code that opens myfile.txt in w+ mode
  4. Read and print its contents
  5. Write into “Hello file” string new value “my” – “Hello my file”
  6. Save changes without file object close
   </ol>
</div>

<h6>Here is it solution code:</h6>
```python

# Write a script that creates a new output file called myfile.txt
f = open('myfile.txt','w')
# Writes the string "Hello file world!" into it
f.write("Hello file world!")
# Write another code that opens myfile.txt in r+ mode
f.close()

# Create file object for read and write
f = open('myfile.txt','r+')
# Read and print its contents
print(f.read())
f.seek(len("Hello "))
# Write into “Hello file” string new value “my” – “Hello my file”
f.write("my " + "file world!")
# Save changes without file object close
f.flush()
```