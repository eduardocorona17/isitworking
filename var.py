message = "Hello Python World!"
print(message)
message = "What up Python Crash Course!"
print(message)

simple_message = "Simple enough?"
print(simple_message)
simple_message = "This is also simple!"
print(simple_message)
name = "ada lovelace"
print(name.title())
first_name = "eduardo"
last_name = "corona"
full_name = f"{first_name} {last_name}"
print(full_name.title())

x, y, z = 1, 2, 3
print(y)
number_list = ['1', '2', '3', '4', '5', '6']
print(number_list[-3])
print(number_list[-2])
print(number_list[-1])
other_msg = f"My first grade was a {number_list[-2]}/6"
print(other_msg)
number_list[0] = '3'
print(number_list)
bikes = ['honda', 'yamaha', 'suzuki']
bikes.append('ducati')
print(bikes)
bikes.insert(0, 'brabas')
print(bikes)
print(bikes[0].title())
print(bikes)
del bikes[3]
print(bikes)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
sorted(cars)
print(cars)
cars.reverse()
print(cars)
print(len(cars))
