#######################
# Test Processing I   #
#######################


def normalize(input_string):
    
    normalized_string = " ".join(input_string.lower().split()).strip()
    return normalized_string 



def no_vowels(input_string):

    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    for vowel in vowels:
        if vowel in input_string:
            input_string = input_string.replace(vowel, "")
        
    no_vowel_string = input_string
    return no_vowel_string

input_string1 = "     I Love   You."

result1 = normalize(input_string1)
print(result1)

result2 = no_vowels(input_string1)
print(result2)

string_list = string_list.upper() # Time Complexity가 증가하게 됨.
vowel_set = ["A", "E", "I", "O", "U"]