"""Basic lexer for C++ source code written in Python"""
import sys

operators_list = [
    '=', '>', '<', '==', '>=', '<=', '!=', '&&', '||', '!', '&', '|', '^', '~', '<<', '>>', '+', '-', '*', '/',
    '%', '++', '--', '+=', '-=', '*=', '/=', '%=', '&=', '|=', '^=', '<<=', '>>=', '->*', '.*', '?', ':', 'sizeof',
    'typeid', 'new', 'delete', 'new[]', 'delete[]'
]
separators_list = [
    ';', ':', ',', '.', '...', '->', '(', ')', '[', ']', '{', '}', '<', '>'
]
keywords_list = [
    'alignas', 'alignof', 'and', 'and_eq', 'asm', 'atomic_cancel', 'atomic_commit', 'atomic_noexcept',
    'auto', 'bitand', 'bitor', 'bool', 'break', 'case', 'catch', 'char', 'char8_t', 'char16_t', 'char32_t',
    'class', 'compl', 'concept', 'const', 'consteval', 'constexpr', 'const_cast', 'continue', 'co_await',
    'co_return', 'co_yield', 'decltype', 'default', 'delete', 'do', 'double', 'dynamic_cast', 'else',
    'enum', 'explicit', 'export', 'extern', 'false', 'float', 'for', 'friend', 'goto', 'if', 'inline',
    'int', 'long', 'mutable', 'namespace', 'new', 'noexcept', 'not', 'not_eq', 'nullptr', 'operator',
    'or', 'or_eq', 'private', 'protected', 'public', 'reflexpr', 'register', 'reinterpret_cast', 'requires',
    'return', 'short', 'signed', 'sizeof', 'static', 'static_assert', 'static_cast', 'struct', 'switch',
    'synchronized', 'template', 'this', 'thread_local', 'throw', 'true', 'try', 'typedef', 'typeid',
    'typename', 'union', 'unsigned', 'using', 'virtual', 'void', 'volatile', 'wchar_t', 'while',
    'xor', 'xor_eq'
]


def lexer(input_string, pos):
    """Lexer function, returns token, lexeme, and position"""
    working_str = ""
    while pos < len(input_string):
        if input_string[pos].isalpha():
            while input_string[pos].isalpha() or input_string[pos].isdigit():
                working_str += input_string[pos]
                pos += 1
            if working_str in keywords_list:
                return "keyword", working_str, pos
            return "identifier", working_str, pos
        if input_string[pos] in separators_list:
            return "seperator", input_string[pos], pos + 1
        if input_string[pos] in operators_list:
            return "operator", input_string[pos], pos + 1
        if input_string[pos].isdigit():
            while input_string[pos].isdigit():
                working_str += input_string[pos]
                pos += 1
            if input_string[pos] == ".":
                working_str += input_string[pos]
                pos += 1
                while input_string[pos].isdigit():
                    working_str += input_string[pos]
                    pos += 1
                return "real", working_str, pos
            return "integer", working_str, pos
        return None, None, pos + 1
    return None, None, pos


def open_file(file_name):
    """Open file and return file object"""
    try:
        with open(file_name, "r", encoding="UTF-8") as file_object:
            return file_object.read()
    except IOError:
        print("Cannot open", file_name)
        sys.exit()



def main():
    """Main function"""
    source_code = open_file("input_scode.txt")
    
    original_stdout = sys.stdout
    with open('output.txt', 'w') as f:
        sys.stdout = f
        print(f"{'Token':<10}\tLexeme")
        position = 0
        while position < len(source_code):
            token, lexeme, position = lexer(source_code, position)
            if token is not None:
                print(f"{token:<10}\t{lexeme}")
        sys.stdout = original_stdout
            
    


if __name__ == "__main__":
    main()
