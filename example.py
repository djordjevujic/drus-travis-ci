"""
Pylint Tutorial
"""

#pylint: disable=too-few-public-methods
class Car(object):
    """ Klasa auto """
    def __init__(self, color):
        self.color = color


MY_CAR = Car('blue')


def crash(car1, car2): #pylint: disable=unused-argument
    """ Sudar funkcija """
    car1.color = 'burnt'

crash(Car('red'), MY_CAR)
