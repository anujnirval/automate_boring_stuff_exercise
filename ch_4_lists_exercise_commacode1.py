spam = ['Apple','Mango','Grapes','Lemon']
def commacode(listvalue):
    if len(listvalue) == 1:
        return listvalue[0]
    return '{}, and {}'.format(', '.join(listvalue[:-1]),listvalue[-1])

print(commacode(spam))                
