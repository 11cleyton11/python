class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        if self.width == self.height:
            return f'Square(side={self.width})'
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        if self.width == self.height:
            self.height = width
        self.width = width
        return self.width

    def set_height(self, height):
        if self.height == self.width:
            self.width = height
        self.height = height
        return self.height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        picture = ''
        for line in range(self.height):
            for char in range(self.width):
                picture += '*'
            picture += '\n'
        return picture
    
    def get_amount_inside(self, shape):
        w = self.width // shape.width
        h = self.height // shape.height
        return w * h


class Square(Rectangle):
    
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.__init__(side)


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
