import constants

# clean up player data (e.g Height should be integers, experience should be booleans)

players = constants.PLAYERS[:]
teams = constants.TEAMS[:]


def experience_to_boolean(player_dicts):
    for player in player_dicts:
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
    return player_dicts


def height_to_integer(player_dicts):
    for player in player_dicts:
        ints = []
        for i in player['height']:
            if i.isnumeric() is True:
                ints.append(i)
                player['height'] = int(''.join(ints))
    return player_dicts


if __name__ == '__main__':
    experience_to_boolean(players)
    height_to_integer(players)
