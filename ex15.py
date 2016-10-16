# Imports argv from the model or library sys
from sys import argv

# Sets the variables script and filename to arguments passed along in the terminal
script, filename = argv

# Sets the variable txt to the function open and the parameter set to the variable filename
txt = open(filename)

# Prints "Here's your file" where %r is replaced by the value of filename
print "Here's your file %r:" % filename
# Prints the variable txt with the method read
print txt.read()
txt.close()

# Prints "Type the filename again:"
print "Type the filename again:"
# Sets the variable file_again to the function raw_input and takes input from the user
file_again = raw_input("> ")

# Sets the variable txt_again to the function
txt_again = open(file_again)

# Prints the variable txt_again and the method read
print txt_again.read()
txt_again.close()
