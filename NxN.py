from collections.abc import Callable
import math
import os


scheme = {
    "white": "\u001b[38;2;255;255;255m\u2588\u2588\u001b[38;2;64;64;64m",
    "yellow": "\u001b[38;2;255;255;0m\u2588\u2588\u001b[38;2;64;64;64m",
    "green": "\u001b[38;2;0;200;0m\u2588\u2588\u001b[38;2;64;64;64m",
    "blue": "\u001b[38;2;0;100;255m\u2588\u2588\u001b[38;2;64;64;64m",
    "red": "\u001b[38;2;255;0;0m\u2588\u2588\u001b[38;2;64;64;64m",
    "orange": "\u001b[38;2;255;127;0m\u2588\u2588\u001b[38;2;64;64;64m"
}


def init(size: int = 3) -> int:
    print ("\u001b[2J\u001b[H")

    if 1 > size:
        raise ValueError()
    
    global n
    n = size
    
    global state
    state = []
    for x in scheme.keys():
        face = []
        for _ in range(n):
            row = []
            for _ in range(n):
                row.append(x)
            face.append(row)
        state.append(face)

    return n

init()
    

def turn(*cycles: list[tuple[int, int, int]]) -> None:
    global state
    for x in cycles:
        x = x[::-1]
        a = state[x[0][0]][x[0][1]][x[0][2]]
        for i in range(1, len(x)):
            state[x[i-1][0]][x[i-1][1]][x[i-1][2]] = state[x[i][0]][x[i][1]][x[i][2]]
        state[x[-1][0]][x[-1][1]][x[-1][2]] = a


turnFace = lambda f, x, y: turn([(f, x, y), (f, y, -x-1), (f, -x-1, -y-1), (f, -y-1, x)])
turnU = lambda x, y: turn([(2, x, y), (5, x, y), (3, -x-1, -y-1), (4, x, y)])
turnL = lambda x, y: turn([(0, x, y), (3, x, y), (1, x, y), (2, x, y)])
turnF = lambda x, y: turn([(0, -x-1, -y-1), (4, -y-1, x), (1, x, y), (5, y, -x-1)])
turnD = lambda x, y: turn([(2, -x-1, -y-1), (4, -x-1, -y-1), (3, x, y), (5, -x-1, -y-1)])
turnR = lambda x, y: turn([(1, -x-1, -y-1), (3, -x-1, -y-1), (0, -x-1, -y-1), (2, -x-1, -y-1)])
turnB = lambda x, y: turn([(1, -x-1, -y-1), (4, y, -x-1), (0, x, y), (5, -y-1, x)])


def move(face: int, func: Callable, l: int, direction: bool) -> None:
    if not 0 < l < n:
        raise ValueError()
        
    for i in range(math.ceil(n / 2)):
        for j in range(n // 2):
            turnFace(face, i, j)

    for i in range(l):
        for j in range(n):
            (func(i, j) if direction else func(j,i))


def slice(func: Callable, l: int, direction: bool) -> None:
    if not 1 < l < n:
        raise ValueError()

    for i in range(n):
        (func(l - 1, i) if direction else func(i, l - 1))


U = U1 = lambda l = 1: move(0, turnU, l, True)
D = D1 = lambda l = 1: move(1, turnD, l, True)
F = F1 = lambda l = 1: move(2, turnF, l, True)
B = B1 = lambda l = 1: move(3, turnB, l, True)
R = R1 = lambda l = 1: move(4, turnR, l, False)
L = L1 = lambda l = 1: move(5, turnL, l, False)

Y = Y1 = lambda: exec("U(n-1); D3(1)")
Z = Z1 = lambda: exec("F(n-1); B3(1)")
X = X1 = lambda: exec("L(n-1); R3(1)")

U2 = lambda l = 1: exec(f"U({l}); U({l})")
U3 = lambda l = 1: exec(f"U({l}); U({l}); U({l})")
D2 = lambda l = 1: exec(f"D({l}); D({l})")
D3 = lambda l = 1: exec(f"D({l}); D({l}); D({l})")
F2 = lambda l = 1: exec(f"F({l}); F({l})")
F3 = lambda l = 1: exec(f"F({l}); F({l}); F({l})")
B2 = lambda l = 1: exec(f"B({l}); B({l})")
B3 = lambda l = 1: exec(f"B({l}); B({l}); B({l})")
R2 = lambda l = 1: exec(f"R({l}); R({l})")
R3 = lambda l = 1: exec(f"R({l}); R({l}); R({l})")
L2 = lambda l = 1: exec(f"L({l}); L({l})")
L3 = lambda l = 1: exec(f"L({l}); L({l}); L({l})")

Y2 = lambda: exec("Y(); Y()")
Y3 = lambda: exec("Y(); Y(); Y()")
Z2 = lambda: exec("Z(); Z()")
Z3 = lambda: exec("Z(); Z(); Z()")
X2 = lambda: exec("X(); X()")
X3 = lambda: exec("X(); X(); X()")


def display() -> None:
    layout = "\u250fC"
    layout += "\u2501C" * (n * 2 + 2)
    layout += "\u2513CN"
    for i in range(n):
        layout += "\u2503C C"
        for j in range(n):
            layout += scheme[state[0][i][j]]
            layout += "CC"
        layout += " C\u2503CN"
    layout += "\u250fC"
    layout += "\u2501C" * (n * 2 + 2)
    layout += "\u254bC"
    layout += "\u2501C" * (n * 2 + 2)
    layout += "\u254bC"
    layout += "\u2501C" * (n * 2 + 2)
    layout += "\u2513CN"
    for i in range(n):
        layout += "\u2503C C"
        for j in range(n):
            layout += scheme[state[5][i][j]]
            layout += "CC"
        layout += " C\u2503C C"
        for j in range(n):
            layout += scheme[state[2][i][j]]
            layout += "CC"
        layout += " C\u2503C C"
        for j in range(n):
            layout += scheme[state[4][i][j]]
            layout += "CC"
        layout += " C\u2503CN"
    layout += "\u2517C"
    layout += "\u2501C" * (n * 2 + 2)
    layout += "\u254bC"
    layout += "\u2501C" * (n * 2 + 2)
    layout += "\u254bC"
    layout += "\u2501C" * (n * 2 + 2)
    layout += "\u251bCN"
    for i in range(n):
        layout += "\u2503C C"
        for j in range(n):
            layout += scheme[state[1][i][j]]
            layout += "CC"
        layout += " C\u2503CN"
    layout += "\u2523C"
    layout += "\u2501C" * (n * 2 + 2)
    layout += "\u252bCN"
    for i in range(n):
        layout += "\u2503C C"
        for j in range(n):
            layout += scheme[state[3][i][j]]
            layout += "CC"
        layout +=" C\u2503CN"
    layout += "\u2517C"
    layout += "\u2501C" * (n * 2 + 2)
    layout += "\u251bC"

    shown = "\u001b[2J\u001b[H\u001b[m\u001b[38;2;64;64;64m"
    layout = layout.split("N")
    w = os.get_terminal_size().columns
    for x in layout:
        shown += ("x" * x.count("C"))\
        .title()\
        .center(w)\
        .replace("x", "")\
        .replace("X", x.replace("C", ""))\
        + "\n"
        
    print (shown)