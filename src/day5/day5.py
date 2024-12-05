"""
Part 1
We get a list of rules and a list of page orders

We need to check for each list of page orders if it is in the correct order
For this we need to map it against the rules.

The rules are in format X|Y where X needs to be before Y in the correct list

Once we have all the correct orders listed, we need to determine the page in the middle position
Then add up all middle page numbers

"""
with open("src/day5/rules.txt", "r") as f:
    rules = f.read().splitlines()
rules = [rule.split("|") for rule in rules]
rules = [list(map(int, rule)) for rule in rules]


with open("src/day5/orders.txt", "r") as f:
    orders = f.read().splitlines()

order_list = [order.split(",") for order in orders]
order_list = [list(map(int, order)) for order in order_list]

"""
For each order in order_list we iterate through page numbers
for each number we filter rules column x and then check if the other numbers are in the rules column y
We return True if the order is correct and False if not
If all are True, the order passes and is put in a different list

"""
def apply_rules(order, rules):
    """
    This function takes an order and a list of rules
    It returns the order if the order is correct according to the rules
    Otherwise it returns a dictionary with the order and the first rule which was not satisfied
    """
    
    checks = []
    bad_rule = []
    for rule in rules:
        if rule[0] in order and rule[1] in order:
            try:
                assert order.index(rule[0]) < order.index(rule[1])
                checks.append(True)
            except AssertionError:
                checks.append(False)
                bad_rule.append(rule)
        else:
            continue
    if all(checks):
        return order
    else:
        return {"order": order, "bad_rule": bad_rule}




checked_orders = [apply_rules(order, rules) for order in order_list]
correct_orders = [order for order in checked_orders if isinstance(order, list)]
bad_orders = [order for order in checked_orders if isinstance(order, dict)]
print(f"Total correct orders: {len(correct_orders)}")
print(f"Total bad orders: {len(bad_orders)}")

middle_vals = [item[len(item)//2] for item in correct_orders]
print(sum(middle_vals))

print(bad_orders)


"""
Part 2
"""

def change_order(order, rules):
    # Create a dictionary to store the rules
    """
    Takes an order and a list of rules
    Reorders the order according to the rules
    The rules are applied in the order they are given
    Returns the reordered list
    """
    checks = [False]
    applicable = []
    for rule in rules:
        if rule[0] in order and rule[1] in order:
            applicable.append(rule)
    # print(applicable)

    while not all(checks):
        checks = []
        for rule in applicable:
            first_index = order.index(rule[0])
            second_index = order.index(rule[1])
            try:
                assert first_index < second_index
                checks.append(True)
                # print(f"rule {rule} is correct")
            except AssertionError:
                order[first_index], order[second_index] = order[second_index], order[first_index]
                checks.append(False)
                # print(f"rule {rule} is incorrect, switched order {order}")


    return order


# Reorder the input list
bad_orders_list = [orders["order"] for orders in bad_orders]
reshuffeled_list = [change_order(order, rules) for order in bad_orders_list]

middle_vals_bad = [item[len(item)//2] for item in reshuffeled_list]
print(sum(middle_vals_bad))