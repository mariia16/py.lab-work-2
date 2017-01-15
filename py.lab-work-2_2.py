'''Write the code to perform following task:
1. Generate sequence 5 integers long from range(0, 100)
2. Generate random float
3. Print variables above
4. Find max element from generated sequence
5. Make a floor division between max element and generated float
6. Find factorial of the result above
7. Shorten the code as much as possible'''

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

