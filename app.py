continueGame = True

class Word():
    def __init__(self):
        self.chosen_word = "test"
        self.remaining_guesses = 8
        self.correct_guessed_letters = []
        

    def start(self):
        word = " "
        #append "_" for every letter in the chosen word
        for letter in self.chosen_word:
            self.correct_guessed_letters.append('_')
        
        #return a string of "_" for every _ in the guessed_letters li
        return "Here is your word", word.join(self.correct_guessed_letters)


    def guess(self, letter):
        letter_indexes = []
        self.remaining_guesses -= 1
        
        #iterate through chosen word
        for i, ltr in enumerate(self.chosen_word):
            if (ltr == letter): 
                letter_indexes.append(i)

        if(len(letter_indexes) > 0):
            self.update_correct_guessed_letters(letter_indexes, letter)
            print(f"Yes! You have {self.remaining_guesses} guesses left")
            self.game_over()
            return " ".join(self.correct_guessed_letters)
        else:
            self.game_over()
            return f"That is incorrect! You have {self.remaining_guesses} guesses left"
            


    def update_correct_guessed_letters(self, arr, letter):
        for letter_index in arr:
            self.correct_guessed_letters[letter_index] = letter


    def game_over(self):
        global continueGame
        if (("".join(self.correct_guessed_letters)) == self.chosen_word):
            print("You did it! You won!")
            continueGame = False
        if(self.remaining_guesses > 0):
            continueGame = True        
        elif(self.remaining_guesses == 0):
            print("You lost!")
            continueGame = False
            print(continueGame)

# word = Word()


# print(word.chosen_word)

# print(word.start())
word = Word()
print(word.start())
print("If you'd like to quit, press q")

while(continueGame):

    user_input = input().lower()
    
    if(user_input == "q"):
        print("bye!")
        break
    elif(len(user_input) > 1):
        print("Please enter one character")
        continue
    elif(type(user_input) != type(str())):
        print("Please type in a letter")
        continue
    else:
        print(word.guess(user_input))