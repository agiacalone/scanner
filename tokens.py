class tokens:
    def gettoken(token):
    
        if token == '`':
            current_read = 0

        elif token == '<':
            current_read = 1

        elif token == '>':
            current_read = 2

        elif token == '[':
            current_read = 3

        elif token == ']':
            current_read = 4

        elif token == '{':
            current_read = 5

        elif token == '}':
            current_read = 6

        elif token == '@':
            current_read = 7

        elif token == '&':
            current_read = 8

        elif token == '#':
            current_read = 9

        elif token == '!':
            current_read = 10
            
        elif token == '~':
            current_read = 11

        elif token == "'":
            current_read = 12

        elif token == '$':
            current_read = 13

        elif token == ':':
            current_read = 14

        elif token == ';':
            current_read = 15

        elif token == '.':
            current_read = 16

        elif token == ',':
            current_read = 17

        elif token == '+':
            current_read = 18

        elif token == '-':
            current_read = 19

        elif token == '/':
            current_read = 20

        elif token == '\\':
            current_read = 21

        elif token == '*':
            current_read = 22

        elif token == '=':
            current_read = 23

        elif token == '^':
            current_read = 24

        elif token == '(':
            current_read = 25

        elif token == ')':
            current_read = 26
            
        elif token.isalpha():
            current_read = 27
            
        elif token.isdigit():
            current_read = 28            
            
        elif token == '"':
            current_read = 29         

        elif token == ' ':
            current_read = 30
            
        elif token == "_":
            current_read = 31

        elif token == '\n':
            current_read = 32

        else: current_read = 33
        
        return current_read
