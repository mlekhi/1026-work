# defining the function with the required two lists as input
def merge_lists(firstList, secondList):
    # creating a new variable to store all the values from the two lists
    mergedList = firstList + secondList
    # removing duplicate values by turning the merged list into a set
    uniqueSet = set(mergedList)
    # sorting the set in ascending order
    sortedSet = sorted(uniqueSet)
    # converting the set back into a list and returning it
    sortedList = list(sortedSet)
    return sortedList