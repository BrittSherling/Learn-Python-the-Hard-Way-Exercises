# A variable defining the string "There are %d types of people." adding 10 in where the formatter %d is
x = "There are %d types of people." % 10
# A variable defining the string "binary"
binary = "binary"
# A variable defining the string "don't"
do_not = "don't"
# A variable defining the string "Those who know %s and those who %s" inserting the variable binary, and do_not respectively
y = "Those who know %s and those who %s." % (binary, do_not)

# prints the variable x ("there are %d types of people." % 10)
print x
# prints the variable y ("Those who know %s and those who %s" % (binary, do_not))
print y

# prints the string "I said: %r." where %r is variable x
print "I said: %r." % x
# prints the string "I also said: '%s'." where %s is the variable y
print "I also said: '%s'." % y

# a Boolean variable set to false
hilarious = False
# A variable defining the string "Isn't that joke so funny?! %r"
joke_evaluation = "Isn't that joke so funny?! %r"

# Prints the variable joke_evaluation where %r in joke_evaluation is the variable hilarious
print joke_evaluation % hilarious

# A variable defining the string "This is the left side of..."
w = "This is the left side of..."
# A variable defining the string "a string with a right side."
e = "a string with a right side."

# Prints the variables w and e added together
print w + e

#SD4: It takes the string w and the string e and uses the addition opperator to add them together, like it would with any interger(*note* it doesn't add a space between the strings).
