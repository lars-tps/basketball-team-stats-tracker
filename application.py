import constants
import random
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def experience_to_boolean(player_dicts):
    """converts the values inside the 'experience' key of input dictionary into booleans"""
    for individual in player_dicts:
        if individual['experience'] == 'YES':
            individual['experience'] = True
        else:
            individual['experience'] = False
    return player_dicts


def height_to_integer(player_dicts):
    """converts the values inside the 'height' key of input dictionary into integers, units are still inches!"""
    for individual in player_dicts:
        ints = []
        for i in individual['height']:
            if i.isnumeric() is True:
                ints.append(i)
                individual['height'] = int(''.join(ints))
    return player_dicts


def guardians_to_list(player_dicts):
    """converts the values inside the 'guardians' key of input dictionary into a list of names"""
    for individual in player_dicts:
        str_replace = individual['guardians'].replace('and', ', ')
        str_split = str_replace.split(', ')
        individual['guardians'] = str_split
    return player_dicts


def team_balance(team_list, player_dicts):
    team_size = len(player_dicts) // len(team_list)
    num_experienced = 0
    experienced_pool = list()
    inexperienced_pool = list()
    for individual in player_dicts:
        if individual['experience'] is True:
            num_experienced += 1
            experienced_pool.append(individual)
        else:
            inexperienced_pool.append(individual)
    exp_ratio = num_experienced / len(player_dicts)
    player_ratio = int(exp_ratio * team_size)

    assigned_teams = list()
    for team in team_list:
        exp_selection = random.sample(experienced_pool, player_ratio)
        inexp_selection = random.sample(inexperienced_pool, player_ratio)
        assigned_teams.append([team, exp_selection + inexp_selection])
        for i in exp_selection:
            experienced_pool.remove(i)
        for i in inexp_selection:
            inexperienced_pool.remove(i)
    return assigned_teams


def debug_display_stats(assigned_teams):
    for assignment in assigned_teams:
        print(f"Team Name: {assignment[0]}")
        for selected_players in assignment[1:]:
            print("Players: ")
            for individuals in selected_players:
                print(f"    {individuals['name']}")


def display_team_stats(selected_team):
    print(f"Team Name: {selected_team[0]}\n{'-'*25}")
    print(f"There are {len(selected_team[1])} players on this team")
    name_list = list()
    experienced_players = list()
    inexperienced_players = list()
    guardians_list = list()
    total_height = 0
    for selected_players in selected_team[1:]:
        for individuals in selected_players:
            name_list.append(individuals['name'])
            if individuals['experience'] is True:
                experienced_players.append(individuals)
            else:
                inexperienced_players.append(individuals)
        for individuals in selected_players:
            total_height += individuals['height']
        for individuals in selected_players:
            for guardian in individuals['guardians']:
                guardians_list.append(guardian)
    avg_height = total_height/len(selected_team[1])
    str_join = ', '.join(name_list)
    guardians = ', '.join(guardians_list)
    print(f"""
Players in this team:
  ~{str_join}
Guardians:
  ~{guardians}

Experienced players: {len(experienced_players)} players
Inexperienced players: {len(inexperienced_players)} players
Average height: {avg_height} inches
""")
    input("Press ENTER or RETURN to continue")


def menu_prompt():
    possible_choice = {1, 2}
    while True:
        try:
            choice = int(input(">  "))
            if choice not in possible_choice:
                raise ValueError
            break
        except ValueError:
            print("**Error!**\nPlease select an option by entering the associated number.")
            continue
    return choice


def team_selection_prompt():
    possible_choice = {1, 2, 3}
    while True:
        try:
            choice = int(input(">  "))
            if choice not in possible_choice:
                raise ValueError
            break
        except ValueError:
            print("**Error!**\nPlease select an option by entering the associated number.")
            continue
    return choice


def tool_loop():
    global loop
    print("BASKETBALL TEAM STATS TOOL\n\n[MENU]\n1) Display Team Stats\n2) Quit\n\n")
    menu_choice = menu_prompt()
    clear_screen()
    if menu_choice == 1:
        print(f"Please select a team\n\n1) {team1[0]}\n2) {team2[0]}\n3) {team3[0]}\n\n")
        team_choice = team_selection_prompt()
        clear_screen()
        if team_choice == 1:
            display_team_stats(team1)
            clear_screen()
        if team_choice == 2:
            display_team_stats(team2)
            clear_screen()
        if team_choice == 3:
            display_team_stats(team3)
            clear_screen()
    if menu_choice == 2:
        clear_screen()
        print("Thanks for using this tool. Have a nice day!")
        loop = False


if __name__ == '__main__':
    players = constants.PLAYERS[:]
    teams = constants.TEAMS[:]
    experience_to_boolean(players)
    height_to_integer(players)
    guardians_to_list(players)
    balanced_teams = team_balance(teams, players)
    team1 = balanced_teams[0]
    team2 = balanced_teams[1]
    team3 = balanced_teams[2]
    loop = True
    while loop is True:
        tool_loop()

