import sys
from collections import deque

def main(lines):
    input_line = lines[0].split()
    queue = deque()
    for item in input_line:
        if item.isdecimal():
            queue.append(int(item))
        elif item == "+":
            if len(queue) >= 2:
                new_item = queue.pop() + queue.pop()
                queue.append(new_item)
            else:
                print("invalid")
                break
        elif item == "-":
            if len(queue) >= 2:
                new_item = - queue.pop() + queue.pop()
                queue.append(new_item)
            else:
                print("invalid")
                break
        elif item == "*":
            if len(queue) >= 2:
                new_item = queue.pop() * queue.pop()
                queue.append(new_item)
            else:
                print("invalid")
                break
        elif item == "++":
            if len(queue) >= 1:
                new_item = queue.pop() + 1
                queue.append(new_item)
            else:
                print("invalid")
                break
        elif item == "@":
            if len(queue) >= 3:
                x = queue.pop()
                y = queue.pop()
                z = queue.pop()
                new_item = x * y + y * z + z * x
                queue.append(new_item)
            else:
                print("invalid")
                break
        else:
            print("invalid")
            break

    if len(queue) == 1:
        ans = queue.pop()
        print(ans)
    else:
        print("invalid")

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
