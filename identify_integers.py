#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Oct 2022
# This program identifies integers


def main():
    # this program identifies an integer

    # input
    print("Integer identifier.")
    user_int = int(input("Enter an integer: "))

    # process

    if user_int > 0:
        print("{0} is a positive integer.".format(user_int))
    elif user_int < 0:
        print("{0} is a negative integer.".format(user_int))
    else:
        print("{0} is zero.".format(user_int))

    # output
    print("\nDone.")


if __name__ == "__main__":
    main()
