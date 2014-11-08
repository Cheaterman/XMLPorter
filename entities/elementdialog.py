__author__ = 'Cheaterman'

from entities import Element



class ElementDialog:
    def __init__(self):
        self.elements = []
        self.current_element = 0

        self.add_element('Name')
        self.add_element('Date')
        self.add_element('Description')

    def add_element(self, name):
        element_names = []
        for element in self.elements:
            element_names.append(element.name)
        if not name in element_names:
            self.elements.append(Element(name))

    def next(self):
        if self.current_element < len(self.elements) - 1:
            self.current_element += 1
        else:
            self.current_element = 0
        return self.current()

    def current(self):
        return self.elements[self.current_element]

    def dump(self):
        for element in self.elements:
            print '%s = "%s"' % (element.name, element.value)