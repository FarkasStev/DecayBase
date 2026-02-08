from enum import Enum


class Action(Enum):
    ADD_FEATURE = 1
    REFACTOR = 2
    ONBOARD_DEV = 3
    RUSH_DEADLINE = 4

    def take_action(self, team):
        if self.name == "ADD_FEATURE":
            print("Adding a new feature")
        elif self.name == "REFACTOR":
            print("Refactoring the code")
        elif self.name == "ONBOARD_DEV":
            print("Onboarding a new developer")
        elif self.name == "RUSH_DEADLINE":
            print("Rushing to meet a deadline")

        return 10
