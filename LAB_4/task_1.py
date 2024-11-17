import json


def task() -> float:
    filename = 'input.json'
    sum_of_prods = 0
    with open(filename) as file:
        data = json.load(file)
    for dicts in data:
        prod_ = dicts.get("score") * dicts.get("weight")
        sum_of_prods += prod_
    formatted_sum = "{:.3f}".format(sum_of_prods)
    return float(formatted_sum)


print(task())
