import math

vector = [None,None,None]
for i in range(3):
    vector[i] = int(input("Enter a value: "))
    
x,y,z = vector
magnitude = math.sqrt(x**2 + y**2 + z**2)

print(magnitude)