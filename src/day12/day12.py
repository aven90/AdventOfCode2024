import re
import pandas as pd

"""
Day 12 of Advent of Code 2024

Today we are at a garden with regions of plots
We have to calculate the cost of the fence around each region

To do this we need to find:
- the perimiter of each region
- the area which is the number of plots in the region

The price is then calculated as:
perimiter * area

Solution direction:
1) import data as array (see day 10)
2) find all regions in the regions, 
    like day 10 we can find the coords of the start of each region
    then see if the next coord in (up, down, left, right) is in the same region
    we update the map with # for each plot processed
3) for each region, find the perimiter
    in step we can make a do a counter based on the where we find the plots
4) for each region, calculate the amount of plots
5) calculate the price
6) calculate the total price as sum of prices
"""
def parse_map_data(data):
    """
    Parse the map data to a pandas DataFrame and set of plot types

    Args:
        data (list): list of strings where each string is a line in the map

    Returns:
        tuple: (map, plot_types)
            map (pd.DataFrame): a pandas DataFrame of the map
            plot_types (set): a set of all plot types found in the map
    """
    map_data = [list(line) for line in data]
    _map = pd.DataFrame(map_data, dtype=str)
    plot_types = set("".join(data))
    return _map, plot_types

def find_next_pos(pos, map_len, map_width):
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

def determine_price(_map, plot_type, map_len, map_width):
    
    print(plot_type)
    plot_map = _map.where(_map == plot_type)
    plot_map = plot_map.dropna(how="all", axis=0).dropna(how="all", axis=1).fillna("#")
    plot_size = plot_map.shape
    check_plots = True
    # define perimeter
    while check_plots:
        if plot_map.iloc[(0,0)] == "#":
            pass
        else:
            find_next_pos((0,0), map_len, map_width)


        
        print(plot_map.iloc[plot_start])
        check_plots = False
    # define area

    price = 1

    

    return price





def solution(data):
    _map, plots = parse_map_data(data)
    map_len = len(_map)
    map_width = len(_map[0])
    price = 0
    print(_map)
    print(plots)
    # print(f"Found {len(trail_heads)} trail heads")
    # for plot_type in plots:
    price += sum(determine_price(_map, plot_type, map_len, map_width) for plot_type in plots)

    # print(f"Part 1 score is {score}")
    # print(f"Part 2 rating is {rating}")



def main():
    with open("src/day12/example.txt", "r") as f:
        data = f.read().splitlines()
    solution(data)

if __name__ == "__main__":
    main()