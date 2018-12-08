# Ask the user for a list of 3 friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to 'nearby_friends.txt'

# hint: readlines()
input_friends = input('Name your three friends separated by a \',\' (comma): ')
friends_list = [x.strip().lower() for x in input_friends.split(',')]

people_file = open('people.txt', 'r')
list_of_people_in_file = [y.lower().strip() for y in people_file.readlines()]
people_file.close()

friends_nearby = []

for friend_inserted in friends_list:
    if friend_inserted in list_of_people_in_file:
        friends_nearby.append(friend_inserted)

nearby_friends_file = open('nearby_friends.txt', 'w')
for friend in friends_nearby:
    nearby_friends_file.write(friend+'\n')

