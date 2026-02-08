import Actions
import config
from DeveloperTeam import DeveloperTeam


def main():
    money = config.STARTING_MONEY
    sprint_number = 0
    team = DeveloperTeam(config.STARTING_TEAM_SIZE)
    while money > 0:
        print("Money:", money)
        print("Choose an option")
        for action in Actions.Action:
            print(f"{action.value}: {action.name}")
        option = input()
        action = Actions.Action(int(option))
        cost = action.take_action(team)
        money -= cost
        sprint_number += 1
    pass

    print(f"Simulation completed after {sprint_number} sprints.")


main()
