from Stack import Stack

#function to reversing a string using stack
def reverse_string(value):
    value_stack = Stack()
    reversed_string = ''
    #adding all the characters of string in a stack
    for i in value:
        value_stack.push(i)
    #geting the characters from stack and appending the value of reversed_string
    for i in range(len(value)):
        reversed_string = reversed_string + value_stack.pop()

    return reversed_string

if __name__ == '__main__':
    string_value = input("Enter Any String: ")
    reversed_string = reverse_string(string_value)
    print(f'The reversed string is: {reversed_string}')