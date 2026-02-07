from Developer import Developer
from Tester import Tester


class DeveloperTeam:
    def __init__(self, size):
        self.developers = []
        self.testers = []
        while size > 0:
            self.developers.append(Developer())
            self.testers.append(Tester())
            size -= 1

    def remove_quitters(self):
        # Remove any developer/tester who is burned out
        for developer in self.developers:
            if developer.is_burned_out():
                self.developers.remove(developer)
        for tester in self.testers:
            if tester.is_burnt_out():
                self.testers.remove(tester)
