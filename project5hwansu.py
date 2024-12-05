# CSC 110
# Project 5 - Main File
# Hwansu Kim (Billy)
# 10/27/21
# This program displays the results of four functions, that are unrelated to each other. This program is more
# akin to a module file, if not for the call to main().


# Describes an employee's performance based on their numerical rating, on a scale of 1 to 10.
def empRating(numRating):
    ratingDescription = "ERROR"
    if numRating == 1 or numRating == 2:
        ratingDescription = "Probation"

    elif numRating == 3 or numRating == 4:
        ratingDescription = "Needs Improvement"

    elif numRating == 5 or numRating == 6 or numRating == 7:
        ratingDescription = "Acceptable"

    elif numRating == 8 or numRating == 9:
        ratingDescription = "Good"

    elif numRating == 10:
        ratingDescription = "Excellent"

    return ratingDescription


# Converts a percent-based grade into NSC's 4.0 grading scale.
def pctToNsc(gradePercentage):
    nscGrade = -9.9
    if 0 <= gradePercentage <= 100:
        nscGrade = (gradePercentage - 60) / 10 + .4

        if nscGrade < 1.0:
            nscGrade = 0
        elif nscGrade > 4.0:
            nscGrade = 4.0

    return nscGrade


# Confirms whether an integer is divisible by 5, 7, or 11.
def isDivisibleBy5or7or11(integer):
    isDivisible = integer % 5 == 0 or integer % 7 == 0 or integer % 11 == 0
    if isDivisible:
        result = True
    else:
        result = False
    return result


# Calculates an employee's commission based on their position, in-state sales, out-of-state sales, and their tenure at
# the company in months.
def commission(empPosition, inStateSales, outOfStateSales, tenureInMonths):
    commissionBump = 0
    if 24 <= tenureInMonths <= 47:
        commissionBump = 0.01

    elif 48 <= tenureInMonths <= 119:
        commissionBump = 0.02

    elif tenureInMonths >= 120:
        commissionBump = 0.03

    inStateRate = 0
    outOfStateRate = 0
    if empPosition == "Trainee":
        inStateRate = 0.01
        outOfStateRate = 0.02

    elif empPosition == "Associate":
        inStateRate = 0.03
        outOfStateRate = 0.05

    elif empPosition == "Lead":
        inStateRate = 0.04
        outOfStateRate = 0.06

    elif empPosition == "Manager":
        inStateRate = 0.05
        outOfStateRate = 0.08

    salesCommission = inStateSales * inStateRate + outOfStateSales * outOfStateRate
    totalCommission = salesCommission + salesCommission * commissionBump

    return totalCommission


def main():
    print(empRating(10))
    print(format(pctToNsc(66), ".1f"))
    print(isDivisibleBy5or7or11(1))
    print(format(commission("Associate", 4000, 5000, 36), ".2f"))


main()


# SUMMARY

#    I started the project by creating stubbed function definitions for all five functions. Then, I started to work my
# way down the list of functions for the projects, starting with empRating(). Now, following the last project, I wanted
# to try test-driven development, but I didn't create the automated test script until the end of the project; but, I did
# use the list of results, provided by the project's rubric, and my own set of calculations I did, outside of Python,
# to compare to the output of my code before I started to code the functions. As I was coding the functions, my first
# priority was to just create working functions and, afterwards, go back and simplify the code; following the principles
# of boolean zen, at least to the best of my abilities. An example of this would be, for the pctToNsc(parameter)
# function, I initially had the selection statement coded as "if parameter >= 0 and parameter <= 100" and afterwards I
# simplified it to "0 <= parameter <= 100". After finishing each function definition, I would run them through the,
# previously, stubbed main() function, before moving onto code the next function, and compare them to the results I
# had, from external sources. And I hadn't really gotten stuck, but I did spend a decent bit of time just looking at
# my code, in order to see if there was any chunk or line I could simplify; unfortunately, this lead me to start
# wondering, needlessly, if the empRating function should also accept floating-point values, between 1 and 10, because
# if so, I could shorten code like "parameter == 1 or parameter == 2" to "1 <= parameter <= 2".
#    Everything works as intended, due to the fact that the arguments aren't dependent on user input; i.e. a bad user
# won't try to force values that don't work. And even in the case of providing arguments that would provide errors,
# the program is coded in a way to provide an error output, instead of the program breaking. An example of this would
# be, outputting -9.9 for the pctToNsc function when an argument less than zero or more than one-hundred is provided.
#    The most important thing I learned from this project is the concept of writing simple and readable code. This
# applied to all of our previous projects, but this project really emphasized the possibility that there's a potentially
# cleaner way to write the exact same code; although, I would like to continue to practice this, as I'm still at a
# point where I'm not entirely confident that I wrote the code in the simplest way possible, without sacrificing
# readability and functionality. I'd like to continue to refine my ability to write clean code and apply what I'm
# already capable of doing, in regards to cleaning up code, to future projects. And, as far as doing things differently
# in the future, I'll definitely apply some of the logic towards writing simple code, that I picked up from this project
# , because I spent about 90% of my time on this project just thinking about how to simplify my code and 10% of the time
# actually coding; although, to be clear, I don't want to necessarily change this ratio, instead I want to increase
# efficiency when it comes to working on the project overall.


