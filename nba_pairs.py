#!/usr/bin/env python3
"""Request NBA json form API to print pairs of players based on height"""
import requests
import sys


def adjacent_up(p, target, mid):
    """Performs linear search to find adjacent pair right side
    Args:
        p: integer indicating the index of player in list of players
            looking for matches
        target: integer indicating height of player to look for
        mid: index of match found, to search in adjacent index
    Return:calls to linear search adjacent_down if a pair is found
            appends tuple with pair match to pairs list
            None if no match is found
    """
    if mid >= size - 1:
        return
    if int(players[mid + 1].get('h_in')) == target:
        pairs.append((p, mid + 1))
        return adjacent_up(p, target, mid + 1)
    else:
        return


def adjacent_down(p, target, mid):
    """Performs linear search to find adjacent pair left side
    Args:
        p: integer indicating the index of player in list of players
            looking for matches
        target: integer indicating height of player to look for
        mid: index of match found, to search in adjacent index
    Return:calls to linear search adjacent_down if a pair is found
            appends tuple with pair match to pairs list
            None if no match is found
    """
    if int(players[mid - 1].get('h_in')) == target:
        pairs.append((p, mid - 1))
        return adjacent_down(p, target, mid - 1)
    else:
        return


def find_pair(p, target, left, right):
    """Find pair performs recursive binary search to get first match
    Args:
        p: integer indicating the index of player in list of players
            looking for matches
        target: integer indicating height of plaer to look for
        left: integer indicating the left boundary to start binary search
        right: integer indicating the right boundary to start binary search
    Return: calls to linear search(adjacent_up and down) if a pair is found
            appends tuple with pair match to pairs list
            None if no match is found
    """
    if left > right:
        return
    if left == right:
        # if player 1 is equal to target return, avoid self pairing
        if p == left:
            return
        if int(players[left].get('h_in')) == target:
            pairs.append((p, left))
        return
    mid = int((right + left) / 2)
    if int(players[mid].get('h_in')) == target:
        if p == mid:
            return
        else:
            pairs.append((p, mid))
            # call for linear search to find adjacent matches
            return (
                adjacent_up(p, target, mid),
                adjacent_down(p, target, mid)
            )
    elif int(players[mid].get('h_in')) > target:
        return find_pair(p, target, left, mid - 1)
    else:
        return find_pair(p, target, mid + 1, right)


def print_names(pair):
    """"Print pair names
    Args:
        pair: is a tuple containing the players that match user input

    Return: None
            prints each pair match to screen in the order
            the small player on the left and the tall on the right
    """
    player1, player2 = pair
    p1 = players[player1].get('first_name') + ' ' +\
        players[player1].get('last_name')
    p2 = players[player2].get('first_name') + ' ' +\
        players[player2].get('last_name')
    print('- {0:18} \t{1}'.format(p1, p2))


def search(size):
    """search for pairs in list
    Args:
        size:is an integer with the number of players in the list
        players: is the list of dictionaries containing the players info
        """
    for p in range(size):
        plyr1 = int(players[p].get('h_in'))  # store first player height
        plyr2 = total - int(players[p].get('h_in'))  # height to look for
        # when player 2 height is out of range of the max or min value continue
        if plyr2 > max_height or plyr2 < min_height:
            continue
        # stops search if current player greater than target
        if plyr1 > plyr2:
            break
        # start linear search when player 1 height is equal to player 2
        if plyr1 == plyr2:
            adjacent_up(p, plyr2, p),
            continue
        # starts binary search for first match
        find_pair(p, plyr2, p, size - 1)
        # print(p)
        # print(plyr1)
    # if at least one pair is matched print the list of pairs
    if len(pairs) > 0:
        for pair in pairs:
            print_names(pair)


if __name__ == '__main__':
    """NBA pairs of players by adding their height in inches
    Input must be a single 3 digit integer between 100 and 200"""

    url = 'https://mach-eight.uc.r.appspot.com/'
    # Initial message for user
    print('Enter a 3 digit number to get pairs of NBA players\n'
          'that match your number with their height in inches')
    while True:
        total = input('NBA-pairs ')
        if total == 'q':
            sys.exit(0)
        # Validation of input as an integer
        try:
            total = int(total)
        except ValueError:
            print('You did not enter a valid 3 digit integer')
            continue
        r = requests.get(url)

        answer = r.json()
        if answer:
            # sort players by h_in height in inches
            players = sorted(answer['values'], key=lambda d: int(d['h_in']))
            size = len(players)
            # define boundaries of search
            min_height = int(players[0].get('h_in'))
            max_height = int(players[size - 1].get('h_in'))
            pairs = []  # list to store valid pairs
            if 2 * min_height <= total <= max_height * 2:
                search(size)

            if len(pairs) == 0:
                print('No matches found')
                print('Try again')
        else:
            print('Answer to request is not a valid JSON')
