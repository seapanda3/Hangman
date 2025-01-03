import random


print(
    """
 _                                            
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     
    """
)

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

random_word = []

for word in random.choices(words):
    random_word.append(word)


random_word_letters = []

for word_letters in random_word[0]:
    random_word_letters.append(word_letters)
    
    
print(random_word_letters)



on_game = ["_"*len(random_word_letters)]
    

message = "Word to guess: "
print(message + "".join(map(str, on_game)))
user_guess = input("Guess the word: ")

# user_random_letter = []

# for user_letters in user_guess:
#     user_random_letter.append(user_letters)


# print(user_random_letter)


# print(random_word_letters == user_random_letter)


# for i in range(len(random_word_letters)):
if user_guess in random_word_letters:
        print("")
else:
    print(f"You guessed {user_guess}, that's not in the word. You lose a life.")
        
