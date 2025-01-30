acronyms = {'LOL', 'Laugh out loud',
            'IDK', "I don't know",
            'TBH', 'To be honest',
            }

try:
    defo = acronyms['BTW']
    print('Definition of', acronyms, 'is', defo)
except:
    print('exceptions')
finally:
    print('finally')

print ('out of try')