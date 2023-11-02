import NxN


def convert(n: int = NxN.n, alg: str = "") -> str:
    alg = alg.upper().split(" ")

    code = ""
    for step in alg:
        if step == "":
            continue
            
        if step[0] in "XYZ":
            if not step[-1].isalnum():
                step = step[:-1] + "3"
            elif step[-1].isalpha():
                step += "1"
            step += "(); "

        else:
            wide = "W" in step
            step = step.replace("W", "")
            
            if not step[-1].isalnum():
                step = step[:-1] + "3"
            elif step[-1].isalpha():
                step += "1"
            if step[0].isalpha():
                step = ("2" if wide else "1") + step

            layers = ""
            while step[0].isdigit():
                layers += step[0]
                step = step[1:]
            layers = int(layers)

            face = step[0]
            turns = int(step[1:])
            
            if layers > 1 and not wide:
                if face in "DBR":
                    layers = n - layers + 1
                    turns = 4 - turns
                if face in "UD":
                    face = "E"
                elif face in "FB":
                    face = "S"
                else:
                    face = "M"

            step = f"{face}{turns}({layers}); "

        code += "NxN." + step
        
    return code + "NxN.display()"


help = """• \u001b[1mHELP: \u001b[22;3mShows list of commands.\u001b[23m
• \u001b[1mRESET: \u001b[22;3mResets the cube to solved state.\u001b[23m
• \u001b[1mEXIT: \u001b[22;3mTerminates program.\u001b[23m
• \u001b[1mRESIZE: \u001b[22;3mLets you resize the cube.\u001b[23m
• \u001b[1mHISTORY: \u001b[22;3mShows past moves.\u001b[23m
• \u001b[1mCLEAR: \u001b[22;3mClears past moves.\u001b[23m

• \u001b[1mU: \u001b[22;3mTurns the top layer 90° clockwise.\u001b[23m
• \u001b[1mD: \u001b[22;3mTurns the bottom layer 90° clockwise.\u001b[23m
• \u001b[1mF: \u001b[22;3mTurns the front layer 90° clockwise.\u001b[23m
• \u001b[1mB: \u001b[22;3mTurns the back layer 90° clockwise.\u001b[23m
• \u001b[1mL: \u001b[22;3mTurns the left layer 90° clockwise.\u001b[23m
• \u001b[1mR: \u001b[22;3mTurns the right layer 90° clockwise.\u001b[23m
• \u001b[1mU': \u001b[22;3mTurns the top layer 90° counterclockwise.\u001b[23m
• \u001b[1mU2: \u001b[22;3mTurns the top layer 180°.\u001b[23m
• \u001b[1m#U: \u001b[22;3mTurns the #ᵗʰ layer from the top 90° clockwise.\u001b[23m
• \u001b[1mUw: \u001b[22;3mTurns the second layer from the top 90° clockwise.\u001b[23m
• \u001b[1m#Uw: \u001b[22;3mTurns the top # layers 90° clockwise.\u001b[23m

• \u001b[1mX: \u001b[22;3mTurns the entire cube 90° clockwise, relative to the left face.\u001b[23m
• \u001b[1mY: \u001b[22;3mTurns the entire cube 90° clockwise, relative to the top face.\u001b[23m
• \u001b[1mZ: \u001b[22;3mTurns the entire cube 90° clockwise, relative to the front face.\u001b[23m
• \u001b[1mX': \u001b[22;3mTurns the entire cube 90° counterclockwise, relative to the left face.\u001b[23m
• \u001b[1mX2: \u001b[22;3mTurns the entire cube 180°, relative to the left face.\u001b[23m"""