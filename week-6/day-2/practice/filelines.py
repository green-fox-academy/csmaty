class FileLines():
    def __init__(self, text):
        self.text = text
        input_file = open(self.text)
        self.lines = input_file.readlines()


    def get_last(self):
        print(self.lines[-1])


    def get_first(self):
        print(self.lines[0])


    def nth_line(self, n):
        input_file = open(self.text)
        lines = input_file.readlines()
        linecount = 0
        charcount = 0
        for line in lines:
            linecount += 1
            if linecount == n:
                print(line)



lines = FileLines('alma.txt')

lines.get_last()
lines.get_first()
lines.nth_line(3)
