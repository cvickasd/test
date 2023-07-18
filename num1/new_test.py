one_people = 0
two_people = 0
three_people = 140
four_people = 0
five_people = 0

max_variable = max(['one_people', 'two_people', 'three_people', 'four_people', 'five_people'], key=lambda x: globals().get(x))

print(max_variable)
