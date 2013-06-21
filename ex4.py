#100 cars
cars = 100
#4 space for people in a car
space_in_a_car = 4.0
#30 drivers
drivers = 30
#90 passengers
passengers = 90
#cars not driven = number of cars - number of drivers 
cars_not_driven = cars - drivers
#cars drivne = number of drivers
cars_driven = drivers
#carpool capactity = cars driven * space in a car
carpool_capactiy = cars_driven * space_in_a_car
#average passengers per car = passengers / cars driven
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capactiy, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
