import sys
from collections import deque

def plus(y, x):
    return x + y
    
def minus(y, x):
    return x - y

def asterisk(y, x):
    return x * y

def plusplus(x):
    return x + 1 

def at(z, y, x):
    return x * y + y * z + z * x
    
def main(lines):
    input_line = lines[0].split()
    queue = deque()
    invalid = False
    operator = {'++': (1, plusplus), '+': (2, plus), '-': (2, minus), '*': (2, asterisk), '@': (3, at)}

    for item in input_line:
        if item.isdecimal():
            queue.append(int(item))
        elif item in operator.keys():
            operand_num, func = operator[item]
            if len(queue) >= operand_num:
                operand = [queue.pop() for i in range(operand_num)]
                queue.append(func(*operand))
            else:
                invalid = True
                break
        else:
            invalid = True
            break

    if len(queue) == 1 and invalid == False:
        ans = queue.pop()
        print(ans)
    else:
        print("invalid")

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