# TEST CASES

# empRating Function
# - Tested each of the valid numerical ratings to assure they output the appropriate ratingDescription.
#    - 1 and 2 output "Probation".
#    - 3 and 4 output "Needs Improvement".
#    - 5, 6, and 7 output "Acceptable".
#    - 8 and 9 output "Good".
#    - 10 outputs "Excellent".
# - Tested invalid arguments to ensure the output was "ERROR".
#    - Negative numbers, like -1, output "ERROR".
#    - Floating-point numbers, like 1.2, output "ERROR".
#       - This is intended, as the only valid data type is integer values.
#   - Strings, like "One", output "ERROR".

# pctToNsc Function
# - Tested values within the valid range, from 0 to and including 100.
#    - Boundary points
#       - 96 outputs 4.0.
#       - 95 outputs 3.9.
#       - 66 outputs 1.0.
#       - 65 outputs 0.0, as any grade less than 1.0 is automatically a 0.0.
#       - 97 to 100 outputs 4.0, as any result greater than 4.0 is converted back to a 4.0, the highest possible score.
#   - Odd percentages, like 88, produced a floating-point number with more than a single digit decimal; compensated
#     by formatting function call in main function, to always output a floating-point number with a single digit
#     decimal.
# - Tested values outside the valid range, less than 0 and greater than 100.
#    - Values less than 0, like -0.000001, output -9.9.
#    - Values greater than 100, like 100.000001, output -9.9.

# isDivisibleBy5or7or11 Function
# - Tested values that result in True.
#    - Values that are exclusively True to just one of the integers.
#       - 5, which is divisible by 5, but not 7 or 11, outputs True.
#    - Values that are True to two out of three of the integers.
#       - 35, which is divisible by 5 and 7, but not 11, outputs True.
#    - Values that are divisible by all three integers.
#       - 385, which is divisible by 5, 7, and 11, outputs True.
#    - 0 results in True.
#    - Negative values that are divisible by any of the three integers outputs True.
#       - -5 outputs True.
# - Tested values that would result in False.
#    - Values that are not divisible by any of the three integers.
#       - 1 results in False.
#       - All floating-point numbers, that have a decimal value greater than 0, result in False.
#           - 5.01 would result in False
#           - 5.0 would NOT result in False, it would output True.
# - Strings, such as "Five", result in a TypeError as you cannot divide a string by an integer.
# - Providing no argument or just a black space results in a TypeError, due to a missing argument.

# commission Function
# - empPosition Parameter
#    - Tested all four valid parameters, "Trainee", "Associate", "Lead", and "Manager".
#       - Each of the four valid parameters result in the use of the appropriate salesCommission equation.
#    - ALL other arguments being passed into the empPosition parameter will result in 0 salesCommission, which results
#      in 0 totalCommission.
#       - This includes integers, floating-point numbers, and strings that are not the four valid strings.
# - inStateSales and outOfStateSales Parameters
#    - Tested to ensure parameters were being passed correctly and properly used in salesCommission equation.
#    - All integer values are valid.
#       - Negative values are not logically valid, as you cannot lose money when making a sale; but, they will not break
#         the program.
#    - All Floating-point values are valid.
#       - Negative values are not logically valid, as you cannot lose money when making a sale; but, they will not break
#         the program.
#    - Strings will result in a TypeError if empPosition is passed a valid argument.
#       - String type arguments will result in 0 if empPosition's argument is not valid, because inStateSales and
#         outOfStateSales are only utilized if empPosition is one of the four valid strings.

# main Function
# - Tested with all function calls, with arguments, to ensure outputs were displaying properly.

# TestSelection.py
# - All expected results drawn from project 5's rubric or calculations done outside of Python.