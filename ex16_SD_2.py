from sys import argv

script = argv

txt = open(raw_input("Name of the file you want opened: "))

print txt.read()
txt.close
