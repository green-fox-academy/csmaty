def palindrome_creator(myword):
    palindrome_word = myword
    wordlength = len(myword)
    for i in range(wordlength-1, -1, -1):
        palindrome_word += myword[i]
    return palindrome_word

print(palindrome_creator(str(input("Give me a word I can make a palindrome of: \n\n"))))
