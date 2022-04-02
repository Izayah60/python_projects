# 8 python Projects

1. Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.
For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4]

2. Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
For example, mid("abc") should return "b" and mid("aaaa") should return ""

3. Write a function named format_number that takes a non-negative number as its only parameter.
Your function should convert the number to a string and add commas as a thousands separator.
For example, calling format_number(1000000) should return "1,000,000".

4. Here's the backstory for this challenge: imagine you're writing a tic-tac-toe game, where the board looks like this:
 
1:  X | O | X
   -----------
2:    |   |  
   -----------
3:  O |   |

    A   B  C
The board is represented as a 2D list:
board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    ["O", " ", " "],
]
Imagine if your user enters "C1" and you need to see if there's an X or O in that cell on the board. To do so, you need to translate from the string "C1" to row 0 and column 2 so that you can check board[row][column].
Your task is to write a function that can translate from strings of length 2 to a tuple (row, column). Name your function get_row_col; it should take a single parameter which is a string of length 2 consisting of an uppercase letter and a digit.
For example, calling get_row_col("A3") should return the tuple (2, 0) because A3 corresponds to the row at index 2 and column at index 0 in the board

5. Define a function param_count that takes a variable number of parameters. The function should return the number of arguments it was called with.
For example, param_count() should return 0, while param_count(2, 3, 4) should return 3

6. Define a function named convert that takes a list of numbers as its only parameter and returns a list of each number converted to a string.
For example, the call convert([1, 2, 3]) should return ["1", "2", "3"].
What makes this tricky is that your function body must only contain a single line of code.

7. Write a program in  to produce Star triangle
8. Write a program in  to check if a number is prime
