x = 2
y = 2


name = input("type your name: ")
print("hello " + name + " welcome to my game")

should_we_play = input("do you want to play? ").lower()
should_we_play == "yes"

if should_we_play == "yes" or should_we_play == "y":
    print("we are gonna play")

direction = input("do you want to go left or right>?").lower()
            

else:
    print("we are not playing")
