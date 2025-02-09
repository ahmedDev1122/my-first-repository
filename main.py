print("""
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
""")
print("welcome to my island")
print("there are two doors in front of you a red door and a blue door ")
door_choice=input("which door do you want to open ").lower()
if door_choice == "red":
    print("great now you entered the room")
    print("you found three boxes white , black and green ")
    box_choice=input("which box do you open").lower()
    if box_choice == "white":
        print("oops ! you opened a box filled with snakes")
    elif box_choice == "green":
        print("congreatulations you found the treasure")    
    elif box_choice == "black":
        print("oops! you opened a box which is filled whit spiders")
    else:
        print("please invalid a choice")
elif door_choice =="blue":
    print("oops! you choose the crocodile door ")
    print("game over")
else:
    print("invalid a choice")
