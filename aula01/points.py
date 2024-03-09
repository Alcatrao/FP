import math
# This program reads the coordinates of two points (x1,y1) and (x2,y2).

x1 = float(input("x1? "))
y1 = float(input("y1? "))
x2 = float(input("x2? "))
y2 = float(input("y2? "))

# create tuples from coordinates
p1 = (x1, y1)
p2 = (x2, y2)

print("Point1:", p1)
print("Point2:", p2)

# Compute and print the distance between the points!
# ...

distance=math.sqrt((x1-x2)**2+(y1-y2)**2)
print("A distância entre", p1, "e", p2, "é:", distance)

