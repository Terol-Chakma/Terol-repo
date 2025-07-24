def are_anagram(str1,str2):
    return sorted(str1) == sorted(str2)
    
if __name__ == '__main__': 
    str1 = input("Enter the first string: ").replace("","").lower()
    str2 = input("Enter the second string: ").replace("","").lower()
    
    if(are_anagram(str1, str2)):
        print("These string are anagram to each other.")
    else:
        print("These string are not anagram to each other")