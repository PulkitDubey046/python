# Create a script to count vowels and consonants in a string

def countVowelAndConsonant(ch):
    if ch in 'aeiouAEIOU':
        return "Vowel"
    else:
        return "Consonant"

string = input("Enter a string: ")
vowel_count = 0
consonant_count = 0

for char in string:
    if char.isalpha():  # check only letters
        if countVowelAndConsonant(char) == "Vowel":
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
