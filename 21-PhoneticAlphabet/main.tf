import pandas

# Create a dictionary in this format:
df_letters = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_code_dict = {row.letter:row.code for (index, row) in df_letters.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ")
phonetic_code_list = [letter_code_dict[letter.upper()] for letter in user_input]
print(phonetic_code_list)
