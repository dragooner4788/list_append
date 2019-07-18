my_list = []

help_message = 'Welcome to Word Length app. Type: !show to show the list you have create !help to bring up the help menu, !stop to stop the application.\n'

print(help_message)

word_input = ''

while word_input != '!stop':
    word_input = input('Please enter a word: ')
    my_list.append(word_input)
    if word_input == '!stop':
        print('Thanks for playing!')
    elif word_input == '!show':
        my_list.pop(-1)
        print(my_list)
    elif word_input == '!help':
        my_list.pop(-1)
        print(help_message)
    else:
        print(len(word_input))