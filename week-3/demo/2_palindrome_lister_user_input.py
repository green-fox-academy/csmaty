def give_all_palindromes(mystring):
    mystring = mystring.lower()
    stripped_string = strip_string(mystring)
    my_list = stripped_string.split(' ')
    palindrome_list = []

    for myword in my_list:
        length = len(myword)
        for i in range(length-1):
            for j in range(i,length):
                textpart = myword[i:j+1]
                if palindrome_decider(textpart):
                    palindrome_list.append(textpart)

    if len(palindrome_list) == 0:
        return '\n \n Sorry, I got no palindromes for you'
    else:
        return set(palindrome_list)

def palindrome_decider(textpart):
    return len(textpart) > 2 and textpart == text_reverser(textpart)


def text_reverser(textpart):
    reversed_part = ''
    textlength = len(textpart)
    for i in range(textlength-1, -1, -1):
        reversed_part += textpart[i]
    return reversed_part

def strip_string(mystring):
    stripped_string = ''
    characters_to_keep = " abcdefghijklmnopqrstuvwxyz"
    for caharacter in mystring:
        if caharacter in characters_to_keep:
            stripped_string += caharacter
    return(stripped_string)

print(give_all_palindromes(str(input('Give me a text to analyse: \n\n'))))
