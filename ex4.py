# Maximum number of cars, also maximum number of drivers
cars = 100
# Maximum number of seats per car. (having 4 as a float point, doesn't seem to matter.)
space_in_a_car = 4.0
# Number of drivers currently available.
drivers = 30
# Passengers looking to carpool.
passengers = 90
# cars_not_driven is equal to the maximum number of cars subtracted by the currectly available amount of drivers.
cars_not_driven = cars - drivers
# cars_driven is exactly equal to the number of drivers.
cars_driven = drivers
# carpool_capacity is the ammount of cars being driven * the maximum numver of available seats.
carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car is equal to the ammount of passengers divided by the number of cars currently being driven.
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "there are only", drivers, "drivers available."
print "there will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "people to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
