import notation
import NxN
import os



checkW = lambda x : os.get_terminal_size().columns >= ((x * 6) + 10)
checkH = lambda x : os.get_terminal_size().lines >= ((x * 8) + 5)
checkSize = lambda x : checkW(x) and checkH(x)


def error(x: BaseException | Exception) -> None:
    print (f"\u001b[2J\u001b[H\u001b[m\u001b[1;38;2;255;0;0m{str(x.args).strip('(').strip(')')}\u001b[m", sep = "", end = "")
    input()
    NxN.display()


n = 3

def changeSize() -> None:
    global n
    N = int(input("\u001b[2J\u001b[H\u001b[mN = \u001b[4m") or n)
    print("\u001b[24m")
    if not checkSize(N):
        error(Exception("Terminal size too small."))
        changeSize()
    else:
        n = NxN.init(N)

changeSize()

             
history = []
last = ""

NxN.display()
while True:
    cmd = input("\u001b[38;2;191;191;255;1m") or last

    try:
        if cmd == "":
            pass
        
        if cmd.upper() == "RESET":
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
            try:
                txt = notation.convert(n, cmd)
            except Exception as e:
                error(e)
            else:
                exec(txt)
                history.append(cmd)
                last = cmd

    except Exception as e:
        error(e)