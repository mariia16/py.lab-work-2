'''Write the code to do following:
1. Generate string with lowercase and uppercase alphabet plus numbers
2. Print 1st symbol of string
3. Print last symbol
4. Print 3rd from start and 3rd from the end
5. Slice first 8 symbols
6. Print only symbols with index, which divides on 3 without remaining
7. Print the symbol of the middle of the string text
8. Reverse text using slice'''


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

