import re

input_string  = input("Enter the string to remove whiespaces:\n")

rightSpace = re.compile(r'\s+$')
leftSpace = re.compile(r'^\s+')

def space_Check(statement):
    if rightSpace.search(statement):
        leftStrip = rightSpace.sub('',statement)
        if leftSpace.search(leftStrip):
            return leftSpace.sub('',leftStrip)
        else:
            return leftStrip
    elif leftSpace.search(statement):
        rightStrip = leftSpace.sub('',statement)
        if rightSpace.search(rightStrip):
            return rightSpace.sub('',rightStrip)
        else:
            return rightStrip
    else:
        return "No Space"

print("Old string is:" + input_string + " and length is: " + str(len(input_string)))

print("New string is:" + str(space_Check(input_string)) + " and length is: " + str(len(str(space_Check(input_string)))))
