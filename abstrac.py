from abc import ABC  # import the abstract class module


class Polygon(ABC):  # sets the abstract class for the other classes to take
    def noofsides(self):
        pass


class Triangle(Polygon):  # overrides the method in the Polygon class
    def noofsides(self):
        print("I have 3 sides")


class Square(Polygon):  # overrides the method in the Polygon class
    def noofsides(self):
        print("I have 4 sides")
