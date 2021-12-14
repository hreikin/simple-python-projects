spam = ["apples", "bananas", "tofu", "cats"]

def insert_string(list_to_print):
    for item in list_to_print[:-1]:
        print(item, end=', ')
    print('and', list_to_print[-1])

insert_string(spam)