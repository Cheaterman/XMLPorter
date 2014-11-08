__author__ = 'Cheaterman'

from sys import stdin
from entities import ElementDialog



class CliMenu:
    def __init__(self):
        self.motd = 'Welcome to XMLPorter. Please enjoy using it!'

        self.print_motd()
        self.dialog = ElementDialog()

    def print_motd(self):
        print self.motd

    def process(self, app):
        self.dialog.current().display()
        line = stdin.readline().strip('\r\n')

        if line == 'quit':
            app.quit = True
            self.dialog.dump()
        else:
            self.dialog.current().value = line
            self.dialog.next()