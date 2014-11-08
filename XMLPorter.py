__author__ = 'Cheaterman'

from screens import CliMenu



class App:
    def __init__(self):
        self.screen = CliMenu()
        self.quit = False

    def start(self):
        while not self.quit:
            self.screen.process(self)



if __name__ == '__main__':
    App().start()