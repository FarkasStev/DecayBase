from enum import Enum

from Developer import Developer
from Feature import Feature
from Tester import Tester


class Action(Enum):
    ADD_FEATURE = 1
    REFACTOR = 2
    ONBOARD_DEV = 3
    ONBOARD_TESTER = 4
    RUSH_DEADLINE = 5

    def take_action(self, team, codebase):
        match self.name:
            case "ADD_FEATURE":
                self.add_feature(team, codebase)
            case "REFACTOR":
                self.refactor(team)
            case "ONBOARD_DEV":
                self.onboard_dev(team)
            case "ONBOARD_TESTER":
                self.onboard_tester(team)
            case "RUSH_DEADLINE":
                self.rush_deadline(team)
            case _:
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
            team.money += module.lines_of_code * module.complexity
        print("Adding a new feature")

    def refactor(self, team):
        print("Refactoring the code")

    def onboard_dev(self, team):
        print("Onboarding a new developer")
        team.add_developer(Developer())

    def onboard_tester(self, team):
        print("Onboarding a new tester")
        team.add_tester(Tester())

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
