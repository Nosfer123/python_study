def is_concatenation(dictionary, key):
    if not key:
        return True
    idx = 1
    while idx <= len(key):
        if key[0:idx] in dictionary and is_concatenation(dictionary, key[idx:]):
            return True
        idx += 1
    return False

test_dict = ["world", "hello", "super"]
print(test_dict)
print("helloworld", is_concatenation(test_dict, 'helloworld'))