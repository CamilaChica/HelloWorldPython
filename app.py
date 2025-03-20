#Solution
#from sys import exc_info

#from utils import find_max

#numbers = [10, 3, 6, 2]
## max = find_max(numbers)
#print(max(numbers))

#Packages
#from ecommerce import shipping
#Other way to import multiple functions: from ecommerce.shipping import cal_shipping, cal_tax

#shipping.cal_shipping()

#Generating Random Values
import random

for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10, 20))

members = ['John', 'Mary', 'Bob', 'Camila']
leader = random.choice(members)
print(leader)

#Exercise

import random
class Dice:
    def roll(self):
       first =  random.randint(1, 6)
       second = random.randint(1, 6)
       return (first, second) #In python, we can also write without parenthesis and it takes it as a Tuple, like this: ""return first, second"

dice = Dice()
print(dice.roll())