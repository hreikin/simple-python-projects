# Write a function named printTable() that takes a list of lists of strings
# and displays it in a well-organized table with each column right-justified.
# Assume that all the inner lists will contain the same number of strings.
#
# Hint: Your code will first have to find the longest string in each of the
# inner lists so that the whole column can be wide enough to fit all the strings.
# You can store the maximum width of each column as a list of integers. The
# printTable() function can begin with colWidths = [0] * len(tableData) , which
# will create a list containing the same number of 0 values as the number of
# inner lists in tableData . That way, colWidths[0] can store the width of the
# longest string in tableData[0] , colWidths[1] can store the width of the
# longest string in tableData[1] , and so on. You can then find the largest
# value in the colWidths list to find out what integer width to pass to the
# rjust() string method.

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]


def printTable():
    # Three columns, Fruit, Name, Animal
    column_lengths = [0] * len(tableData)
    _ = 0
    for dataset in tableData:
        for item in dataset:
            # Only keep the longest length
            if len(item) > column_lengths[_]:
                column_lengths[_] = len(item)
        # increment the iterator for the column_lengths index
        _ += 1

    i = 0
    # Each list is the same length (specified by the task) so len() is the same regardless
    while i < len(tableData[0]):
        column_tracker = 0
        # Print each item accessed by using i for the correct index. This also works for column_lengths
        while column_tracker < len(column_lengths):
            print(f" | {tableData[column_tracker][i].rjust(column_lengths[column_tracker])}", end="")
            column_tracker += 1
        print(" |")
        i += 1


if __name__ == '__main__':
    printTable()