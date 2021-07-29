import sys
import math

x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])
distance = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
print (distance)