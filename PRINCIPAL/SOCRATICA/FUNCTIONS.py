print(dir ())

def f():
    pass
f()
print(dir ())
def ping():
    return "Ping!"
x = ping()
print(x)
import math
print(dir(math))
def volume(r=0):
    """Returns the volume of a sphere with radius r."""
    v = (4.0/3.0) * math.pi * r**3
    return v
x = volume()
print(x)

def triangle_area(b,h):
    """Returns the area of a triangle with base b and height h."""
    return 0.5 * b * h
z = triangle_area(3,6)
print(z)
def cm(feet = 0, inches = 0):
    """Converst a length from feet and inches to centimeters."""
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm + feet_to_cm


print(cm(feet=5))
print(cm(inches=70))
print(cm(feet=5, inches=8))
print(cm(inches=8, feet=5))

def  g(y, x = 0 ):
    return x + y
print(g(5))    