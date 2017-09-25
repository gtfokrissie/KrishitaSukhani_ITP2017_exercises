guests=['Sidney Sheldon' , 'Channing tatum' , 'Rihanna']
message=' I would be pleased if you could attend my dinner party this weekend!'
print('Greetings '+ guests[0] + message)
print('Greetings '+ guests[1] + message)
print('Greetings '+ guests[2] + message)
print('Channing tatum cannot make it')
del guests[1]
guests.insert(1,'Skrillex')
print('Greetings '+ guests[0] + message)
print('Greetings '+ guests[1] + message)
print('Greetings '+ guests[2] + message)
print('Great news I have found a larger dining table therefore we are able to invite more guests')
guests.insert(0,'Cindy Kimberly')
guests.insert(1,'Jenna Marbles')
guests.append('johnny depp')
print('Greetings '+ guests[0] + message)
print('Greetings '+ guests[1] + message)
print('Greetings '+ guests[2] + message)
print('Greetings '+ guests[3] + message)
print('Greetings '+ guests[4] + message)
print('Greetings '+ guests[5] + message)
print(' My apologies but the dinner table has been reduced to only 2 seatings')
popped_guests=guests.pop()
Apology= ', I am sorry to say but we are not able to invite you over for dinner, have a nice weekend! '
print(popped_guests+Apology)
popped_guests=guests.pop()
Apology= ', I am sorry to say but we are not able to invite you over for dinner, have a nice weekend! '
print(popped_guests+Apology)
popped_guests=guests.pop()
Apology= ', I am sorry to say but we are not able to invite you over for dinner, have a nice weekend! '
print(popped_guests+Apology)
popped_guests=guests.pop()
Apology= ', I am sorry to say but we are not able to invite you over for dinner, have a nice weekend! '
print(popped_guests+Apology)
invitation=', I am pleased to inform you that dinner is still on this weekend'
print('dear, '+ guests[0]+invitation)
print('dear, '+ guests[-1]+invitation)
del guests[0]
del guests[1]
print(guests)
