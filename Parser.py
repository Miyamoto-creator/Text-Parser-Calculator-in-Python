# Python 3

from Lexer import Lexer, TokenType


# Parser for text calculator
class Parser:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.current_token = self.tokenizer.Scanner()
        # self.logger = logging.getLogger('Parser')
        # self.logger.setLevel(logging.DEBUG)
        # self.logger.addHandler(logging.StreamHandler())
        # self.logger.debug('Parser initialized')

    # Error handling
    def error(self):
        raise Exception('Invalid syntax')

    # Eat the current token and move to the next token
    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.tokenizer.Scanner()
        else:
            self.error()

    # Parse the expression
    def parse(self):
        result = self.expr()
        if self.current_token.type != TokenType.EOF:
            self.error()
        return result

    # Parse the expression
    def expr(self):

        # Parse the first term
        result = self.term()

        # Parse the rest of the expression
        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            token = self.current_token

            # Token type is PLUS
            if token.type == TokenType.PLUS:
                self.eat(TokenType.PLUS)
                result = result + self.term()

            # Token type is MINUS
            elif token.type == TokenType.MINUS:
                self.eat(TokenType.MINUS)
                result = result - self.term()
        return result

    # Parse the term
    def term(self):

        # Parse the first factor
        result = self.factor()

        # Parse the rest of the term
        while self.current_token.type in (TokenType.EXP, TokenType.MUL, TokenType.DIV):
            token = self.current_token
            # Token type is EXP
            if token.type == TokenType.EXP:
                self.eat(TokenType.EXP)
                result = result ** self.factor()
            # Token type is MUL
            elif token.type == TokenType.MUL:
                self.eat(TokenType.MUL)
                result = result * self.factor()
            # Token type is DIV
            elif token.type == TokenType.DIV:
                self.eat(TokenType.DIV)
                result = result / self.factor()
        return result

    # Parse the factor
    def factor(self):

        # Token type is INTEGER
        if self.current_token.type == TokenType.INTEGER:
            token = self.current_token
            self.eat(TokenType.INTEGER)
            return token.value

        # Token type is LPAREN
        elif self.current_token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            result = self.expr()
            self.eat(TokenType.RPAREN)
            return result

        # Token type is MINUS
        elif self.current_token.type == TokenType.MINUS:
            self.eat(TokenType.MINUS)
            return -self.factor()

        # Token type is PLUS
        elif self.current_token.type == TokenType.PLUS:
            self.eat(TokenType.PLUS)
            return self.factor()

        # Token type is EOF
        elif self.current_token.type == TokenType.EOF:
            return None

        # Token type is not INTEGER, LPAREN, MINUS, PLUS or EOF
        else:
            self.error()


# Test the parser manually if needed.
def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        tokenizer = Lexer(text)
        parser = Parser(tokenizer)
        result = parser.parse()
        print(result)


if __name__ == '__main__':
    main()
