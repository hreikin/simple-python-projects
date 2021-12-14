# Write a function that takes a list value as an argument and returns
# a string with all the items separated by a comma and a space, with and
# inserted before the last item. For example, passing the previous spam list to
# the function would return 'apples, bananas, tofu, and cats' . But your func-
# tion should be able to work with any list value passed to it.

spam = ["apples", "bananas", "tofu", "cats"]

def insert_string(list_to_print):
    for item in list_to_print[:-1]:
        print(item, end=', ')
    print('and', list_to_print[-1])

insert_string(spam)