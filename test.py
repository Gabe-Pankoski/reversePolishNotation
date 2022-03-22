from reversePolishNotation import evalRPN

def testRPN():
    eq1 = [ "1", "2", "+", "1", "-" ] #2
    eq2 = [ "1", "1", "1", "+", "+"  ] #3
    eq3 = [ "-1", "2", "+", "2", "*" ] #2
    eq4 = [ "10", "5", "5", "+", "/" ] #5
    eq5 = [ "10", "3", "2", "+", "-" ] #5
    eq6 = [ "10", "3", "2", "+", "+", "-1", "*" ] #6

    assert evalRPN(eq1) == 2
    assert evalRPN(eq2) == 3
    assert evalRPN(eq3) == 2
    assert evalRPN(eq4) == 1
    assert evalRPN(eq5) == 5
    assert evalRPN(eq6) == -15