# Open data
with open("src/day6/input.txt", "r") as f:
    roommap: list[str] = f.read().splitlines()


directions = ["^", ">", "v" "<"]

room_length: int = len(roommap)
room_width: int = len(roommap[0])

cur_pos = {"on_map": True}

for y_pos, line in enumerate(roommap):
    for x_pos, char in enumerate(line):
        if char in directions:
            cur_pos["dir"] = char
            cur_pos["y"] = y_pos
            cur_pos["x"] = x_pos

print(f"Starting on {cur_pos['y']}, {cur_pos['x']} in direction {cur_pos['dir']}")


def mark_map_position(current, new, room_map):
    pass


def check_valid_move(current, new, roommap) -> bool:
    if roommap[new][current["x"]] != "#":
        return True
    else:
        return False


def change_direction():
    pass


while cur_pos["on_map"]:
    match cur_pos["dir"]:
        case "^":
            new_y = cur_pos["y"] - 1
            if check_valid_move(cur_pos, new_y, roommap):
                roommap[new_y][cur_pos["x"]] = cur_pos["dir"]


            pass
        case ">":
            new_x = cur_pos["x"] + 1
            pass
        case "v":
            new_y = cur_pos["y"] + 1
            pass
        case "<":
            new_x = cur_pos["x"] - 1
        case _:
            print("The guard is left the room")
            cur_pos["on_map"] = False
