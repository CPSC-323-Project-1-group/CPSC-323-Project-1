import keyword #provides list of all key keywords using keyword.kwlist

#Lexer function 
def lexer(input_string):
    #create temp string
    tempStr=""
    
    #Turn input string into chars
    
    for i, char in enumerate(input_string):

        if (tempStr+char) in Keywords:
            #keyword
            print("keyword: "+tempStr+char)
            tempStr=""
        elif char in Seperators:
            #seperator
            print("seperator: "+char)
        elif char in Operators:
            #operator
            print("operator: "+char)
        elif input_string[i+1].isalpha()==False and input_string[i+1].isdigit()==False and input_string[i+1] != '.' and char != ' ':
            # real and identifier
            if (char).isdigit():
                print("real: "+tempStr+char)
            else:
                print("identifier: "+tempStr+char)
            tempStr=""
        elif char != ' ':
            #add to end of string
            tempStr=tempStr+char
        
       # print('char', str(i + 1).rjust(3, ' '), ':', char)
    

#lists with diffrent tokken name and there symbols
Operators = ['+', '-', '*', '/','%', '**', '//', '=', '+=', '-=', '*=','<','>' ]
Seperators = ['(',')',';']
Keywords = ["while","if"]
identifer = []


#Test input string 
input_string = 'while (t < lower) r = 28.00;'
lexer(input_string)

