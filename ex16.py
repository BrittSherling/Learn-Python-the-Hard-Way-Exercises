# From sys Module or Library import argv
from sys import argv

# Set variables script and filename to the input from the user command aruguments
script, filename = argv

# Prints "We're going to erase" where %r is the variable filename
print "We're going to erase %r." % filename
# Prints "If you dont want that, hit CTRL-C (^C)"
print "If you dont want that, hit CTRL-C (^C)."
# Prints "If you do want that, hit RETURN"
print "If you do want that, hit RETURN."

# Gets input from the user and has the placeholder '?'
raw_input("?")

# Prints "Opening the file..."
print "Opening the file..."
# Sets the variable target equal to the function open(filename, 'w') 'w being for writing'
target = open(filename, 'w')

# Prints "Truncateing the file. Goodbye!"
print "Truncateing the file. Goodbye!"

# Prints "Now i'm going to ask you for three lines."
print "Now i'm going to ask you for three lines."

# Sets the variable line1 equal to the input from the user with the placeholder "line 1:"
line1 = raw_input("line 1: ")
# Sets the variable line1 equal to the input from the user with the placeholder "line 2:"
line2 = raw_input("line 2: ")
# Sets the variable line1 equal to the input from the user with the placeholder "line 3:"
line3 = raw_input("line 3: ")

# Prints "I'm going to write these to the file."
print "I'm going to write these to the file."

# Takes the variable target and uses the write function to write in line1, line2, line3 with a new line between each
target.write("%s \n %s \n %s \n" % (line1, line2, line3))

# Prints "And finally, we close it."
print "And finally, we close it."
# takes the variable target and uses the close function to close the document
target.close()
