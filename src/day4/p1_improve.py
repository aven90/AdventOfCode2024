import numpy as np
import re

with open("src/day4/day4.txt", "r") as f:
    # this will also be the horizontal data
    data = f.read().splitlines()


total_list = []
for item in data:
    tmp = [char for char in item]
    total_list.append(tmp)
nparray = np.array(total_list)
arrshape = nparray.shape
print(nparray.shape)

# create diagonals
diags = [np.diag(nparray, k=i).tolist() for i in range(-arrshape[0], arrshape[1])]
diags = ["".join(sublist) for sublist in diags if sublist]

reverse_diags = [np.fliplr(nparray).diagonal(i).tolist() for i in range(-arrshape[0], arrshape[1])]
reverse_diags = ["".join(sublist) for sublist in reverse_diags if sublist]

# Verticals
verticals = ["".join(map(str, col)) for col in nparray.T]

# we combine all the strings
validate_list = data + verticals + diags + reverse_diags

# find all "xmas" in validate_list
found_xmas = re.findall(r"XMAS", " ".join(validate_list))

# find all "samx" in validate_list
found_samx = re.findall(r"SAMX", " ".join(validate_list))

print(f"total 'XMAS' found: {len(found_xmas) + len(found_samx)}")