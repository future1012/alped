from name_function import get_formatted_name

print('Enter q at any time to quit')
while True:
   first = input('plz input your first name: ')
   if first == 'q':
      break
   last = input('\n plz input your last name: ')
   if last == 'q':
      break

   formatted_name = get_formatted_name(first,last)
   print('\t Neatly formatted name: ' + formatted_name)
