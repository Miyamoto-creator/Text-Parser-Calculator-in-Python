import Parser
import pytest


def test_factor():
    text = "3"
    tokenizer = Parser.Tokenizer(text)
    parser = Parser.Parser(tokenizer)
    assert parser.factor() == 3


def test_factor2():
    text = "-3"
    tokenizer = Parser.Tokenizer(text)
    parser = Parser.Parser(tokenizer)
    assert parser.factor() == -3


def test_factor3():
    text = "(3)"
    tokenizer = Parser.Tokenizer(text)
    parser = Parser.Parser(tokenizer)
    assert parser.factor() == 3


def test_expr():
    text = "3+3"
    tokenizer = Parser.Tokenizer(text)
    parser = Parser.Parser(tokenizer)
    assert parser.expr() == 6


def test_expr2():
    text = "3-3"
    tokenizer = Parser.Tokenizer(text)
    parser = Parser.Parser(tokenizer)
    assert parser.expr() == 0


def test_expr3():
    text = "5--5"
    tokenizer = Parser.Tokenizer(text)
    parser = Parser.Parser(tokenizer)
    assert parser.expr() == 10

def test_expr4():
    text = "5---5"
    tokenizer = Parser.Tokenizer(text)
    parser = Parser.Parser(tokenizer)
    assert parser.expr() == 0

def test_expr5():
    text = "5+----5"
    tokenizer = Parser.Tokenizer(text)
    parser = Parser.Parser(tokenizer)
    assert parser.expr() == 10

# test another expression

def test_expr6():
    text = "5+5*5"
    tokenizer = Parser.Tokenizer(text)
    parser = Parser.Parser(tokenizer)
    assert parser.expr() == 30

# test expression with parenthesis

def test_expr7():
    text = "(5+5)*5"
    tokenizer = Parser.Tokenizer(text)
    parser = Parser.Parser(tokenizer)
    assert parser.expr() == 50

# test expression with parenthesis

def test_expr8():
    text = "(5+5)*5/5"
    tokenizer = Parser.Tokenizer(text)
    parser = Parser.Parser(tokenizer)
    assert parser.expr() == 10

# test expression with parenthesis

def test_expr9():
    text = "(5+5)*5/5-5"
    tokenizer = Parser.Tokenizer(text)
    parser = Parser.Parser(tokenizer)
    assert parser.expr() == 5

# test expression with parenthesis and empty spaces

def test_expr10():
    text = "(5 + 5) * 5 / 5 - 5"
    tokenizer = Parser.Tokenizer(text)
    parser = Parser.Parser(tokenizer)
    assert parser.expr() == 5

# test expression with parenthesis and empty spaces

def test_expr11():
    text = "(5 + 5) * 5 / 5 - 5"
    tokenizer = Parser.Tokenizer(text)
    parser = Parser.Parser(tokenizer)
    assert parser.expr() == 5

# test empty expression

def test_expr12():
    text = ""
    tokenizer = Parser.Tokenizer(text)
    parser = Parser.Parser(tokenizer)
    assert parser.expr() == None

# test expression with nothing but operators

def test_expr13():
    text = "++++"
    tokenizer = Parser.Tokenizer(text)
    parser = Parser.Parser(tokenizer)
    assert parser.expr() == None






