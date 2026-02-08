from enum import Enum

from Developer import Developer
from Feature import Feature
from Tester import Tester


class Action(Enum):
    ADD_FEATURE = 1
    REFACTOR = 2
    ONBOARD_DEV = 3
    RUSH_DEADLINE = 4

    def take_action(self, team, codebase):
        if self.name == "ADD_FEATURE":
            self.add_feature(team, codebase)
        elif self.name == "REFACTOR":
            self.refactor(team)
        elif self.name == "ONBOARD_DEV":
            self.onboard_dev(team)
        elif self.name == "RUSH_DEADLINE":
            self.rush_deadline(team)
        else:
            raise ValueError(f"Invalid action: {self.name}")

        team.remove_quitters()
        cost = self.incur_cost(team)
        self.summarize_state(team, codebase)
        return cost

    def add_feature(self, team, codebase):
        feature = Feature()
        for module in codebase.code_modules:
            module.develop_feature(feature, team.developers)
            module.test_feature(feature, team.testers)
        print("Adding a new feature")

    def refactor(self, team):
        print("Refactoring the code")

    def onboard_dev(self, team):
        print("Onboarding a new developer")
        team.add_developer(Developer())

    def rush_deadline(self, team):
        print("Rushing to meet a deadline")

    def incur_cost(self, team):
        print("Incurring a cost")
        cost = 0
        for developer in team.developers:
            cost += developer.pay_rate
        for tester in team.testers:
            cost += tester.pay_rate
        return cost

    def summarize_state(self, team, codebase):
        print("Team Summary:")
        print("Money:", team.money)
        print("Team:")
        for developer in team.developers:
            print(f"  {developer}")
        for tester in team.testers:
            print(f"  {tester}")
        print("Codebase:")
        for module in codebase.code_modules:
            print(f"  {module}")
