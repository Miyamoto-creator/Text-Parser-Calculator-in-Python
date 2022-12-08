from Lexer import Lexer, TokenType, Token


# test all methods from Lexer.py



def test_lexer_Scanner():
    text = "3"
    lexer = Lexer(text)
    assert lexer.Scanner() == Token(TokenType.INTEGER, 3)

def test_lexer_Scanner2():
    text = "3+3"
    lexer = Lexer(text)
    assert lexer.Scanner() == Token(TokenType.INTEGER, 3)


def test_lexer_Tokenizer():
    text = "3"
    lexer = Lexer(text)
    assert lexer.Tokenizer() == [Token(TokenType.INTEGER, 3), Token(TokenType.EOF, None)]

def test_lexer_Tokenizer2():
    text = "3+3"
    lexer = Lexer(text)
    assert lexer.Tokenizer() == [Token(TokenType.INTEGER, 3), Token(TokenType.PLUS, '+'), Token(TokenType.INTEGER, 3), Token(TokenType.EOF, None)]

def test_lexer_integer():
    text = "3"
    lexer = Lexer(text)
    assert lexer.integer() == 3

def test_lexer_integer2():
    text = "33"
    lexer = Lexer(text)
    assert lexer.integer() == 33

def test_lexer_integer3():
    text = "333"
    lexer = Lexer(text)
    assert lexer.integer() == 333

def test_lexer_integer4():
    text = "3333"
    lexer = Lexer(text)
    assert lexer.integer() == 3333

def test_lexer_integer5():
    text = "33333"
    lexer = Lexer(text)
    assert lexer.integer() == 33333

def test_lexer_integer6():
    text = "333333"
    lexer = Lexer(text)
    assert lexer.integer() == 333333

def test_lexer_integer7():
    text = "3333333"
    lexer = Lexer(text)
    assert lexer.integer() == 3333333

# test float
def test_lexer_float():
    text = "3.3"
    lexer = Lexer(text)
    assert lexer.float() == 3.3

def test_lexer_float2():
    text = "3.33"
    lexer = Lexer(text)
    assert lexer.float() == 3.33

def test_lexer_float3():
    text = "3.333"
    lexer = Lexer(text)
    assert lexer.float() == 3.333

def test_lexer_float4():
    text = "3.3333"
    lexer = Lexer(text)
    assert lexer.float() == 3.3333

def test_lexer_float5():
    text = "3.33333"
    lexer = Lexer(text)
    assert lexer.float() == 3.33333

# test other shit

def test_lexer_whitespace():
    text = " 3"
    lexer = Lexer(text)
    assert lexer.skipWhiteSpace() == None

def test_lexer_whitespace2():
    text = "  3"
    lexer = Lexer(text)
    assert lexer.skipWhiteSpace() == None

def test_lexer_whitespace3():
    text = "   3"
    lexer = Lexer(text)
    assert lexer.skipWhiteSpace() == None

# test other methods

