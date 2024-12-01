# Prep file input from text to csv
infile = "day1.txt"
outfile= "day1.csv"

with open(infile, "r") as f:
    inputfile = f.read()

inputfile = inputfile.replace(" ", ";")
with open(outfile, "w") as f:
    f.write(inputfile) 