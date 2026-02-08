import Actions
import CodeBase
import config
from CodeModule import CodeModule
from DeveloperTeam import DeveloperTeam


def main():
    sprint_number = 0
    team = DeveloperTeam()
    codebase = CodeBase.CodeBase()
    codebase.add_code_module(CodeModule())
    while team.money > 0 and len(team.developers) > 0 and len(team.testers) > 0:
        print("Money:", team.money)
        print("Choose an option")
        for action in Actions.Action:
            print(f"{action.value}: {action.name}")
        option = input()
        while option not in [str(i) for i in range(len(Actions.Action))]:
            print("Invalid option. Please try again.")
            option = input()
        action = Actions.Action(int(option))
        cost = action.take_action(team, codebase)
        team.money -= cost
        sprint_number += 1
    pass

    print(f"Simulation completed after {sprint_number} sprints.")


main()
