"""
Part 1

Assignment:  sum of all places in the path of the guard (sum of X) before leaving the place
"""
import re


# Open data
with open("src/day6/input.txt", "r") as f:
    data = f.read().splitlines()

#Create room map
roommap = [list(line) for line in data]
original_map = [list(line) for line in data]

# Set possible directions
directions = ["^", ">", "v", "<"]

# initiatie current position
cur_pos = {"on_map": True}

# find current position in map
for y_pos, line in enumerate(roommap):
    for x_pos, char in enumerate(line):
        if char in directions:
            cur_pos["dir"] = char
            cur_pos["y"] = y_pos
            cur_pos["x"] = x_pos
room_start = [cur_pos["dir"], [cur_pos["y"], cur_pos["x"]]]

# print(f"Starting on {cur_pos['y']}, {cur_pos['x']} in direction {cur_pos['dir']}")


def check_object(new_pos: list[int], room_map: list[str]) -> bool:
    if room_map[new_pos[0]][new_pos[1]] != "#":
        return True
    else:
        # print(f"The guard hit a object at {new_pos}")
        return False


def change_direction(current: str, directions: list[str]) -> dict:
    dir_index = directions.index(current)
    new_dir_index = (dir_index + 1) % len(directions)
    new_dir = directions[new_dir_index]
    return new_dir

def update_roommap(current: dict, new: list[int], room_map):
    # mark the new position with direction
    roommap[new[0]][new[1]] = current["dir"]
    roommap[cur_pos["y"]][cur_pos["x"]] = "X"
    return roommap

def check_valid_move(new: list[int], room_map):
    length = len(room_map)
    width = len(room_map[0])
    if 0 <= new[0] < length and 0 <= new[1] < width:
        return True
    else:
        return False

def make_move(cur_pos: dict, new_pos, room_map):
    if check_object(new_pos, room_map):
        room_map = update_roommap(cur_pos, new_pos, room_map)
        cur_pos["y"] = new_pos[0]
        cur_pos["x"] = new_pos[1]
    else:
        cur_pos["dir"]= change_direction(cur_pos["dir"], directions)
    return cur_pos, room_map


all_paths = []
# While the guard is still on the map, we retrieve it's path
while cur_pos["on_map"]:

    # We retrieve the new position
    match cur_pos["dir"]:
        case "^":
            new_pos = [cur_pos["y"] -1, cur_pos["x"]]

        case ">":
            new_pos = [cur_pos["y"], cur_pos["x"] + 1]

        case "v":
            new_pos = [cur_pos["y"] + 1, cur_pos["x"]]

            pass
        case "<":
            new_pos = [cur_pos["y"], cur_pos["x"] - 1]

        case _:
            raise ValueError(f"Unknown direction {cur_pos['dir']}")

    all_paths.append(new_pos)
    # we check if the move has a valid position, if yes we make the move
    if check_valid_move(new_pos, roommap):
        cur_pos, roommap = make_move(cur_pos, new_pos, roommap)
    else:
        roommap[cur_pos["y"]][cur_pos["x"]] = "X"
        # print("The guard has left the room")
        cur_pos["on_map"] = False




## part 2

all_obstacles = []
for index, line in enumerate(data):
    obs = [m.start() for m in re.finditer("#", line)]
    for obj in obs:
        all_obstacles.append([index, obj])

# update the path by removing the obstacales
objects_encountered = []
for obj in all_obstacles:
    for p in all_paths:
        # print(p)
        if obj == p:
            objects_encountered.append(p)
            all_paths.remove(p)

# print(all_paths)

# initiate container for possible objects
possible_obj = []


print("\n\nStart part 2")

sub_list = [[6,3]]

