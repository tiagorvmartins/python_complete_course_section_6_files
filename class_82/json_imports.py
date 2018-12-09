import json

file = open('friends_json.txt','r')
file_contents = json.load(file)  # reads file and turns it to dictionary
file.close()

print(file_contents['friends'][0])

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

# Go and investigate how to use json.dump

file_write = open('cars_json.txt', 'w')
json.dump(cars, file_write)
file_write.close()

my_json_string = '[{"name":"Alfa Romeo","released":1950}]'
incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])

