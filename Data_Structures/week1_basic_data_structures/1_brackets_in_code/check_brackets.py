# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    length = 0
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i))
            length += 1

        if next in ")]}":
            # Process closing bracket, write your code here
            if length == 0 and i == 0:
                return 1
            if length > 0 and are_matching(opening_brackets_stack[length - 1].char, next):
                del opening_brackets_stack[-1]
                length -= 1
            else:
                return i + 1

    if length == 0:
        return 'Success'
    else:
        return opening_brackets_stack[-1].position + 1


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()