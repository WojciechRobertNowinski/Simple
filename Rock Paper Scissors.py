print("Hello, we are playing Rock Paper Scissors. For start press enter.")
input("")
print("...rock...")
print("...paper...")
print("...scissors...")

choice1 = input("enter Player 1's choice: ")
print("=== No cheating! \n\n " * 10)
choice2 = input("enter Player 2's choice: ")

if choice1 == "rock" and choice2 == "paper":
    print("Player 2 wins!")
elif choice1 == "rock" and choice2 == "scissors":
    print("Player 1 wins!")
elif choice1 == "paper" and choice2 == "rock":
    print("Player 1 wins!")
elif choice1 == "paper" and choice2 == "scissors":
    print("Player 2 wins!")
elif choice1 == "scissors" and choice2 == "rock":
    print("Player 2 wins!")
elif choice1 == "scissors" and choice2 == "paper":
    print("Player 1 wins!")
elif choice1 == choice2:
    print("Draw!")
else:
    print("Something went wrong, wanna try again?")



                                                  # another approach

# if choice1 == choice2:
#     print("It's a draw!")
# elif choice1 == "rock":
#     if choice2 == "paper":
#         print("Player 2 wins!")
#     elif choice2 == "scissors":
#         print("Player 1 wins!")
# elif choice1 == "paper":
#     if choice2 == "rock":
#         print("Player 1 wins")
#     elif choice2 == "scissors":
#         print("Player 2 wins!")
# elif choice1 == "scissors":
#     if choice2 == "paper":
#         print("Player 1 wins!")
#     elif choice2 == "rock":
#         print("Player 2 wins!")
# else:
#     print("Something went wrong, wanna try again?")
