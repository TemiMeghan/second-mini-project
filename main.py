# ****************************************************************
# Second mini project
# Lists,
# ****************************************************************

import random # the random library
# ############
# Task #1
#############
print("Task #1")
# A short story of the city I was born with the use of list and fstrings

Interesting_Lagos = ["Ikeja-City mall", "Lekki Conservation Center", "The 3rd mainland bridge"]   #A list of interesting places in the Lagos city.
lagos_1 = Interesting_Lagos[0]  #first item in Interesting_Lagos
lagos_2 = Interesting_Lagos[1]  #second item in Interesting_Lagos
lagos_3 = Interesting_Lagos[2]  #third item in Interesting_Lagos
print()  #indicates a space
  # about the first item in Interesting_Lagos
print(f"{lagos_1} is a popular place in Lagos, known for several activities from watching movies at the cinema inside the mall, to eateries, clothing brands and clothing stores and different bank ATMs. It is mostly known as the one stop to have fun with family and friends as well as shop for your favorite wares and items.")
print()  #indicates a space
#about the second item in Interesting_Lagos
print(f"Lagos which is known as one of the busiest city, would you think there would be a place for adventure? Oh yes, {lagos_2} offers you adventure in its rarest form, a home to several plants and animals and a place for family and friends to hangout after a busy day in the city") 
print()  #indicates a space
#about the third item in Interesting_Lagos
print(f"Lastly, have you ever jouneyed on the first longest bridge in Africa, with a total length of 11,800m? {lagos_3} is the first ever longest bridge created in Africa and is located in Lagos, journeying on this bridge is something you sure don't want to miss.")
print()  #indicates a space
print()  #indicates a space
# ############
# Task #2
#############
print("Task #2")
# Step 1
#  a list of the five people going on the mission with a message informing each person about their presence in this mission and using the len() function and fstring in delvering the message.
print()  #indicates a space
# list of friends selected for the mission including me
mission_friends = ["Iffy", "Aayu", "Bils", "Paul", "Temi"]
# a messegae to iffy
message_0 = (f"Hello {mission_friends[0]}, this is {mission_friends[-1]}. I got an important message from the new president of the Intergalactic Space Force, Priyanka Chopra, to inform you about a special mission we have and you have been selected to be a part of this mission. Thank you")
print(message_0)
print()  #indicates a space
# a messegae to Aayu
message_1 = (f"Hello {mission_friends[1]}, this is {mission_friends[-1]}. I got an important message from the new president of the Intergalactic Space Force, Priyanka Chopra, to inform you about a special mission we have and you have been selected to be a part of this mission. Thank you")
print(message_1)
print()  #indicates a space
# a messegae to Bils
message_2 = (f"Hello {mission_friends[2]}, this is {mission_friends[-1]}. I got an important message from the new president of the Intergalactic Space Force, Priyanka Chopra, to inform you about a special mission we have and you have been selected to be a part of this mission. Thank you")
print(message_2)
print()  #indicates a space
# a messegae to paul
message_3 = (f"Hello {mission_friends[3]}, this is {mission_friends[-1]}. I got an important message from the new president of the Intergalactic Space Force, Priyanka Chopra, to inform you about a special mission we have and you have been selected to be a part of this mission. Thank you")
print(message_3)
print()  #indicates a space
# a messegae indicating the total number of friends on this mission
print(f"In this we mission we are {len(mission_friends)} in total.")
print()  #indicates a space
# Step 2
not_able = (f"Hi {mission_friends[-2]}, I am so sorry to announce to you that you would not be participating in the mission with the team and I due to a bad case of Space Sneezing you have. Thank you.")
print(not_able)
mission_friends[-2] = "Emmae"  # replacing Paul with Emmae
print()  #indicates a space
# An updated message to iffy
update_iffy = (f"Hello {mission_friends[0]}, this is {mission_friends[-1]}. I got an important message from the new president of the Intergalactic Space Force, Priyanka Chopra, to inform you about a special mission we have and you have been selected to be a part of this mission. Also our dear friend Paul fell sick and has been replaced with {mission_friends[-2]}, Thank you.")
print(update_iffy)
print()  #indicates a space
# An updated message to Aayu
update_Aayu = (f"Hello {mission_friends[1]}, this is {mission_friends[-1]}. I got an important message from the new president of the Intergalactic Space Force, Priyanka Chopra, to inform you about a special mission we have and you have been selected to be a part of this mission. Also our dear friend Paul fell sick and has been replaced with {mission_friends[-2]}, Thank you.")
print(update_Aayu)
print()  #indicates a space
# An updated message to Bils
update_Bils = (f"Hello {mission_friends[2]}, this is {mission_friends[-1]}. I got an important message from the new president of the Intergalactic Space Force, Priyanka Chopra, to inform you about a special mission we have and you have been selected to be a part of this mission. Also our dear friend Paul fell sick and has been replaced with {mission_friends[-2]}, Thank you.")
print(update_Bils)
print()  #indicates a space
# An updated message to Emmae
update_Emmae = (f"Hello {mission_friends[-2]}, this is {mission_friends[-1]}. I got an important message from the new president of the Intergalactic Space Force, Priyanka Chopra, to inform you about a special mission we have and you have been selected to be a part of this mission. Also our dear friend Paul fell sick and you are to stand in for him {mission_friends[-2]}, Thank you.")
print(update_Emmae)
print()  #indicates a space
# a messegae indicating the total number of friends on this mission
print(f"In this we mission we are {len(mission_friends)} in total.")
print()  #indicates a spac
#Step 3
# Adding 3 celebrities to the list using the insert() and append() method
mission_friends.insert(0, "Eli-J")  #first celebrity
mission_friends.insert(3, "Sylvia")  #second celebrity
mission_friends.append("Saki")  #third celebrity
print(mission_friends)
print() #indicates a space
mission_0 = (f"Hello {mission_friends[0]}, this is {mission_friends[-2]}. I got an important message from the new president of the Intergalactic Space Force, Priyanka Chopra, to inform you about a special mission we have and you have been selected to be a part of this mission. Thank you")  #a message to Eli-J on the mission
print(mission_0)
print() #indicates a space
mission_1 = (f"Hello {mission_friends[1]}, this is {mission_friends[-2]}. I got an important message from the new president of the Intergalactic Space Force, Priyanka Chopra, to inform you about a special mission we have and you have been selected to be a part of this mission. Thank you")  #a message to Iffy on the mission
print(mission_1)
print() #indicates a space
mission_2 = (f"Hello {mission_friends[2]}, this is {mission_friends[-2]}. I got an important message from the new president of the Intergalactic Space Force, Priyanka Chopra, to inform you about a special mission we have and you have been selected to be a part of this mission. Thank you")  #a message to Aayu on the mission
print(mission_2)
print() #indicates a space
mission_3 = (f"Hello {mission_friends[3]}, this is {mission_friends[-2]}. I got an important message from the new president of the Intergalactic Space Force, Priyanka Chopra, to inform you about a special mission we have and you have been selected to be a part of this mission. Thank you")  #a message to Sylvia on the mission
print(mission_3)
print() #indicates a space
mission_4 = (f"Hello {mission_friends[4]}, this is {mission_friends[-2]}. I got an important message from the new president of the Intergalactic Space Force, Priyanka Chopra, to inform you about a special mission we have and you have been selected to be a part of this mission. Thank you")  #a message to Bils on the mission
print(mission_4)
print() #indicates a space
mission_5 = (f"Hello {mission_friends[5]}, this is {mission_friends[-2]}. I got an important message from the new president of the Intergalactic Space Force, Priyanka Chopra, to inform you about a special mission we have and you have been selected to be a part of this mission. Thank you")  #a message to Emmae on the mission
print(mission_5)
print() #indicates a space
mission_07 = (f"Hello {mission_friends[-1]}, this is {mission_friends[-2]}. I got an important message from the new president of the Intergalactic Space Force, Priyanka Chopra, to inform you about a special mission we have and you have been selected to be a part of this mission. Thank you")  #a message to Saki on the mission
print(mission_07)
print() #indicates a space
# a messegae indicating the total number of friends on this mission
print(f"In this we mission we are {len(mission_friends)} in total.")
print() #indicates a space
print() #indicates a space
# Step 4
# informing the team of the current changes of the mission, with the use of pop method and len()
aborted_0 = (f"Hello {mission_friends[0]}, this is {mission_friends[-2]}. I got an important message from the new president of the Intergalactic Space Force, Priyanka Chopra, to inform you about a slight change in the mission which allows only two members of the team to be in this mission and you have not been selected for this mission. Thank you")  #a message to Eli-j on the cancelled mission
print(aborted_0)
mission_friends.pop(0)  # removed Eli-j from the list
print(mission_friends) #Prints current members in the team
print() #indicates a space
aborted_1 = (f"Hello {mission_friends[1]}, this is {mission_friends[-2]}. I got an important message from the new president of the Intergalactic Space Force, Priyanka Chopra, to inform you about a slight change in the mission which allows only two members of the team to be in this mission and you have not been selected for this mission. Thank you")  #a message to Aayu on the cancelled mission
print(aborted_1)
mission_friends.pop(1)  # removed Aayu from the list
print(mission_friends) #Prints current members in the team
print() #indicates a space
aborted_2 = (f"Hello {mission_friends[2]}, this is {mission_friends[-2]}. I got an important message from the new president of the Intergalactic Space Force, Priyanka Chopra, to inform you about a slight change in the mission which allows only two members of the team to be in this mission and you have not been selected for this mission. Thank you")  #a message to Bils on the cancelled mission
print(aborted_2)
mission_friends.pop(2)  # removed Bils from the list
print(mission_friends) #Prints current members in the team
print() #indicates a space
aborted_3 = (f"Hello {mission_friends[0]}, this is {mission_friends[-2]}. I got an important message from the new president of the Intergalactic Space Force, Priyanka Chopra, to inform you about a slight change in the mission which allows only two members of the team to be in this mission and you have not been selected for this mission. Thank you")  #a message to Iffy on the cancelled mission
print(aborted_3)
mission_friends.pop(0)  # removed Iffy from the list
print(mission_friends) #Prints current members in the team
print() #indicates a space
aborted_4 = (f"Hello {mission_friends[1]}, this is {mission_friends[-2]}. I got an important message from the new president of the Intergalactic Space Force, Priyanka Chopra, to inform you about a slight change in the mission which allows only two members of the team to be in this mission and you have not been selected for this mission. Thank you")  #a message to Emmae on the cancelled mission
print(aborted_4)
mission_friends.pop(1)  # removed Emmae from the list
print(mission_friends) #Prints current members in the team
print() #indicates a space
aborted_5 = (f"Hello {mission_friends[0]}, this is {mission_friends[-2]}. I got an important message from the new president of the Intergalactic Space Force, Priyanka Chopra, to inform you about a slight change in the mission which allows only two members of the team to be in this mission and you have not been selected for this mission. Thank you")  #a message to Sylvia on the cancelled mission
print(aborted_5)
mission_friends.pop(0)  # removed Sylvia from the list
print(mission_friends) #Prints current members in the team
print() #indicates a space
onboard_1 = (f"Hello {mission_friends[1]}, this is {mission_friends[0]}. I got an important message from the new president of the Intergalactic Space Force, Priyanka Chopra, to inform you about a slight change in the mission which allows only two members of the team to be in this mission and you have been selected for this mission with myself {mission_friends[0]}. Thank you")  #a message to Saki on the mission
print(onboard_1)
print(mission_friends) #Prints current members in the team
print() #indicates a space
# a messegae indicating the total number of friends on this mission
print(f"In this we mission we are {len(mission_friends)} in total.")
print() #indicates a space
# step 5
# using the del() to delete members of te team and printing out the list and also the numbers of element in the list.
del mission_friends[0::] # deletes all members of the team
print(mission_friends) # prints an empty list
print() #indicates a space
# a messegae indicating the total number of friends on this mission
print(f"In this we mission we are {len(mission_friends)} in total.")
print()  #indicates a space
print()  #indicates a space
# ############
# Tast #3
#############
print("Task #3")
print()  #indicates a space
# locations of the next 5 world cup in a list and using the following to modify the list: sorted(), sort() and reverse().
#List of locations for the next world cup
Worldcup_locations = ["Brazil", "South Africa", "Germany", "Qatar", "France"]
print(Worldcup_locations)
print()  #indicates a space
# arranges list in ascending order
locations_1 = sorted(Worldcup_locations)
print(locations_1) #prints modified list without modifying the original list
print()  #indicates a space
print(Worldcup_locations)#prints list as stored originally
print()  #indicates a space
#arranges list in descending order
reverse_locations = sorted(Worldcup_locations, reverse=True) 
print(reverse_locations) #prints modified list without modifying the original list
print()  #indicates a space
print(Worldcup_locations)#prints list as stored originally
print()  #indicates a space
#prints origanl list in reverse order
Worldcup_locations.reverse() #list reversed
print(Worldcup_locations) #reversed list printed
print()  #indicates a space
Worldcup_locations.reverse() #list reversed 2nd time
print(Worldcup_locations) #reversed list printed 2nd time
print()  #indicates a space
Worldcup_locations.sort() #sorts list in ascending order
print(Worldcup_locations) #prints modified list
print()  #indicates a space
#sorts list in descending order
Worldcup_locations.sort(reverse=True) 
print(Worldcup_locations) #prints list in descending order
print()  #indicates a space
# ############
#Task #4
#############
print("Task #4")
print()  #indicates a space
# a list of different elements with the use of random library to create a story
places = ["lagos","abuja","alberta"] #places list
foods = ["rice", "potatoe", "noodles"] #foods types
cars = ["toyota", "benz", "ford"] # car types
colours = ["white", "black", "silver"] # different colours
fruits = ["apple", "orange", "strawberry"] # fruit types
# The story with the use of .randint(1,5), .choice() from the random library imported and title() to format properly
print(f"In {random.choice(places).title()}, there are {random.randint(1, 5)} common cars being used, an example is {random.choice(cars).title()}, which is commonly used by 60 percent of people that lives in this city, it comes in {random.randint(1, 5)} colours, but the most popular colour used by people in this city is {random.choice(colours).title()}, because it always makes the owners appear elegant. The people in the city has  {random.randint(1, 5)} popular foods, an example is {random.choice(foods).title()} alongside they are lovers of fruits. In this city, we have {random.randint(1, 5)} popular fruits and most residents in this city love eating {random.choice(fruits).title()} because of its sweet flavour.")
print()  #indicates a space
# ############
# Task #5
#############
print("Task #5")
print()  #indicates a space
# a program that adds the numbers of a student number together using list and index positions.
student_id = ["B",0,0,1,6,1,3,7,9] #student number in list
# output of my student number
print(f"My student number is {student_id[0]} {student_id[1]} {student_id[2]} {student_id[3]} {student_id[4]} {student_id[5]} {student_id[-3]} {student_id[-2]} {student_id[-1]}")
print()  #indicates a space
# ############
# Task #6
#############
print("Task #6")
print()  #indicates a space
# a program that prints the items of a meal using its index and fstring in a sentence
meals = ["Breakfast", "Lunch", "Dinner"] #meal lists
#breakfast items
breakfast = ["eggs", "milk", "bread", "coffee"] 
#lunch items
lunch = ["rice", "tomatoes", "chicken", "orange juice"]
#dinner items
dinner = ["pasta", "meatballs", "garlic sauce", "fish"]
print(f"Today at my aunt's house, I would be having {breakfast[0]} and {breakfast[-1]} for {meals[0]}, for {meals[1]} I would be having {lunch[0]} and {lunch[-1]} and finally, for {meals[-1]} I would be having {dinner[0]} and {dinner[-1]}, would you like to join me?")