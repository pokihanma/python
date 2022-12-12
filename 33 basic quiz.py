#-----------------
def new_game():
    
    guesses = []
    correct_guess = 0
    question_num = 1
    
    
    
    for key in questions:
        
        print(key)
        print("-----------------")
        for i in options[question_num-1]:
            print(i)
        guess = input("enter (A,B,C,D): ").upper()
        guesses.append(guess)
        correct_guess+= check_ans(questions.get(key),guess)

        question_num +=1
        
    display_score(correct_guess,guesses)    
#-----------------
def check_ans(answer,guess):
    if answer == guess:
        print("correct")
        return 1
    else:
        print("you dumb ")
         
#-----------------
def display_score(correct_guesses,guesses):
    print("--------------------------------")
    print("results")
    print("--------------------------------")
    print("Answers: ",end="")
    for i in  questions:
        print(questions.get(i),end="")
    print()
    
    print("guesses: ",end="")
    for i in  guesses:
        print(i,end="")
    print()   
#-----------------
def play_again():
    pass
#------------------
questions = {
    "who created python" : "A",
    "python is tributed hich company group": "B",
    "What year the pyhton is developed ": "B",
    "which language is very easy syntex" : "A"
}
options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. python","B. java", "C. C", "D. c++"]]
new_game()
