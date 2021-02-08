import json
data = {}
data['dalle']='https://dalle.com.np/'
data['daddys']='https://daddys-kitchen-the-cafe-and-restaurant.business.site/'

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)