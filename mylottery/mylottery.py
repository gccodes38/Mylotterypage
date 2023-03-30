import random


def yourname_password_gen():

# Generate a random lottery number
    name = input("Enter user's name: ")
    lucky_numbercode = int(input("input your lucky number: "))
    rand_number = random.randint(1, 50)
    print(rand_number)
    # winninglottery_num = "20"
    for x in range(1):
        if rand_number == 20:
            print("congratulations", name, "your lottery number is 30, you are the lucky winner")
        else:
            print("sorry", name, "check some other time")


yourname_password_gen()