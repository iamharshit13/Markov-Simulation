import time
import random

vowel_to_vowel_probability = 13
consonant_to_consonant_probability = 33
vowel_to_consonant_probability = 100 - vowel_to_vowel_probability
consonant_to_vowel_probability = 100 - consonant_to_consonant_probability


total_vowel_count = 0
total_consonant_count = 0

counter = 0

current_character = "vowel"
while True:
    random_number = random.randint(1, 100)

    if current_character == "vowel":
        if random_number <= vowel_to_vowel_probability:
            current_character = "vowel"
        else:
            current_character = "consonant"
    else:
        if random_number <= consonant_to_consonant_probability:
            current_character = "consonant"
        else:
            current_character = "vowel"
    
    if current_character == "vowel":
        total_vowel_count += 1

    else:
        total_consonant_count += 1
    total_vowel_percentage = (total_vowel_count / (total_vowel_count + total_consonant_count)) * 100
    total_consonant_percentage = (total_consonant_count / (total_vowel_count + total_consonant_count)) * 100

    if counter % 25 == 0:
        print(f"Vowels: {total_vowel_count} ({total_vowel_percentage:.2f}%) | Consonants: {total_consonant_count} ({total_consonant_percentage:.2f}%)")
        time.sleep(2) 

    counter += 1

