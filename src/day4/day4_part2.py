import re

with open("src/day4/day4.txt", "r") as f:
    data = f.read().splitlines()

# part 2
"""
It seems we searched the incorrect values
instead of looking for XMAS we need to look for a X shaped MAS
F.E
M _ S
_ A _
M _ S

In each line look for patterns:

1. r"M.S"
2. r".A."
3. r"S.M"
4. r"M.M"
5  r"S.S"

If we find pattern 1, than pattern 2 needs to be in the next line followed by pattern in the following line

If all 3 patterns are found in a line we found a XMAS

Get all patterns, then cross reference the index positions
"""

# def find_pattern_occurance(pattern, data):
#     position = {}
#     for index, line in enumerate(data):
#         found_patterns = [m.start() for m in re.finditer(pattern, line)]
#         position[index] = found_patterns
#     return position

def find_pattern_occurance(pattern, data):
    position = {}
    for index, line in enumerate(data):
        m_s_patterns = []
        pos = 0
        while True:
            m = re.search(pattern, line[pos:])
            if m is None:
                break
            m_s_patterns.append(pos + m.start())
            pos += m.start() + 1
        position[index] = m_s_patterns
    return position



m_s_pattern = find_pattern_occurance(r"M.S", data)
a_pattern = find_pattern_occurance(r".A.", data)
s_m_pattern = find_pattern_occurance(r"S.M", data)
m_m_pattern = find_pattern_occurance(r"M.M", data)  
s_s_pattern = find_pattern_occurance(r"S.S", data)

# print(data[0])
# print(m_s_pattern)
print(f"{m_s_pattern=}\n{a_pattern=}\n{s_m_pattern=}\n{m_m_pattern=}\n{s_s_pattern=}")

"""
for key, val in dict1
    while key + 2 <= len(dict1.keys()) -1: 
    for item in val:
        if item + 1 dict2[k+1]:
            if item in dict3[k+2]:
                true
"""
def check_pattern(pattern1, pattern2, pattern3):
    count = 0
    for key, val in pattern1.items():
        if key + 2 <= len(pattern1.keys()) -1:
            for item in val:
                if item in pattern2[key+1]:
                    if item in pattern3[key+2]:
                        count += 1
    return count


pattern_comb = [
    (m_s_pattern, a_pattern, m_s_pattern),
    (s_m_pattern, a_pattern, s_m_pattern),
    (m_m_pattern, a_pattern, s_s_pattern),
    (s_s_pattern, a_pattern, m_m_pattern),
]

total_count = sum(map(lambda x:check_pattern(*x), pattern_comb))
print(total_count)