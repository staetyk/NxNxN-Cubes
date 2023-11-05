import notation
import NxN
import os


checkW = lambda x : os.get_terminal_size()[0] >= ((6 * x) + 10)
checkH = lambda x : os.get_terminal_size()[1] >= ((8 * x) + 13)
checkSize = lambda x : checkW() and checkH()


n = 3

def changeSize() -> None:
    global n
    while True:
        N = NxN.init(int(input("\u001b[HN = ") or n))
        if not checkSize(N):
            print("\u001b[1;31mError: Terminal size too small.\u001b[0m")
        else:
            break
    n = N

changeSize()

             
history = []
last = ""

NxN.display()
while True:
    cmd = input("\u001b[38;2;191;191;255;1m") or last

    try:
        if cmd == "":
            NxN.display()
        
        elif cmd.upper() == "RESET":
            history.append(cmd)
            NxN.init(n)
            NxN.display()
        
        elif cmd.upper() == "EXIT":
            print ("\u001b[2J\u001b[H\u001b[m", end = "")
            break
        
        elif cmd.upper() == "RESIZE":
            history.append(cmd)
            changeSize()
            NxN.display()
        
        elif cmd.upper() == "HISTORY":
            print ("\u001b[2J\u001b[H\u001b[m", *(f">> \u001b[2m{x}\u001b[m\n" for x in history), sep = "", end = "")
            input()
            NxN.display()
        
        elif cmd.upper() == "CLEAR":
            history = []
            last = ""
            NxN.display()

        elif cmd.upper() == "HELP":
            print (f"\u001b[2J\u001b[H\u001b[m{notation.help}\u001b[m", sep = "", end = "")
            input()
            NxN.display()

        else:
            history.append(cmd)
            last = cmd
            exec(notation.convert(n, cmd))

    except Exception as _:
       NxN.display()