'''Laboratory Work 2.1
Write the code to do following:
1. Create any variable with name var1
2. Check type of var1 with type function
3. Check is var1 is True
4. Check is var1 is False
5. Create var2 that equal to (var1 or True)
6. Check is var2 is True
7. Check is var2 is False
8. Check result for var2 and var1'''

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
