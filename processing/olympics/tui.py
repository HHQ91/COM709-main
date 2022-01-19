
def started(msg=""):
    for x in range(85):
        print('-', end='')

    print(f"\nOperation started: {msg}...")


def complete():
    print("Operation completed.")
    for x in range(85):
        print('-', end='')

def error(msg):
    print(f"Error! {msg}")

def menu():
#     selection = input("""
# Please select one of the following options:
#     [years]     List unique years
#     [tally]     Tally up medals
#     [ctally]      Tally up medals for each team
#     [exit]      Exit the program
#     """)
    menu1 = "[years]     List unique years"
    menu2= "[tally]     Tally up medals"
    print("Please select one of the following options:")
    print(f"{menu1:10}")
    print(f"{menu2:10}")

    print(f"Your selection: ")

def display_medal_tally(tally):
    print(f"| {'Gold':<10} | {tally['Gold']:<10} |")
    print(f"| {'Silver':<10} | {tally['Silver']:<10} |")
    print(f"| {'Bronze':<10} | {tally['Bronze']:<10} |")

def display_team_medal_tally(team_tally):
    for team, tally in team_tally.items():
        print(team)
        print(f"\tGold:{tally['Gold']}, Silver:{tally['Silver']}, Bronze:{tally['Bronze']}")



file_path = "athlete_event.csv"
started(file_path)
error("Invalid Selection!")
complete()
menu()
dic = {"Gold": 10, "Silver": 5, "Bronze": 2}
display_medal_tally(dic)
display_team_medal_tally()

