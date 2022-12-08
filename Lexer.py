# Contains TokenType, Token, and Lexer classes for the parser calculator

from dataclasses import dataclass

# Token types auto() is a function that automatically assigns a value to each token type

from enum import Enum, auto


class TokenType(Enum):
    INTEGER = auto()
    PLUS = auto()
    MINUS = auto()
    MUL = auto()
    DIV = auto()
    EXP = auto()
    LPAREN = auto()
    RPAREN = auto()
    EOF = auto()


# Token class is used to store the token type and the value of the token type
# dataclass

@dataclass
class Token:
    type: TokenType
    value: any

    def __repr__(self):
        return f'{self.type}:{self.value}'


# Lexer Class that uses the Token Class and includes the method Tokenizer() that returns a list of tokens

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if len(text) > 0 else None
        self.Tokens = []

    def Scanner(self):
        # Lexical analyzer (also known as scanner or tokenizer)
        while self.current_char is not None:  # While there is still input to be consumed
            if self.current_char.isspace():
                self.skipWhiteSpace()
                continue
            if self.current_char.isdigit():
                return Token(TokenType.INTEGER, self.integer())
            if self.current_char == '+':
                self.advance()
                return Token(TokenType.PLUS, '+')
            if self.current_char == '-':
                self.advance()
                return Token(TokenType.MINUS, '-')
            if self.current_char == '*':
                self.advance()
                return Token(TokenType.MUL, '*')
            if self.current_char == '/':
                self.advance()
                return Token(TokenType.DIV, '/')
            if self.current_char == '^':
                self.advance()
                return Token(TokenType.EXP, '^')
            if self.current_char == '(':
                self.advance()
                return Token(TokenType.LPAREN, '(')
            if self.current_char == ')':
                self.advance()
                return Token(TokenType.RPAREN, ')')
            self.error()

        return Token(TokenType.EOF, None)

    def advance(self):
        # Advance the 'pos' pointer and set the 'current_char' variable
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def Tokenizer(self):
        # Tokenizer method that returns a list of tokens
        while True:
            token = self.Scanner()
            self.Tokens.append(token)
            if token.type == TokenType.EOF:
                break

            # Edge cases for multiple operators
            self.opEdgeCases(self.Tokens, token)

        return self.Tokens

    def error(self):
        raise Exception('Error parsing input')

    def skipWhiteSpace(self):
        # Skip whitespace
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        # Return a (multidigit) integer consumed from the input
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    # Defines logic for multiple mathematical operators like minus or plus happening right after each other
    @staticmethod
    def opEdgeCases(tokens, token):  # tokens is the list of tokens, token is the current token
        """
        Defines logic for multiple mathematical operators like minus or plus happening right after each other
        :param tokens:
        :param token:
        :return:
        """
        # double minus equals plus
        if tokens[-1].type == TokenType.MINUS and tokens[-2].type == TokenType.MINUS:
            tokens.remove(token)
            tokens[-1].type = TokenType.PLUS
            tokens[-1].value = '+'

        # double plus equals just one plus
        elif tokens[-1].type == TokenType.PLUS and tokens[-2].type == TokenType.PLUS:
            tokens.remove(token)

        # minus plus equals minus
        elif tokens[-1].type == TokenType.MINUS and tokens[-2].type == TokenType.PLUS:
            tokens.remove(token)
            tokens[-1].type = TokenType.MINUS
            tokens[-1].value = '-'

        # minus plus equals minus
        elif tokens[-1].type == TokenType.PLUS and tokens[-2].type == TokenType.MINUS:
            tokens.remove(token)
            tokens[-1].type = TokenType.MINUS
            tokens[-1].value = '-'


# Test the tokenizer with user input
def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        tokenizer = Lexer(text)
        tokens = tokenizer.Tokenizer()
        print(tokens)


if __name__ == '__main__':
    main()
