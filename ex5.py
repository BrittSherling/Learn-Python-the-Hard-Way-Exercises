name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.00 # inches
weight = 180.00 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
# height multiplied by 2.54 to find total hieght in cm
height_cm = height * 2.54
# 1 kg divided by 2.2 pounds, then multipled by the weight in pounds.
weight_kg = (1 / 2.2046226218) * weight

print "Let's talk about %s." % name
print "He's %d Centimeters tall." % height_cm
print "He's %d Kilograms heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height_cm, weight_kg, age + height_cm + weight_kg)
