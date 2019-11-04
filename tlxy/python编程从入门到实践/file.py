with open('pi_digits.txt') as  file_object:
    # contents = file_object.read()
    # print(contents.lstrip())
    lines = file_object.readlines()

pi_strings = ''

for line in lines:
    pi_strings += line.strip()

print(pi_strings)


with open('write_file.txt', 'w') as write_file:
    write_file.write('ssssssssssssssssss\n')
    write_file.write('ssssssssssssssssss\n')
    write_file.write('ssssssssssssssssss\n')


