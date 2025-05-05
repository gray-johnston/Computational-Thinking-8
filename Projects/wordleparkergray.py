
import random
import nltk
from nltk.corpus import words

# Make sure you have the word list
nltk.download('words')

# Get the list of words
word_list = words.words()

# Filter for 5-letter alphabetic words
five_letter_words = [word.lower() for word in word_list if len(word) == 5 and word.isalpha()]
# Pick a word at random
word_listold = ["nymph","aglet","anode","ouija","leche","floog","Moist","gnome","aping","apple", "brave", "crane", "dodge", "eagle", "flame", "grape", "hound", "inlet", "jolly",
"kneel", "latch", "mirth", "noble", "orbit", "piano", "queen", "risky", "sheep", "trick",
"urban", "vigor", "wrist", "xerox", "yacht", "zesty", "align", "blush", "cabin", "dealt",
"envoy", "fable", "gleam", "hoist", "ideal", "jumps", "karma", "lemon", "magic", "nerdy",
"ocean", "punch", "quilt", "rouge", "sassy", "tulip", "uncle", "vivid", "woven", "xenon",
"yodel", "zebra", "angle", "blaze", "cliff", "drain", "event", "froze", "grind", "hatch",
"ivory", "joint", "knife", "lunar", "mocha", "novel", "oxide", "plaza", "quack", "raven",
"spike", "trend", "ultra", "verge", "waltz", "xylem", "yours", "zonal", "amber", "blond",
"candy", "dizzy", "elite", "frost", "gloom", "haste", "input", "jelly", "koala", "leech",
"mince", "naive", "occur", "pride", "quest", "rider", "siren", "tiger", "usher", "vapor",]
hidden_word = random.choice(five_letter_words)
print(hidden_word)
# Repeat for 6 guesses
for i in range(6):
    # Guess a word
    guess_word = input()
    output = ""

    # First letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

        # First letter (in python, counting starts at 0 not 1)
    if guess_word[1] == hidden_word[1]:
        output += "🟩"
    elif guess_word[1] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"


        # First letter (in python, counting starts at 0 not 1)
    if guess_word[2] == hidden_word[2]:
        output += "🟩"
    elif guess_word[2] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

        # First letter (in python, counting starts at 0 not 1)
    if guess_word[3] == hidden_word[3]:
        output += "🟩"
    elif guess_word[3] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

        # First letter (in python, counting starts at 0 not 1)
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    

    # Result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You win")
        break

print(f"You used {i+1} guesses")
