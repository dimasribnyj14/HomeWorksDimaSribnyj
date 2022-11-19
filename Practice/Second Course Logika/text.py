#Hello guys, now we go to know which subrscribers have their nicknames. Lets go use Dict!
subscribers = {"ELFINSTA": 230422}
#Now lets check out!
print(subscribers)
#Oh, we today got a new subscriber, lets check out his nickname!
new_subscriber = {"guns sus": 290422}
#Now this subscriber goes into the dictionary.
subscribers.update(new_subscriber)
#Okay, we changed this dict, lets check out at this time!
print(subscribers)
#Alright, now i want to know, when ELFINSTA subscribed.
print(subscribers.get("ELFINSTA"))
#So, now i want to know only their nicknames, not data of the subscribe.
print(subscribers.keys())
#Okay, now i want know only their data of the surbscibe, not nicknames.
print(subscribers.values())
#Good, and the last one, useless method, i dont know why this method added to the dict
print(subscribers.items())
#Well done, now i want to say "Good Bye!"
print(subscribers)