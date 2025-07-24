def is_pangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return set(s.lower()) >= alphabet

if __name__ == '__main__':
    s = input("Enter the sentence: ")
    if (is_pangram(s)):
        print("The sentence is pangram.")
    else:
        print("The sentence is not pangram. ")