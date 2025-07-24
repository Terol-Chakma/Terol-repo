def rearrange_vowel(str):
    vowels = "aeiouAEIOU"
    vowel = ""
    consonant = ""
    for ch in str:
        if ch.isalpha():
            if ch in vowels:
                vowel += ch
            else:
                consonant += ch
    return vowel + consonant
        
if __name__ == '__main__': 
    str = input("Enter the string: ")
    output = rearrange_vowel(str)
    print(output)