import sys


def print_heart():
    print(" @@@ @@@")
    print("@   @   @")
    print("@       @")
    print("@       @")
    print(" @     @")
    print("  @   @")
    print("   @ @")
    print("    @")


for i in range(int(sys.argv[1])):
    print_heart()
