#------------------------------------------------------------
def new_game():
    number_quest = 1
    score = 0
    guesses = []
    for key in questions:
        print(key)
        for i in answer[number_quest-1]:
            print(i)
        print("------------------------------")
        guess = input("Choose A,B,C: ")
        guess = guess.upper()
        guesses.append(guess)

        score += check_answer(questions.get(key), guess)
        number_quest += 1

    display_score(score, guesses)
    pass
#------------------------------------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("Wrong")
        return 0
    pass
#------------------------------------------------------------
def display_score(correct_answer, guesses):
    print('------------------------------------------------------------')
    print("Results")
    print('------------------------------------------------------------')
    print("Answers: ",end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i,end=" ")  
    print()
    print((correct_answer)/len(questions)*100)
    pass

#------------------------------------------------------------
def play_again():
    response = input("Do you wanna play again? (yes/no): ")
    response.lower()
    if response == "yes":
        return True
    else:
        return False
    pass


questions = {"Ai la bo m":"A", "Ai dep trai nhat?: ":"B", "Day la nam bao nhieu":"C"}
answer  = [["A. TAO     B. Thang kia    C. No one"], ["A. Khong phai tao    B. La tao   C.Thang kia"],
           ["A.2022     B.2023      C.2024"]]


new_game()
while play_again():
    new_game()
print("Game over")
