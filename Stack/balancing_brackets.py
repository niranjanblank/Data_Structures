from Stack import Stack



def match_bracket(item, bracket):
    if bracket == ')' and item == '(':
        return True
    elif bracket == '}' and item == '{':
        return True
    elif bracket == ']' and item == '[':
        return True
    else:
        return False


def is_bracket_balanced(bracket_string):
    stack = Stack()
    for bracket in bracket_string:
        if stack.is_empty():
            stack.push(bracket)
        else:
            last_item = stack.peek()
            match = match_bracket(last_item, bracket)
            if match:
                stack.pop()
            else:
                stack.push(bracket)
    return stack.is_empty()


if __name__ == '__main__':
    string = input("Enter Bracket String: ")
    print(f'Entered String: {string}')
    if is_bracket_balanced(string):
        print('The String is balanced')
    else:
        print('The String isn\'t balanced')
