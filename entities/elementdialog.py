__author__ = 'Cheaterman'

from xml.etree import cElementTree
from xml.dom import minidom
from entities import Element



class ElementDialog:
    def __init__(self):
        self.elements = []
        self.current_element = 0

        self.add('Name')
        self.add('Date')
        self.add('Description')

    def add(self, name):
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
        root = cElementTree.Element('Element')
        for element in self.elements:
            field = cElementTree.SubElement(root, element.name)
            field.text = element.value

            print('%s = "%s"' % (element.name, element.value))

        tree = cElementTree.ElementTree(root)
        document = minidom.parseString(cElementTree.tostring(root, encoding='UTF-8'))
        file = open('Element.xml', 'wb')
        file.write(document.toprettyxml(
            indent='    ',
            encoding='UTF-8'
        ))