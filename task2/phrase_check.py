def phrase_check(filename):
    count = 0
    with open(filename, "r") as file:
        for line in file:
            stripped_line = line.strip().split(" ")
            if all(count_word == 1 for count_word in [stripped_line.count(i) for i
                                                      in stripped_line]):
                count += 1
    return count


phrase_check("../data/skychallenge_skyphrase_input.txt")
