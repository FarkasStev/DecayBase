def main():
    money = 100
    cost = 10
    sprint_number = 0
    while money > 0:
        print("Money:", money)
        print("Choose an option")
        option = input()
        print("You chose: ", option)
        money -= cost
        sprint_number += 1
    pass

    print(f"Simulation completed after {sprint_number} sprints.")


main()
