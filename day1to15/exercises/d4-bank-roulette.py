import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_items = len(names) 
   #Get the total number of items in list.
random_choice = random.randint(0, num_items - 1)
   #Generate random numbers between 0 and the last index. 
person_who_will_pay = names[random_choice]
   #Pick out random person from list of names using the random number.

print(person_who_will_pay + " is going to buy the meal today!")