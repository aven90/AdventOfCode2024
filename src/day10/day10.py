import re
import pandas as pd

"""
Day 10 of Advent of Code 2024

Today we arrived at a lava production facility and are prodded by a reindeer.
we have to fill a blank topographic map with the missing hiking paths

The topographic map indicates the height at each position using a scale from 0 (lowest) to 9 (highest).

a good hiking trail:
 - is as long as possible
 - has an even, gradual uphill slope

For all practical purposes, this means that a hiking trail is any path that starts at height 0,  ends at height 9, 
and always increases by a height of exactly 1 at each step. 
Hiking trails never include diagonal steps - only 
up (row -1 ), 
down (row + 1), 
left ( col -1 )
right (col + 1) 

A trailhead is any position that starts one or more hiking trails and start at 0
a trailhead's score is the number of 9-height positions reachable from that trailhead
"""

def parse_map_data(data):
    map_data = [list(line) for line in data]
    _map = pd.DataFrame(map_data, dtype=float)
    trail_heads = []
    for i, line in enumerate(data):
        heads = [m.start() for m in re.finditer(r"0", line)]
        for pos in heads:
            trail_heads.append((i, pos))


    return _map, trail_heads

def find_new_pos(pos, map_len, map_width):
    """
    Finds all new positions in a map, given the current position

    Parameters
    ----------
    pos : tuple
        The current position in the map
    map_len : int
        The length of the map
    map_width : int
        The width of the map

    Returns
    -------
    coords : list
        A list of new positions that can be reached from the current position

    Notes
    -----
    The new positions are calculated by moving one step up, down, left or right from the current position.
    If the new position is outside the map, it is not included in the list.
    """
    direction = ["up", "down", "left", "right"]
    coords = []
    for dir in direction:
        match dir:
            case "up":
                new_pos = (pos[0] - 1, pos[1])
            case "down":
                new_pos = (pos[0] + 1, pos[1])
            case "left":
                new_pos = (pos[0], pos[1] - 1)
            case "right":
                new_pos = (pos[0], pos[1] + 1)
            case _:
                raise ValueError(f"Unknown direction {dir}")
        if new_pos[0] < 0 or new_pos[0] >= map_len or new_pos[1] < 0 or new_pos[1] >= map_width:
            continue
        coords.append(new_pos)
    return coords


def find_trails_for_start(_map, start, map_len, map_width):
    """
    Finds all trails from a given start position in the map, as well as the score and rating of that trailhead

    Parameters
    ----------
    _map : pd.DataFrame
        The map data
    start : tuple
        The starting coordinates of the trailhead
    map_len : int
        The length of the map
    map_width : int
        The width of the map

    Returns
    -------
    score : int
        The score of the trailhead, which is the number of unique 9-height positions reachable from the trailhead
    rating : int
        The rating of the trailhead, which is the total number of 9-height positions reachable from the trailhead
    """
    curr_height = 0.0
    trails = {curr_height: [start]}
    pos = trails[curr_height][0]
    next_height = curr_height + 1
    
    while next_height < 10:
        # For each known coords in current height, find new coords
        new_trails = []     
        for pos in trails[curr_height]:

            # retrieve coords for all new positions
            new_positions = find_new_pos(pos, map_len, map_width)

            for new_pos in new_positions:
                if _map.iloc[new_pos] == next_height:
                    new_trails.append(new_pos)
        trails[next_height] = new_trails
        curr_height += 1
        next_height = curr_height + 1

    rating = len(trails[9])
    score = len(set(trails[9]))

    return score, rating

def solution(data):
    """
    Solution direction:
    1) find all trails heads starting coords in map
    2) for each trail head, find the number of 9s reachable from it in the map
    for start in trails:
        
    """
    _map, trail_heads = parse_map_data(data)
    map_len = len(_map)
    map_width = len(_map[0])
    score = 0
    rating = 0
    # print(f"Found {len(trail_heads)} trail heads")
    for start in trail_heads:
        score_trail, rating_trail = find_trails_for_start(_map, start, map_len, map_width)
        score += score_trail
        rating += rating_trail
    print(f"Part 1 score is {score}")
    print(f"Part 2 rating is {rating}")



def main():
    with open("src/day10/input.txt", "r") as f:
        data = f.read().splitlines()
    solution(data)

if __name__ == "__main__":
    main()