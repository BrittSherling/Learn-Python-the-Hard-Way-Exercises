# Declares the variable formatter and sets it equal to "%r %r %r %r"
formatter = "%r %r %r %r"

# prints the variable formatter and sets the formatters equal to 1, 2, 3, 4 respectively
print formatter % (1, 2, 3, 4)
# prints the variable formatter and sets the formatters equal to "one", "two", "three", "four"
print formatter % ("one", "two", "three", "four")
# prints the variable formatter and sets the formatters equal to boolean True, False, False, True
print formatter % (True, False, False, True)
# prints the variable formatter and sets the formatters equal to the variable formatter four times
print formatter % (formatter, formatter, formatter, formatter)
# prints the variable formatter and sets the formatter equal to the strings "I had this thing.", "That you could type up right.", "But it didn't sing.", "So I said goodnight."
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
