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
