# LetterE.py - This program prints the letter E with 3 asterisks
# across and 5 asterisks down. 
# Input:  None
# Output: Prints the letter E.

NUM_ACROSS = 3 # Number of asterisks to print across
NUM_DOWN = 5 # Number of asterisks to print down

# Write a loop to control the number of rows.
while NUM_DOWN >= 0:
    # Write a loop to control the number of columns
    while NUM_ACROSS >= 0:
        # Decide when to print an asterisk in every column.
        if NUM_ACROSS == 3:
            print("*")
        # Decide when to print asterisk in column 1.   
        elif NUM_ACROSS == 2:
            print("*")
        # Decide when to print a space instead of an asterisk.   
        elif NUM_ACROSS == 1:
            print(" ")
        # Figure out where to place this statement that prints a newline.
        NUM_ACROSS = NUM_ACROSS - 1
        print("\n")
    NUM_DOWN = NUM_DOWN - 1
    NUM_ACROSS = 3
