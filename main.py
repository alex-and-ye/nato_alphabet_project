import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
word = input("Enter your name: ").upper()
phonetic_code_l = [nato_dict[letter] for letter in word]
print(phonetic_code_l)
