def evalRPN(tokens: list[str]) -> int:
    stack = []
    for token in tokens:
        if token in ["+","-","*","/"]:
            r = stack.pop()
            l = stack.pop()
            eq = l + token + r
            res = str(int(eval(eq)))
            stack.append(res)
        else:
            stack.append(token)
    return int(stack[0])
