#-----------------------------------------------------------------------------
# Let's talk about object oriented programming! :)
# Classes == things that have 1. attributes 2. behaviours
# Objects == instances of classes
# e.g. for a class 'Fruit', a mango or pear could be an object of that class
#-----------------------------------------------------------------------------

#class definition
class Shape:
    # Attributes: variables - characteristics 
    num_of_sides = 0
    base = 0.0
    height = 0.0
    area = 0.0

    # dunder init function - initialise the object (an instance of this class)
    def __init__(self, num_sides, height, base, area): 
        self.num_of_sides = num_sides
        self.height = height
        self.base = base
        self.area = area

    # Behaviours: functions/things that you can do with an object
    # self allows python to refer to the object 
    def calculate_area(self):
        if self.num_of_sides == 3:
            self.area = 0.5 * self.base * self.height

# --------------------------------------------------------------------------- #
# call everything you wanna do here
fave_triangle = Shape(3,2.2,5,0)
fave_triangle.calculate_area()

print("Base: ", fave_triangle.base)
print("Original area before calc:", fave_triangle.area)
print("After calc:", fave_triangle.area)

another_triangle = Shape(3,5,10,25)

if another_triangle.area > fave_triangle.area:
    print("another_tri is a bigger triangle")