import pyperclip

text = pyperclip.paste()
# print(text)

lines_list = text.split('\n')
print(type(lines_list))
for i in range(len(lines_list)):
    lines_list[i] = '* ' + lines_list[i]
    print(lines_list[i])
print(lines_list)
new_lines = '\n'.join(lines_list)

pyperclip.copy(new_lines)
