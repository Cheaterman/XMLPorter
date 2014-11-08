__author__ = 'Cheaterman'

from sys import stdin



class CliMenu():
    def __init__(self):
        self.motd = 'Welcome to XMLPorter. Please enjoy using it!'

        self.print_motd()


    def print_motd(self):
        print self.motd

    def process(self, app):
        line = stdin.readline().strip('\r\n')
        if line == 'quit':
            app.quit = True
        else:
            print line