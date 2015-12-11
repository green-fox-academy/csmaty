
class DuplicateEncode():
    def __init__(self, text):
        self.text = text

    def duplicate_encode(self):
        self.text

        output = {}
        for i in self.text.lower():
            if i not in output:
                output[i] = 1
            else:
                output[i] += 1
        finalstring = ''
        for i in self.text.lower():
            if output[i] == 1:
                finalstring += '('
            else:
                finalstring += ')'

        return finalstring
