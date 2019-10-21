#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on September 2019
# This program uses a while loop
# To add consecutive numbers up to a chosen number


def main():
    # This function Calculates the sum using a while loop
    loop_counter = 0
    answer = 0

    # input
    number = int(input("Enter a positive integer: "))
    print("")

    # process and output
    while loop_counter < number:
        print("{0} times through loop: ".format(loop_counter))
        loop_counter = loop_counter + 1
        answer = answer + loop_counter

    print("The sum of all integers up to your entry is: ", answer)


if __name__ == "__main__":
    main()
