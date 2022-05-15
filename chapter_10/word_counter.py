# -*- coding: utf-8 -*-
def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        #print(f"Sorry, the file {filename} does not exist.")
        pass
    else:
        words = contents.strip()
        num_words = len(words)
        print(f"The file {filename} has about {num_words}.")


filenames = ['Treasure Island.txt', 'The Jungle Book.txt',
             'moby_dick.txt', 'alice.txt']


for filename in filenames:
    count_words(filename)
