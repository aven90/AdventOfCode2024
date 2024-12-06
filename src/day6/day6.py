"""
Part 1

Assignment:  sum of all places in the path of the guard (sum of X) before leaving the place
"""

# Open data
with open("src/day6/input.txt", "r") as f:
    data = f.read().splitlines()

roommap = [list(line) for line in data]

directions = ["^", ">", "v", "<"]

cur_pos = {"on_map": True}

for y_pos, line in enumerate(roommap):
    for x_pos, char in enumerate(line):
        if char in directions:
            cur_pos["dir"] = char
            cur_pos["y"] = y_pos
            cur_pos["x"] = x_pos

print(f"Starting on {cur_pos['y']}, {cur_pos['x']} in direction {cur_pos['dir']}")




def check_object(new_pos: list[int], room_map: list[str]) -> bool:
    if room_map[new_pos[0]][new_pos[1]] != "#":
        return True
    else:
        print("The guard hit a object")
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


# While the guard is still on the map
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

    print(cur_pos["dir"],new_pos)
    # we check if the move has a valid position, if yes we make the move
    if check_valid_move(new_pos, roommap):
        cur_pos, roommap = make_move(cur_pos, new_pos, roommap)
    else:
        roommap[cur_pos["y"]][cur_pos["x"]] = "X"
        print("The guard has left the room")
        cur_pos["on_map"] = False

# We count the number of X in the roommap
count = 0
for line in roommap:
    count += line.count("X")

print(f"The guard has visited {count} places")


