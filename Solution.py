class Shape:

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, len):
        self.length = len

    def area(self):
        return self.length*self.length


l_sq = Square(8)
print(l_sq.area())



#############_________second Method

# class Shape(object):
#
#     def area(self):
#         return 0
#
#
# class Square(Shape):
#     def area(self):
#         return self*self
#
#
# ar = Square
# print(ar.area(8))
