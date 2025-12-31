# [^,+,*,2,x,*,3,y,*,2,z]

from enum import Enum


DatasetPl = ['^','+','*',2,'x','*',3,'y','*',2,'z']

# for index, item in enumerate(DatasetPl):
    # print(item)
    
class FunctionFlag(Enum):
    EXP = "^"
    MUL = "*"
    ADD = "+"
    
Variables = ['x','y','z']
    
# def RootRecursion(DataPL):
#     FirstChar = DataPL[0]
    
#     print(FirstChar)
    
def toString(tokens):
    stack = []
    
    # Operators and their "arity" (number of arguments)
    binary_ops = ['+', '-', '*', '/', '^']
    unary_ops = ['sin', 'cos', 'tan', 'ln', 'exp']
    
    print(tokens)

    # Process from right to left
    for token in reversed(tokens):
        print(f'SYM---{token}')
        if token in binary_ops:
            # Pop two operands for binary
            op1 = stack.pop()
            op2 = stack.pop()
            # Construct infix string
            new_expr = f"({op1} {token} {op2})"
            stack.append(new_expr)
            
        elif token in unary_ops:
            # Pop one operand for unary
            op1 = stack.pop()
            # Construct function string
            new_expr = f"{token}({op1})"
            stack.append(new_expr)
            
        else:
            # It's a number or variable (Leaf node)
            stack.append(str(token))
            
    return stack[0]

# Example usage:
# ln(x^2 + 1) in Prefix: ['ln', '+', '^', 'x', 2, 1]
expression = ['ln', '+', '^', 'x', 2, 1]
# print(toString(DatasetPl)) 
# Output: ln((x ^ 2) + 1)
   
   
    
    
# print(RootRecursion(DatasetPl))


import numpy as np

def FX_Generator(tokens, data_map):
    """
    tokens: List of prefix tokens e.g. ['+', 'x', 'y']
    data_map: Dict of arrays e.g. {'x': np.array([1, 2]), 'y': np.array([3, 4])}
    """
    # We use a copy of the tokens because pop(0) is destructive
    tokens_working = list(tokens)

    def evaluate():
        token = tokens_working.pop(0)
        print(token)
        # 1. Handle Variables
        if isinstance(token, str) and token.lower() in data_map:
            return data_map[token.lower()]

        # 2. Handle Constants
        if isinstance(token, (int, float)):
            return np.full_like(next(iter(data_map.values())), token, dtype=float)

        # 3. Handle Binary Operators
        
        '''
        Each time Evaluate is called, it goes to the Next item in the polish thing
        
        
        This is hella cool
        
        cause think of it as a tree
        
        the ^ needs two
        
        hence it calls it twice, 
        
        now upon calling it the first time, we get a +
        
        the plus does its whole thing (same) and it REMOVES IT FROM THE WHOLE TOKENLIST
        
        now when the 2nd evaluate is called, all thats left is just the other bit needed for the exponent
        
        hence davai
        '''
        if token == '+':
            return evaluate() + evaluate()
        elif token == '-':
            return evaluate() - evaluate()
        elif token == '*':
            return evaluate() * evaluate()
        elif token == '/':
            return evaluate() / evaluate()
        elif token == '^':
            base = evaluate()
            exp = evaluate()
            return np.power(base, exp)

        # 4. Handle Unary Operators
        elif token == 'sin':
            return np.sin(evaluate())
        elif token == 'ln':
            # We use np.abs or a clip to prevent NaNs in regression
            return np.log(np.abs(evaluate()) + 1e-9)
        
    return evaluate()

print(FX_Generator(DatasetPl,{'x': 2, 'y': 1,'z':1}))