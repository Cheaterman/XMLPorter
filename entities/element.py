__author__ = 'Cheaterman'

class Element:
    def __init__(self, name):
        self.name = name
        self.value = ''

    def display(self):
        print self.name, ': '