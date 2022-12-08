from dataclasses import dataclass
from enum import Enum, auto


# Contains TokenType, Token, and Lexer classes for the parser calculator


class TokenType(Enum):
    """auto() is a function that automatically assigns a value to each token type"""
    INTEGER = auto()
    PLUS = auto()
    MINUS = auto()
    MUL = auto()
    DIV = auto()
    EXP = auto()
    LPAREN = auto()
    RPAREN = auto()
    EOF = auto()


@dataclass  # dataclasses is a decorator that allows you to create a class that has a constructor and other methods
class Token:
    """Token class is used to store both the type of the token and the tokens value"""
    type: TokenType  # type of token
    value: any  # value of token

    def __repr__(self):
        """Returns the token type and the value of the token type"""
        return f'{self.type}:{self.value}'


class Lexer:
    """Lexer Class that uses the Token Class and includes the method Tokenizer() that returns a list of tokens"""
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if len(text) > 0 else None
        self.Tokens = []

    def Scanner(self):
        # The scanner method is responsible for breaking a sentence apart into tokens. One token at a time.
        while self.current_char is not None:  # While there is still input to be consumed
            if self.current_char.isspace():
                self.skipWhiteSpace()
                continue

            elif self.current_char.isdigit():
                return Token(TokenType.INTEGER, self.integer())

            elif self.current_char == '+':
                self.advance()
                return Token(TokenType.PLUS, '+')

            elif self.current_char == '-':
                self.advance()
                return Token(TokenType.MINUS, '-')

            elif self.current_char == '*':
                self.advance()
                return Token(TokenType.MUL, '*')

            elif self.current_char == '/':
                self.advance()
                return Token(TokenType.DIV, '/')

            elif self.current_char == '^':
                self.advance()
                return Token(TokenType.EXP, '^')

            elif self.current_char == '(':
                self.advance()
                return Token(TokenType.LPAREN, '(')

            elif self.current_char == ')':
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
