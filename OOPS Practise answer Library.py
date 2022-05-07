class Formula():
    
    def init(self):
        pass 
    
    def Circle(self):
        pi=3.14
        r=int(input('Enter the circle of radius:'))
        Area=pi*r*r
        print('Area of the circle is:',Area)

    def Rectangle(self):
        l=int(input('Enter the length:'))
        b=int(input('Enter the breadth:'))
        Area=l*b
        print('Area of the rectangle is:',Area)  

    def Square(self):
        a=int(input('Enter the length:'))
        Area=a*a*a*a
        print('Area of the square is:',Area)
        
class Area():
    
    def init(self):
        pass
    
    def Circle(self):
        pi=3.14
        r=int(input('Enter the circle of radius:'))
        Area=pi*r*r
        circle='Area of the circle is:',Area
        print('Area of the circle is:',Area)
        return circle

    def Rectangle(self):
        l=int(input('Enter the length:'))
        b=int(input('Enter the breadth:'))
        Area=l*b
        rectangle='Area of the rectangle is:',Area
        print('Area of the rectangle is:',Area)
        return rectangle   

    def Square(self):
        a=int(input('Enter the length:'))
        Area=a*a*a*a
        square='Area of the square is:',Area
        print('Area of the square is:',Area)
        return square



