# Contains TokenType, Token, and Tokenizer classes for the parser calculator

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


# Tokenizer Class that uses the Token Class and includes the method scanner() that returns a list of tokens

class Tokenizer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if len(text) > 0 else None
        self.Tokens = []

    def error(self):
        raise Exception('Error parsing input')

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skipWhiteSpace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def getNextToken(self):
        while self.current_char is not None:
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

    # Defines logic for multiple mathematical operators like minus or plus happening right after each other
    def opEdgeCases(self, tokens, token):
        if tokens[-1].type == TokenType.MINUS and tokens[-2].type == TokenType.MINUS:
            tokens.remove(token)
            tokens[-1].type = TokenType.PLUS
            tokens[-1].value = '+'

        # plus plus turns into plus
        elif tokens[-1].type == TokenType.PLUS and tokens[-2].type == TokenType.PLUS:
            tokens.remove(token)

        # plus minus turns into minus
        elif tokens[-1].type == TokenType.MINUS and tokens[-2].type == TokenType.PLUS:
            tokens.remove(token)
            tokens[-1].type = TokenType.MINUS
            tokens[-1].value = '-'

        # minus plus turns into minus
        elif tokens[-1].type == TokenType.PLUS and tokens[-2].type == TokenType.MINUS:
            tokens.remove(token)
            tokens[-1].type = TokenType.MINUS
            tokens[-1].value = '-'

    def scanner(self):
        while True:
            token = self.getNextToken()
            self.Tokens.append(token)
            if token.type == TokenType.EOF:
                break

            # Checks if token list includes two consecutive minus signs
            # If they do, it removes the first one and changes the second one to a plus sign

            # turn this into its own function
            self.opEdgeCases(self.Tokens, token)

        return self.Tokens


# Test the tokenizer with user input
def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        tokenizer = Tokenizer(text)
        tokens = tokenizer.scanner()
        print(tokens)


if __name__ == '__main__':
    main()
