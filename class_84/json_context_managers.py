import json

with open('friends_json.txt','r') as file:
    file_contents = json.load(file)  # reads file with context manager, closing the file after the block


print(file_contents['friends'][0])

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

# Go and investigate how to use json.dump

with open('cars_json.txt', 'w') as file_write:
    json.dump(cars, file_write)

my_json_string = '[{"name":"Alfa Romeo","released":1950}]'
incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])

