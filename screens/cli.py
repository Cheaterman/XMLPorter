__author__ = 'Cheaterman'

from sys import stdin
from xml.etree import cElementTree
from xml.dom import minidom
from entities import ElementDialog



class CliMenu:
    def __init__(self):
        self.motd = 'Welcome to XMLPorter. Please enjoy using it!'

        self.print_motd()
        self.dialog = ElementDialog()
        self.elements = []

    def print_motd(self):
        print(self.motd)

    def process(self, app):
        self.dialog.current().display()
        line = stdin.readline().strip('\r\n')

        if line == 'quit':
            app.quit = True
            self.save()
        else:
            self.dialog.current().value = line
            if not self.dialog.next():
                self.elements.append(self.dialog)
                self.dialog = ElementDialog()

    def save(self):
        root = cElementTree.Element('Elements')
        for element in self.elements:
            leaf = cElementTree.SubElement(root, 'Element')
            for child in element.elements:
                field = cElementTree.SubElement(leaf, child.name)
                field.text = child.value

        tree = cElementTree.ElementTree(root)
        document = minidom.parseString(cElementTree.tostring(root, encoding='UTF-8'))
        file = open('Element.xml', 'wb')
        file.write(document.toprettyxml(
            indent='    ',
            encoding='UTF-8'
        ))