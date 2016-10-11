from items import *
from map import rooms

inventory = [item_id, item_laptop, item_money]

# Start game at the reception
current_room = rooms["Reception"]

carrying_mass = 0
max_mass = 3

for i in inventory:
    carrying_mass += i["mass"]
