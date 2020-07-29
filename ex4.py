# storing value 100 in variable cars
cars = 100
#storing value 4.0 in variable
space_in_a_car = 4.0
#storing value in variable
drivers = 30
#storing value in variable
passengers = 90
#subtracting cars by drivers 
cars_not_driven = cars - drivers
#the number of cars driven is equal to the aqvailability of drivbes
cars_driven = drivers
# carpool capacity is the the space in a car * the numbers of cars being driven
carpool_capacity = cars_driven * space_in_a_car
#average passengers that can be put in a car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, " people today")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "number of passengers in each car")