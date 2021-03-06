# Christopher Geier (cpg3rb)
import urllib.request


def clean(user_string_list):
    clean_list = []
    for words in user_string_list:
        clean_list.append(words.strip('.?!,()\"\''))
    return clean_list

correct_words = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/words.txt').read().decode('utf-8').split('\n')
print('Type text; enter a blank line to end.')
user_string = input()
while user_string != '':
    clean_input = clean(user_string.split())
    for word in clean_input:
        if word.lower() not in correct_words and word not in correct_words:
            print('  MISSPELLED: ' + word)
    user_string = input()
