import m_module
from m_module import puzzle
from sys import argv

args = map(int, argv[1:])

def main():
    a, b, tries = map(int, input('Input min, max and tries: ').split())
    if m_module.func(a, b, tries):
        print("Win")
    else:
        print("Lose")


if __name__ == '__main__':
    """Task3"""
    # if m_module.func(*args):
    #     print("Win")
    # else:
    #     print("Lose")

    """Task4"""
    # puzzle_text = input("Input puzzle: ")
    # solutions = input('Enter three solutions, separated by commas: ').split(',')
    # tries = int(input("Input number of tries: "))
    # print(puzzle(puzzle_text, solutions, tries))

    """Task5"""
    # m_module.puzzle_dict()
    """Task6"""
    # m_module.show_result()

    """Task7"""
    date = input("Enter date dd.mm.yyyyy: ")
    if m_module.calendar(date):
        print("The date is real")
    else:
        print('Wrong Earth')
