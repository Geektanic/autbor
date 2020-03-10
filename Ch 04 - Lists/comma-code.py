# comma-code.py
# Takes a list and writes it out with commas and "and" before last item.

spam = ["apples", "bananas", "tofu", "cats"]

def get_list():
    user_list = []
    while True:
        entry_item = input("Enter an item (\"!q\" to quit): ")
        if entry_item == "!q":
            break
        else:
            user_list.append(entry_item)
    return(user_list)


def commas(orig_list):
    return_string = ""
    for item in range(len(orig_list)):
        if item == 0:
            return_string = f"{orig_list[item]}, "
        elif item < (len(orig_list) - 1):
            return_string = return_string + f"{orig_list[item]}, "
        else:
            return_string = return_string + f"and {orig_list[item]}"
    return(return_string)

print("We need to get a list of items.")
print("At each prompt enter an individual item in your list.")
print("To finish use \"!q\".")

spam = get_list()

if len(spam) == 0:
    print("We end up with an empty list.")
else:
    print_this = commas(spam)
    print(print_this)