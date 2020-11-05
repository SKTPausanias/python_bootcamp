#!/usr/bin/python

import string


def text_analyzer(*s):
    '''This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text.'''
    argcount = len(s)
    if argcount == 0:
        print("Where is the text to analyse?")
    elif argcount > 1:
        print("ERROR")
    else:
        for elem in s:
            total = 0
            count1 = 0
            count2 = 0
            countspace = 0
            countpunct = 0
            for c in elem:
                total += 1
                if c.isupper():
                    count1 += 1
                elif c.islower():
                    count2 += 1
                elif c == ' ':
                    countspace += 1
                elif c in string.punctuation:
                    countpunct += 1
            print("The text contains", total, "characters:")
            print("-", count1, "upper letters")
            print("-", count2, "lower letters")
            print("-", countpunct, "punctuation marks")
            print("-", countspace, "spaces")
