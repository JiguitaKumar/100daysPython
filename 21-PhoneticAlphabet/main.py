import pandas

# Create a dictionary in this format:
df_letters = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_code_dict = {row.letter:row.code for (index, row) in df_letters.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
get_input = True
while get_input:
    user_input = input("Enter a word: ")
    try:
        phonetic_code_list = [letter_code_dict[letter.upper()] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(phonetic_code_list)
        get_input = False
