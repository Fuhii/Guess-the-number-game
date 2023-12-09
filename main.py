import sys
import random


def get_int_input(prompt):
    while True:
        sys.stdout.buffer.write(prompt)
        sys.stdout.flush()
        input_str = sys.stdin.buffer.readline().decode().strip()
        if input_str.isdigit():
            return int(input_str)
        else:
            print("Invalid input. Please enter a number.")

max_num = get_int_input(b"please enter the maximum value: ")
min_num = get_int_input(b"please enter the minimum value: ")


def gess_game(max_num, min_num):
    try:
        if max_num < min_num:
            raise Exception("the maximum value is less than the minimum value")
        if max_num == min_num:
            raise Exception("Both values are same")
    except Exception as e:
        print(str(e))
        return
    ran_num = random.randint(min_num, max_num)

    while True: 
        gess_num = get_int_input(b"What is the number you are guessing?: ")
        if min_num > gess_num or max_num < gess_num:
            print("The number you are guessing is out of range.")
        elif gess_num != ran_num:
            print("That is not correct")
        else:
            print("Congratulations! You guessed the number correctly.")
            break 

gess_game(max_num, min_num)


