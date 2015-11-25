class MySuperString:
    def __init__(self, mystring):
        self.mystring = mystring

    def reverse(self):
        stringlength = len(self.mystring)
        myreversedstring = ''
        for i in range(stringlength-1, -1, -1):
            myreversedstring += self.mystring[i]
        return myreversedstring

    def character_counter(self, mycharacter):
        charcount = 0
        for i in self.mystring:
            if i == mycharacter:
                charcount += 1
        return charcount

    def space_to_underscore(self):
        underscorestring = ''
        for i in self.mystring:
            if i == ' ':
                underscorestring += '_'
            else:
                underscorestring += i
        return underscorestring

    def average_calculator (self, mynumberlist):
        sum_of_my_numbers = 0
        for n in mynumberlist:
            sum_of_my_numbers += n

        return sum_of_my_numbers / len(mynumberlist)

x = MySuperString("I know the pieces fit 'cause I watched them fall away")

print(x.reverse())
print(x.character_counter('e'))
print(x.space_to_underscore())
print(x.average_calculator([45, 32, 49, 6]))
