import keyword #provides list of all key keywords using keyword.kwlist

#Lexer function 
def lexer(input_string):
    #Turn input string into chars
    for i, char in enumerate(input_string):
        print('char', str(i + 1).rjust(3, ' '), ':', char)
    

#lists with diffrent tokken name and there symbols
Operators = ['+', '-', '*', '/','%', '**', '//', '=', '+=', '-=', '*=' ]
Seperators = []
identifer = []


#Test input string 
input_string = 'while (t < lower) r = 28.00;'
lexer(input_string)

