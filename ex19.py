# defines the function 'cheese_and_crackers'
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # prints "You have %d cheeses" where %d is the variable cheese_count
    print "You have %d cheeses!" % cheese_count
    # prints "You have %d boxes of crackers" where %d is the variable boxes_of_crackers
    print "You have %d boxes of crackers" % boxes_of_crackers
    # prints "Man that's enough for a party!"
    print "Man that's enough for a party!"
    # prints "Get a blanket" and starts a new line
    print "Get a blanket.\n"

# prints "We can just give the function numbers directly:"
print "We can just give the function numbers directly:"
# calls the function cheese_and_crackers with the arguments 20 and 30
cheese_and_crackers(20, 30)

# prints "OR, we can use variables from our script:"
print "OR, we can use variables from our script:"
# sets the variable amount_of_cheese to 10
amount_of_cheese = 10
# sets the variable amount_of_crackers to 50
amount_of_crackers = 50

# calls the function cheese_and_crackers with the arguments amount_of_cheese, and amount_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# prints "We can even do math inside too:"
print "We can even do math inside too:"
# calls the function cheese_and_crackers with the arguments 10+20 and 5+6
cheese_and_crackers(10 + 20, 5 + 6)


# prints "And we can combine the two, variables and math:"
print "And we can combine the two, variables and math:"
# calls the function cheese_and_crackers with the arguments amount_of_cheese+100 and amount_of_crackers+1000
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
