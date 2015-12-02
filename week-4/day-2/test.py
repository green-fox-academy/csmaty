from reverse import reverse_list
import os

print(reverse_list([3, 4, 5]))
print(os.getpid())
print(os.getcwd())



alma_file = open('alma.txt', 'w')
#print(alma_file.read()) write tipussal van megnyitva - nem lehet olvasni
alma_file.write('Csubakka')
alma_file.close()

alma_file = open('alma.txt')
print(alma_file.read())
alma_file.close()
