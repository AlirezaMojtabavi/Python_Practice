from math import floor

locations = str(input())
listOfLocations = locations.split()

maximum = float((listOfLocations[0]))
minimum = float((listOfLocations[1]))
center = float((listOfLocations[2]))

for item in listOfLocations :
    item = float(item)
    if item >= maximum :
        maximum = item
    else :
        maximum = maximum

    if item <= minimum :
        minimum = item
    else:
        minimum = minimum

for item2 in listOfLocations :
    item2 = float(item2)
    if (item2 != minimum) and (item2 != maximum):
        center = item2

result = (center - minimum) + (maximum - center)

if (result - floor(result)) == 0 :
    result = str(result)
    for letter in result :
        if letter == "." :
            result = result[: result.index(letter)]
            result = int(result)

print(result)