import pandas as pd


# Part 1
df_input = pd.read_csv("day1/day1.csv", sep=";")

print(df_input)

list_col1 = df_input["col1"].tolist()
list_col2 = df_input["col2"].tolist()

list_col1.sort(), list_col2.sort()

df_calc = pd.DataFrame({"col1": list_col1, "col2": list_col2})
df_calc["diff"] = abs(df_calc["col1"] - df_calc["col2"])
total = df_calc["diff"].sum()

print(f"The total is: {total}")


# Part 2
# check how often each num occurs in the list

count = dict()
for num in list_col1:
    count[num] = list_col2.count(num)

df_p2 = pd.DataFrame(count.items(), columns=["num", "count"])
df_filt = df_p2.query("count != 0").reset_index()

df_p2["mult"] = df_p2["num"] * df_p2["count"]
total_p2= df_p2["mult"].sum()
print(f"The total is: {total_p2}")