# for each position in the path we check if we can add objects
for pos in all_paths:
    # reset initial position

    changed_map = [list(line) for line in data]
    # print(pos)
    init_pos = {"on_map": True}
    for y_pos, line in enumerate(changed_map):
        for x_pos, char in enumerate(line):
            if char in directions:
                init_pos["dir"] = char
                init_pos["y"] = y_pos
                init_pos["x"] = x_pos

    try:
        changed_map[pos[0]][pos[1]] = "#"
    except IndexError:
        continue

    # print(f"Starting on {start_p2['y']}, {start_p2['x']} in direction {start_p2['dir']}")
    starting = [init_pos["y"], init_pos["x"]]
    if pos == starting:
        continue

    # init_pos = start_p2.copy()
    print(f"Adding object in position {pos}")
    # print("Starting on:", init_pos)


    # reset counter
    counter = 0
    other_counter = 0
    first_round = []
    second_round = []
    found_loop = False
    first_encounter = False
    second_encounter = False
    third_encounter = False
    # reset map and add the extra object in the path on the map

    # print(first_encounter, second_encounter, third_encounter)
    # print(first_round)
    # print(second_round)
    # while the guard is still on the map and we didn't find the exta objects 3 times from the same direction

    while init_pos["on_map"] and not found_loop and other_counter < 100:
        # We retrieve the new position
        match init_pos["dir"]:
            case "^":
                new_pos = [init_pos["y"] -1, init_pos["x"]]

            case ">":
                new_pos = [init_pos["y"], init_pos["x"] + 1]

            case "v":
                new_pos = [init_pos["y"] + 1, init_pos["x"]]

                pass
            case "<":
                new_pos = [init_pos["y"], init_pos["x"] - 1]

            case _:
                raise ValueError(f"Unknown direction {init_pos['dir']}")
            
        # print(new_pos)
        # print(changed_map[6])
        # we check if the move has a valid position, if yes we make the move
        if check_valid_move(new_pos, changed_map):
            if changed_map[new_pos[0]][new_pos[1]] != "#":
                changed_map[new_pos[0]][new_pos[1]] = init_pos["dir"]
                changed_map[init_pos["y"]][init_pos["x"]] = "X"   
                init_pos["y"] = new_pos[0]
                init_pos["x"] = new_pos[1]
            else:
                # print(pos, new_pos)
                # print(f"The guard hit a object at {new_pos}")
                if pos == new_pos and not first_encounter and not second_encounter and not third_encounter:
                    # if counter = 0, we hit it for the first time
                    print("starting first round, set first encounter to true")
                    first_round.append(new_pos)
                    first_encounter = True
                    # print(first_round)
                    # print(counter)
                elif pos == new_pos and first_encounter and not second_encounter and not third_encounter:
                    # if counter = 1, object we hit after hitting the new block
                    print("Starting second round, set second encounter to true")
                    second_round.append(new_pos)
                    second_encounter = True
                elif pos == new_pos and first_encounter and second_encounter and not third_encounter:
                    third_encounter = True
                elif first_encounter and not second_encounter and not third_encounter:
                    # print("still in first round")
                    first_round.append(new_pos)
                    other_counter += 1
                    # print(first_round)
                elif first_encounter and second_encounter and not third_encounter:
                    second_round.append(new_pos)
                    other_counter += 1
                    # print("still in second round")
                    # print(second_round)
                elif third_encounter:
                    # print("third round, check if it's a loop")

                    if first_round == second_round:
                        print("it's a loop")
                        found_loop = True
                    else:
                        other_counter += 1
                else:
                    other_counter += 1
                init_pos["dir"]= change_direction(init_pos["dir"], directions)

        else:
            # changed_map[init_pos["y"]][init_pos["x"]] = "X"
            print("The guard has left the room")
            init_pos["on_map"] = False

    if found_loop or other_counter >= 100:
        print(f"Found potential object at {pos}")
        possible_obj.append(f"{pos[0], pos[1]}")
        # print(possible_obj)
    # print("\n")
# print(set(possible_obj))
print(f"found {len(set(possible_obj))} potential objects")