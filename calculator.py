''' ---------------------------------------PROJECT-----------------------------
    ----------------------------------SMART CALCULATOR-------------------------'''

'''This is the program of Smart calculator.In this program,you simply ask the question like a human
   e.g. add 3 and 4 and this will give the output 7.'''
from mathy import * #import mathy module which we have define before.
print(responses[0])
print(responses[1])
while True:
    print()
    text=input("Enter some text")
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l=extract_numbers_from_text(text)
                r=operations[word.upper()](l[0],l[1])
                print(r)
            except:
                print("Something is wrong please retry")
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
    else:
        sorry()
'''This program will be continuously running until or unless user
   enter the text EXIT'''
"""-----------------------------------------THANK YOU-------------------------------"""
