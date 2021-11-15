#!/usr/bin/env python3
"""Request NBA json form API to print pairs of players based on height"""
import requests
import sys


def adjacent_up(p, target, point):
    """Find adjacent pair right side"""
    if point >= size - 1:
        return
    if int(players[point + 1].get('h_in')) == target:
        pairs.append((p, point + 1))
        return adjacent_up(p, target, point + 1)
    else:
        return


def adjacent_down(p, target, mid):
    """Find adjacent pair left side"""
    if int(players[mid - 1].get('h_in')) == target:
        pairs.append((p, mid - 1))
        return adjacent_down(p, target, mid - 1)
    else:
        return


def find_pair(p, target, left, right):
    """Find pair"""
    # print('Finding pairs')
    # print(target, size, left, right)
    if left > right:
        return
    if left == right:
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
            return (
                adjacent_up(p, target, mid),
                adjacent_down(p, target, mid)
            )
    # print(str(left) + 'llllll')
    elif int(players[mid].get('h_in')) > target:
        return find_pair(p, target, left, mid - 1)
    else:
        return find_pair(p, target, mid + 1, right)


def get_names(pair):
    """"Get pair names"""
    player1, player2 = pair
    p1 = players[player1].get('first_name') + ' ' +\
        players[player1].get('last_name')
    p2 = players[player2].get('first_name') + ' ' +\
        players[player2].get('last_name')
    print('- {0:18} \t{1}'.format(p1, p2))


def search(size):
    """search"""
    for p in range(size):
        plyr1 = int(players[p].get('h_in'))
        plyr2 = total - int(players[p].get('h_in'))
        if plyr2 > max_height or plyr2 < min_height:
            continue
        if plyr1 > plyr2:  # stops search if current player greater than target
            break
        if plyr1 == plyr2:
            adjacent_up(p, plyr2, p),
            continue
        find_pair(p, plyr2, p, size - 1)
        # print(p)
        # print(plyr1)
    if len(pairs) > 0:
        for pair in pairs:
            get_names(pair)


if __name__ == '__main__':
    """NBA pairs of players by adding their height in inches
    Input must be a single 3 digit integer between 100 and 200"""

    url = 'https://mach-eight.uc.r.appspot.com/'
    print('Enter a 3 digit number to get pairs of NBA players\n'
          'that match your number with their height in inches')
    while True:
        total = input('NBA-pairs ')
        if total == 'q':
            sys.exit(0)
        try:
            total = int(total)
        except ValueError:
            print('You did not enter a valid 3 digit integer')
            continue
        r = requests.get(url)
        answer = r.json()
        if answer:
            players = sorted(answer['values'], key=lambda d: int(d['h_in']))
            size = len(players)
            min_height = int(players[0].get('h_in'))
            max_height = int(players[size - 1].get('h_in'))
            pairs = []
            if total >= 2 * min_height and total <= max_height * 2:
                search(size)

            if len(pairs) == 0:
                print('No matches found')
                print('Try again')
