'''Write the code to do following:
1 Write a script that creates a new output file called myfile.txt
2 writes the string "Hello file world!" into it
3 write another code that opens myfile.txt in w+ mode
4 read and print its contents
5 write into “Hello file” string new value “my” – “Hello my file”
6 Save changes without file object close'''

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

