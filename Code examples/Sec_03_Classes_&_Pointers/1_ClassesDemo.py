# Why is a class used in python?
    # Usually used to define a data type
    # Python has build in classes like Integer, String etc

# Example code for a class Cookie

class Cookie: 
    def __init__(self, color): #__init__ is the constructor, it takes self as 1st arg and rest of its parameters follow
        self.color = color

    # every method inside a class takes self as one of its args

    def getColor(self):
        return self.color
    
    def setColor(self, newColor):
        self.color = newColor

cookie_1 = Cookie('Red')
cookie_2 = Cookie('Blue')

print('Color of cookie 1 is', cookie_1.getColor())
print('Color of cookie 2 is', cookie_2.getColor())

cookie_1.setColor('Yellow')

print('Now the color of cookie 1 is', cookie_1.getColor())
print('Color of cookie 2 is', cookie_2.getColor())