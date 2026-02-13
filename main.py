from datetime import datetime

from textual.app import App, ComposeResult
from textual.widgets import Digits

import Actions
import CodeBase
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


class ClockApp(App):
    CSS = """
    Screen { align: center middle; }
    Digits { width: auto; }
    """

    def compose(self) -> ComposeResult:
        yield Digits("")

    def on_ready(self) -> None:
        self.update_clock()
        self.set_interval(1, self.update_clock)

    def update_clock(self) -> None:
        clock = datetime.now().time()
        self.query_one(Digits).update(f"{clock:%T}")


if __name__ == "__main__":
    app = ClockApp()
    app.run()
