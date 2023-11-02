import notation
import NxN

n = NxN.init(int(input("\u001b[HN = ") or 3))

history = []
last = ""

NxN.display()
while True:
    cmd = input("\u001b[38;2;191;191;255;1m") or last

    if cmd == "":
        NxN.display()
        
    if cmd == "RESET":
        history += cmd
        NxN.init(n)
        NxN.display()
        
    elif cmd == "EXIT":
        print ("\u001b[2J\u001b[H\u001b[m", end = "")
        break
        
    elif cmd == "RESIZE":
        history += cmd
        n = NxN.init(int(input("\u001b[2J\u001b[H\u001b[mN = ") or n))
        NxN.display()
        
    elif cmd == "HISTORY":
        print ("\u001b[2J\u001b[H\u001b[m", *(f">> \u001b[2m{x}\u001b[m\n" for x in history), sep = "", end = "")
        input()
        NxN.display()
        
    elif cmd == "CLEAR":
        history = []
        last = ""
        NxN.display()

    elif cmd == "HELP":
        print (f"\u001b[2J\u001b[H\u001b[m{notation.help}\u001b[m" + "\n" * n)
        input()
        NxN.display()

    else:
        history += cmd
        last = cmd
        exec(notation.convert(n, cmd))