''' Python 3.9
8.11.2020

Write a Python program to print out a set containing
all the colors from color_list_1 which are not present
in color_list_2. Go to the editor
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}'''

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])


def color(set1, set2):
    return set1.difference((set2))


print(color(color_list_1, color_list_2))
