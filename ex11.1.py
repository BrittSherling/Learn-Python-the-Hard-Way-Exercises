# Example of sys admin menu (no functionality)
style_line = 30 * '-'
print style_line
print (" M A I N - M E N U ")
print style_line
print ("1. Start Server.")
print ("2. Backup.")
print ("3. Reboot Server.")
print ("4. Stop Server.")
print style_line

##########################
## Error Handling       ##
## will only accept int ##
##########################
# Wait for valid input in while...not
is_valid = 0

while not is_valid :
    try :
        choice = int(raw_input('Enter your choice [1 - 4] : '))
        is_valid = 1 #set it to 1 to validate input and to terminate the while..not loop
    except ValueError, e :
        print ("'%s' is not a valid interger." % e.args[0].split(": ")[1])

# Take action as per selected menu-option
if choice == 1:
    print ("Starting Server...")
elif choice == 2:
    print ("Starting Backup...")
elif choice == 3:
    print ("Rebooting Server...")
elif choice == 4:
    print ("Stopping Server...")
else:
    print ("Invalid number. Try again...")
