import converters
from converters import lbs_to_kg

lbs_to_kg(100)

print(converters.kg_to_lbs(70))

#Ercecise
numbers = [10, 3, 6, 2]
max = numbers[0]
for number in numbers:
    if number > max:
        max = numbers
print(max)

