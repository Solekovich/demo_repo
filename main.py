import random


def create_number(_start_range_, _end_range_):
    user_number = int(input("Write your number: "))
    hidden_number = random.randint(start_range, end_range)
    while user_number != hidden_number:
        if user_number > hidden_number:
            user_number = int(input("Try lower: "))
        if user_number < hidden_number:
            user_number = int(input("Try higher: "))
    print("Congrats, you're right!!!")


start_range = int(input("Start of the range: "))
end_range = int(input("End of the range: "))
create_number(start_range, end_range)
