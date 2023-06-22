# defining the function with the required words parameter
def last_first_pairs(words):
    # creating a new set that stores the last/first matching tuples
    matchingSets = set()
    # for loop through each of the words
    for word1 in words:
        for word2 in words:
            # checking if the last letter of word1 matches the first letter of word2
            if word1[-1] == word2[0]:
                # adding the tuples into the set if the above condition is met
                matchingSets.add((word1, word2))
    # sort all the matching sets in lexicographical order
    sortedMatchingSets = sorted(matchingSets)
    # returning the sorted matching sets
    return sortedMatchingSets


