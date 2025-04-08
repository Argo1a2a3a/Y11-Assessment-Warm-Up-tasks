
# Input a number from the user and print the square of the number in a message
number = int(input("Enter a number: "))
number2 = number**2
print(f'The square of {number} is {number2}.')

# input a word and blank out all letters that are not vowels with '='
word = input("Please enter a word: ")
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O' 'U'}
result = ''.join([char if char in vowels else '=' for char in word])
print(result)

# Create a list of words - go through the list and sum the total number of characters in all words
words = ["i", "like", "trains"]
total_characters = 0
for word in words:
    total_characters += len(word)
print(f'{total_characters} characters.')


# Create a list of words - count the total number of DIFFERENT characters in all the words
words = ["i", "like", "trains"]
unique_characters = set()
for word in words:
    for char in word:
        unique_characters.add(char.lower())
total_unique_characters = len(unique_characters)
print(f"The total number of different characters is: {total_unique_characters}")


# Sum the values in a 3 x 3 2D list of numbers
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
total_sum = 0
for row in numbers:
    for value in row:
        total_sum += value
print(f"The total sum of the values in the 2D list is: {total_sum}")


# Write a function to return if a letter is a vowel or not
def is_vowel(letter):
    """Check if the given letter is a vowel."""
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O' 'U'}  
    if letter in vowels:
        return True
    else:
        return False
letter = input("Enter a single letter: ")
if is_vowel(letter):
    print(f"'{letter}' is a vowel.")
else:
    print(f"'{letter}' is not a vowel.")


# Start with a list of words.  Create a dictionary to count how many words are of each length. 
words = ["i", "like", "trains"]
word_length_counts = {}
for word in words:
    length = len(word)  
    if length in word_length_counts:
        word_length_counts[length] += 1  
    else:
        word_length_counts[length] = 1  
print(f"Word lengths and their counts: {word_length_counts}")

