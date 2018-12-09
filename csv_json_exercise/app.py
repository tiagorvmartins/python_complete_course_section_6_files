# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:

import json

csv_file = open('csv_file.txt', 'r')
club_lines = [line.strip() for line in csv_file.readlines()]
csv_file.close()

dictionary_to_write = []
for line in club_lines:
    separated_values = line.split(',')
    dictionary_to_write.append({"club":separated_values[0],"city":separated_values[1],"country":separated_values[2]})

json_file = open('json_file.txt', 'w')
json.dump(dictionary_to_write, json_file)
json_file.close()