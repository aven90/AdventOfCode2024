
from dataclasses import dataclass
  
def part2(data):
    # import data
    datalist = []
    x = 0
    for index, val in enumerate(data):
        files = []
        if index % 2 == 0:
            for i in range(int(val)):
                files.append(x)
                # datalist.append(str(x))
            x += 1
        else:
            for _ in range(int(val)):
                files.append(x)
        datalist.append(files)
    datalist = [d for d in datalist if d]
    # print(datalist)
    
    numbs = []
    for i, val in enumerate(datalist):
        if val.isdigit():
            numbs.append(i)
    # print(numbs)

    """
    for each file we gonna check if they can be matched with the free spaces 
    while the free space is earlier than the file
    """
    
    slots = []
    for slot_index, slot in enumerate(datalist):
        if "." in slot:
            slots.append(slot_index)
            break


    # we get all files
    all_files = []
    for i, val in enumerate(datalist):
        if val.isdigit():
            all_files.append(val)
    
    for file in all_files[::-1]:
        old_file_index = datalist.index(file)
        for slot in slots:
            if slot > old_file_index:
                break

            elif len(datalist[slot]) >= len(file):
                # new memory slot size
                new_slot = datalist[slot][len(file):]
                
                # we create the memory replace for file
                old_file_loc = ""
                for _  in range(len(file)):
                    old_file_loc += "."

                # we replace stuff
                datalist[old_file_index] = old_file_loc
                datalist[slot] = file
                if len(new_slot) > 0:
                    datalist.insert(slot + 1, new_slot)
                break
            else:
                pass

    # print(datalist)
        new_data = []
        temp = []
        for i in datalist:
            if i.isdigit():
                if len(temp) > 0:
                    new_data.append("".join(temp))
                    temp = []
                new_data.append(i)
            else:
                temp.append(i)
        datalist = new_data

            # we reset 
        slots = []
        
        for slot_index, slot in enumerate(datalist):
            if "." in slot:
                slots.append(slot_index)


    
    data_check = "".join(datalist)
    total = []
    for index, val in enumerate(data_check):
        if val == ".":
            continue
        else:
            total.append(index*int(val))

    # print(sum(total))

    try: 
        assert sum(total) == 6420913943576
        print("Part 2 works")
    except AssertionError:
        print("Part 2 failed")

def main():

    file = "input"
    with open(f"src/day9/{file}.txt", "r") as f:
        data = f.read()
    part2(data)
 

if __name__ == "__main__":
    main()