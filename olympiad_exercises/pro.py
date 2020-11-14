size = input()
size = size.split()
width = ""


# size[0] to wysokość a [1] to szerokość

def print_edge():
    print("X" * int(size[1]))


def print_center():
    print("X" + (" " * (int(size[1]) - 2)) + "X")


print_edge()

for i in range(int(size[0]) - 2):
    print_center()

print_edge()
