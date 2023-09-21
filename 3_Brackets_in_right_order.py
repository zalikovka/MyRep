def checkio(expression):
    starting=["(","[","{"]
    ending=[")","]","}"]
    bracket_stack=''
    for i in range(0,len(expression)):
        if expression[i] in starting:
            bracket_stack+=expression[i]
        elif expression[i] in ending:
            if bracket_stack=='':
                return False
            elif starting[ending.index(expression[i])]==bracket_stack[-1]:
                bracket_stack = bracket_stack[:-1]
            else:
                return False
        else:
            continue
    return bracket_stack == ''



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
