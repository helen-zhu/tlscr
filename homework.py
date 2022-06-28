
def join_all(thing):
    if isinstance(thing, str):
        return thing

    assert isinstance(thing, list)

    concat_thing = ""
    for item in thing:
        concat_thing += join_all(item)
    return concat_thing

join_all([["red", ["green", "blue"]], "lime"])

def longest(thing):
    if isinstance(thing, str):
        return len(thing)
    assert isinstance(thing, list)
    longest_thing = 0
    for item in thing:
        len_item = longest(item)
        if len_item > longest_thing:
            longest_thing = len_item
    return longest_thing


longest(["red", ["green", "blue"], ["lime"], [['purple'], ["pink", "darkorchid4", "grey"]]])

def add_len(thing):
    if isinstance(thing, int):
        return thing
    sum_thing = 0
    if isinstance(thing, dict):
        for item in thing.keys():
            sum_thing += add_len(thing[item])
    if isinstance(thing, list):
        for item in thing:
            sum_thing += add_len(item)
    return sum_thing


test_data = {"alpha": 1, "beta": {"gamma": [2, 3], "delta": [4, {"epsilon": 5}]}}
add_len(test_data)

def json_find(index_list, data):
    if len(index_list) == 1:
        return data[index_list[0]]
    else:
        new_data = data[index_list[0]]
        new_index = index_list[1:]
        return json_find(new_index, new_data)

test_data = {"alpha": 1, "beta": {"gamma": [2, 3], "delta": [4, {"epsilon": 5}]}}
test_index = ["beta", "delta", 1]
json_find(test_index, test_data)
